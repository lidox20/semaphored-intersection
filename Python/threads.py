# threads.py
from threading import Thread, Semaphore
from time import sleep
import settings
from mspdebug import *
import painting

fasttimer = Semaphore(value = 0)
regularsem = Semaphore(value = 0)
transitionsem = Semaphore(value = 0)
fast_timer_cond = True
regular_timer_cond = True
yellow_cond = True
trans_cond = True

E = 1
D = 0
blinked = 0
index = 0
opCodeFirst = 0
opCodeSecond = 0

#################################################
#first byte
map_sem1 = {settings.RY : 0, settings.G : 1, settings.Y : 2, settings.R : 3, settings.BG : 1}
map_sem2 = {settings.RY : 0, settings.G : 4, settings.Y : 8, settings.R : 12, settings.BG : 4}
map_semp3 = {settings.R : 0, settings.G : 16, settings.BG : 16}
map_semp4 = {settings.R : 0, settings.G : 32, settings.BG : 32}
map_es1 = {E : 64, D : 0}
map_es2 = {E : 128, D : 0}

#second byte
map_esp3 = {E : 1, D : 0}
map_esp4 = {E : 2, D : 0}
map_con = {E : 4, D : 0}
################################################


def getOpCodeOne(sem1, sem2, semp3, semp4):
    global map_sem1, map_sem2, map_semp3, map_sem4, map_es1, map_es2,map_esp3 ,map_esp4,map_con, E, D
    opCode = 0
    opCode = opCode | map_sem1[sem1]
    opCode = opCode | map_sem2[sem2]
    opCode = opCode | map_semp3[semp3]
    opCode = opCode | map_semp4[semp4]
    opCode = opCode | map_es1[E]
    opCode = opCode | map_es2[E]
    print('*********')
    print(hex(opCode))
    print('*********')
    return opCode

def getOpCodeTwo(): #con):
    global map_sem1, map_sem2, map_semp3, map_sem4, map_es1, map_es2,map_esp3 ,map_esp4,map_con, E, D

    opCode = 0
    #opCode = opCode | map_con[con]
    opCode = opCode | map_esp3[E]
    opCode = opCode | map_esp4[E]
    return opCode


# Fast blinking thread
def fast_timer():
    global fast_timer_cond, blinked
    global opCodeFirst, opCodeSecond
    global fasttimer
    blinked = 0
    fasttimer.acquire()
    while( fast_timer_cond ):
        blinked += 1
        settings.mutex.acquire()
        toggle_semaphores( opCodeFirst, opCodeSecond )
        settings.mutex.release()
        sleep(0.34)
        if ( blinked == 3 ):
            blinked = 0
            settings.sem.release()
            fasttimer.acquire()


# Transition thread
def transition():
    R = settings.R
    Y = settings.Y
    global trans_cond, index, transitionsem
    while( trans_cond ):
        # Block this thread on transition semahpore
        settings.transitionsem.acquire()
        if ( trans_cond == False ):
            return

        # Unlock blinking semaphore
        settings.mutex.acquire()
        settings.yellowThread = True
        settings.yellowblink.release()
        settings.mutex.release()

        # Sleep for blink period
        sleep(2)

        # Set variables
        settings.mutex.acquire()
        settings.yellowThread = False
        index = 0
        settings.regularThread = True
        settings.mutex.release()

        # Set fixed Yellow light for another 2 seconds
        f = getOpCodeOne( Y, Y, R, R )
        painting.clear_all_lights()
        send_to_msp( f, 0 )
        sleep(2)

        # Unblock regular timer
        settings.mutex.acquire()
        settings.isTransition = False
        settings.mutex.release()
        settings.sem.release()

# Yellow blinking thread
def yellow():
    global yellow_cond, map_es1, map_es2, index, transitionsem
    Y = settings.Y
    R = settings.R

    first = getOpCodeOne( Y, Y, R, R )
    while( yellow_cond ):
        # Check for blocking indicator of the yellow blinking thread
        if ( settings.yellowThread == False ):
            settings.mutex.acquire()
            index = 0
            settings.mutex.release()

            # Block yellow blinking thread
            settings.yellowblink.acquire()
            if ( yellow_cond == False ):
                return
        else:
            # Check if thread is ready to go
            # If not, block & wait
            # If thread finished, just exit function
            if ( settings.yellowThread == False ):
                settings.yellowblink.acquire()
                if ( yellow_cond == False ):
                    return

            # Send data to MSP430
            settings.mutex.acquire()
            send_to_msp( first , 0 )
            settings.mutex.release()
            first ^= map_es1[E]
            first ^= map_es2[E]
            sleep(0.5)

# Regular thread
def regular_timer():
    global map_sem1, map_sem2, map_semp3, map_sem4, map_es1, map_es2,map_esp3 ,map_esp4,map_con, E, D
    global opCodeFirst, opCodeSecond
    global regular_timer_cond, regularsem, index, fasttimer

    settings.sem.acquire()
    while( regular_timer_cond ):
        settings.mutex.acquire()
        index = 0
        settings.mutex.release()
        while(index < len(settings.semlist1) and regular_timer_cond):
            if ( settings.regularThread == False ):
                settings.sem.acquire()
            opCodeFirst = getOpCodeOne(settings.semlist1[index], settings.semlist2[index],settings.semplist3[index],settings.semplist4[index])
            opCodeSecond = getOpCodeTwo()#settings.semlistcond[x])
            if ( is_blinking( settings.semlist1[index], settings.semlist2[index], settings.semplist3[index], settings.semplist4[index]) ):
                fasttimer.release()
                settings.sem.acquire()
            else :
                # Check if regular thread is ready to go
                # If not, block & wait
                # If thread finished, just exit function
                if ( settings.regularThread == False ):
                    settings.sem.acquire()
                    if ( regular_timer_cond == False ):
                        return

                # Send data to MSP430
                settings.mutex.acquire()
                send_to_msp(opCodeFirst, opCodeSecond)
                settings.mutex.release()
                sleep(1)
            settings.mutex.acquire()
            index += 1
            settings.mutex.release()

    return



# Toggle semaphores
def toggle_semaphores( ocf, ocs ):
    global E, D, index, opCodeFirst, opCodeSecond
    global map_es1, map_es2, map_esp3, map_esp4
    BG = settings.BG

    # S1 semaphore
    if ( settings.semlist1[index] == BG ):
        opCodeFirst ^= map_es1[E]

    # S2 semaphore
    if ( settings.semlist2[index] == BG ):
        opCodeFirst ^= map_es2[E]

    # Passengers semaphore 3
    if ( settings.semplist3[index] == BG ):
        opCodeSecond ^= map_esp3[E]

    # Passenger semaphore 4
    if ( settings.semplist4[index] == BG ):
        opCodeSecond ^= map_esp4[E]
    send_to_msp( opCodeFirst, opCodeSecond )


# Determine if it's blinking
def is_blinking( s1, s2, p1, p2 ):
    BG = settings.BG
    t = (s1 == BG or s2 == BG or p1 == BG or p2 == BG)
    return t

# Create & Start threads
def start_threads():
    settings.t_yellowblink = Thread(target = yellow)
    settings.t_fasttimer = Thread(target = fast_timer)
    settings.t_regulartimer = Thread(target = regular_timer)
    settings.t_transition = Thread(target = transition)
    settings.t_fasttimer.start()
    settings.t_regulartimer.start()
    settings.t_yellowblink.start()
    settings.t_transition.start()
    # settings.thread = Thread(target = threaded_function, args = (10, ))
    # settings.thread.start()

def finish_threads():
    global fast_timer_cond, regular_timer_cond, yellow_cond, trans_cond, transition
    fast_timer_cond = False
    regular_timer_cond = False
    yellow_cond = False
    trans_cond = False
    fasttimer.release()
    settings.sem.release()
    settings.transitionsem.release()
    settings.yellowblink.release()
    # Wait for threads to complete
    # settings.t_yellowblink.join()
    # settings.t_fasttimer.join()
    # settings.t_regulartimer.join()
    # settings.t_transition.join()
