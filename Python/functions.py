# functions.py
import settings
import threads
from threading import Semaphore
from mspdebug import *
from serial import *

# Gets object of the specified input
# @param direction
#   "from"
#   "to"
def obj( semaphore, field, direction = "from" ):
    val = "input_" + str(semaphore)
    switcher = {
        0: "red",
        1: "redyellow",
        2: "green",
        3: "bgreen",
        4: "yellow",
        5: "con"
    }
    val += "_"
    val += switcher.get(field, "red")
    val += "_"
    val += str(direction)
    module = globals()['settings']
    return vars(module).get( val )

# Gets semaphore object for graphics
def paintobj( semaphore, field, passenger = False ):
    R  = settings.R
    Y  = settings.Y
    G  = settings.G
    if ( passenger == False ):
        val = "sem_"
    else :
        val = "semp_"
    val += str(semaphore)
    switcher = {
        R: "red",
        G: "green",
        Y: "yellow"
    }
    val += "_"
    val += switcher.get(field, "red")
    module = globals()['settings']
    return vars(module).get( val )

# Gets object of the specified input
# @param direction
#   "from"
#   "to"
def objp( semaphore, direction = "from" ):
    val = "input_p" + str(semaphore)
    switcher = {
        0: "red",
        1: "redyellow",
        2: "green",
        3: "bgreen",
        4: "yellow",
        5: "con"
    }
    val += "_green_"
    val += str(direction)
    module = globals()['settings']
    return vars(module).get( val )

# Get text value of the specified input for semaphore
# @param direction
#   "from"
#   "to"
def input( semaphore, field, direction = "from" ):
    return obj(semaphore, field, direction).text()

# Get text value of the specified input for passenger semaphore
# @param direction
#   "from"
#   "to"
def inputp( semaphore, direction = "from" ):
    semaphore = int(semaphore)
    semaphore -= 2
    o = objp( str(semaphore), direction )
    return o.text()

# Enable inputs
def enable_inputs(sem):
    if sem == 1:
        #input_1_red_from.setReadOnly(False)
        settings.input_1_red_to.setReadOnly(False)
        settings.input_1_redyellow_from.setReadOnly(False)
        settings.input_1_redyellow_to.setReadOnly(False)
        settings.input_1_green_from.setReadOnly(False)
        settings.input_1_green_to.setReadOnly(False)
        settings.input_1_bgreen_from.setReadOnly(False)
        settings.input_1_bgreen_to.setReadOnly(False)
        settings.input_1_yellow_from.setReadOnly(False)
        settings.input_1_yellow_to.setReadOnly(False)
        settings.input_1_con_from.setReadOnly(False)
        settings.input_1_con_to.setReadOnly(False)
    else :
        settings.input_2_red_from.setReadOnly(False)
        settings.input_2_red_to.setReadOnly(False)
        settings.input_2_redyellow_from.setReadOnly(False)
        settings.input_2_redyellow_to.setReadOnly(False)
        settings.input_2_green_from.setReadOnly(False)
        settings.input_2_green_to.setReadOnly(False)
        settings.input_2_bgreen_from.setReadOnly(False)
        settings.input_2_bgreen_to.setReadOnly(False)
        settings.input_2_yellow_from.setReadOnly(False)
        settings.input_2_yellow_to.setReadOnly(False)

# Disable inputs
def disable_inputs(sem):
    if sem == 1 :
        #input_1_red_from.setReadOnly(True)
        settings.input_1_red_to.setReadOnly(True)
        settings.input_1_redyellow_from.setReadOnly(True)
        settings.input_1_redyellow_to.setReadOnly(True)
        settings.input_1_bgreen_from.setReadOnly(True)
        settings.input_1_bgreen_to.setReadOnly(True)
        settings.input_1_green_from.setReadOnly(True)
        settings.input_1_green_to.setReadOnly(True)
        settings.input_1_yellow_from.setReadOnly(True)
        settings.input_1_yellow_to.setReadOnly(True)
        settings.input_1_con_from.setReadOnly(True)
        settings.input_1_con_to.setReadOnly(True)
    else :
        settings.input_2_red_from.setReadOnly(True)
        settings.input_2_red_to.setReadOnly(True)
        settings.input_2_redyellow_from.setReadOnly(True)
        settings.input_2_redyellow_to.setReadOnly(True)
        settings.input_2_green_from.setReadOnly(True)
        settings.input_2_green_to.setReadOnly(True)
        settings.input_2_bgreen_from.setReadOnly(True)
        settings.input_2_bgreen_to.setReadOnly(True)
        settings.input_2_yellow_from.setReadOnly(True)
        settings.input_2_yellow_to.setReadOnly(True)

# Set all variables inside application
def initiate_variables():
    dlg = settings.dlg
    global isClick

    settings.input_1_red_from = dlg.input_1_red_from
    settings.input_1_red_to = dlg.input_1_red_to

    settings.input_1_redyellow_from = dlg.input_1_redyellow_from
    settings.input_1_redyellow_to = dlg.input_1_redyellow_to

    settings.input_1_green_from = dlg.input_1_green_from
    settings.input_1_green_to = dlg.input_1_green_to

    settings.input_1_bgreen_from = dlg.input_1_bgreen_from
    settings.input_1_bgreen_to = dlg.input_1_bgreen_to

    settings.input_1_yellow_from = dlg.input_1_yellow_from
    settings.input_1_yellow_to = dlg.input_1_yellow_to

    settings.input_1_con_from = dlg.input_1_con_from
    settings.input_1_con_to = dlg.input_1_con_to

    settings.input_p1_green_from = dlg.input_p1_green_from
    settings.input_p1_green_to = dlg.input_p1_green_to

    settings.input_2_red_from = dlg.input_2_red_from
    settings.input_2_red_to = dlg.input_2_red_to

    settings.input_2_redyellow_from = dlg.input_2_redyellow_from
    settings.input_2_redyellow_to = dlg.input_2_redyellow_to

    settings.input_2_green_from = dlg.input_2_green_from
    settings.input_2_green_to = dlg.input_2_green_to

    settings.input_2_bgreen_from = dlg.input_2_bgreen_from
    settings.input_2_bgreen_to = dlg.input_2_bgreen_to

    settings.input_2_yellow_from = dlg.input_2_yellow_from
    settings.input_2_yellow_to = dlg.input_2_yellow_to

    settings.input_p2_green_from = dlg.input_p2_green_from
    settings.input_p2_green_to = dlg.input_p2_green_to

    settings.sem_1_prio = dlg.sem_1_prio
    settings.sem_2_prio = dlg.sem_2_prio

    settings.sem_1_red = dlg.sem_1_red
    settings.sem_1_yellow = dlg.sem_1_yellow
    settings.sem_1_green = dlg.sem_1_green

    settings.sem_2_red = dlg.sem_2_red
    settings.sem_2_yellow = dlg.sem_2_yellow
    settings.sem_2_green = dlg.sem_2_green

    settings.sem_3_red = dlg.sem_3_red
    settings.sem_3_yellow = dlg.sem_3_yellow
    settings.sem_3_green = dlg.sem_3_green

    settings.sem_4_red = dlg.sem_4_red
    settings.sem_4_yellow = dlg.sem_4_yellow
    settings.sem_4_green = dlg.sem_4_green

    settings.semp_1_red = dlg.semp_1_red
    settings.semp_1_green = dlg.semp_1_green

    settings.semp_2_red = dlg.semp_2_red
    settings.semp_2_green = dlg.semp_2_green

    settings.semp_3_red = dlg.semp_3_red
    settings.semp_3_green = dlg.semp_3_green

    settings.semp_4_red = dlg.semp_4_red
    settings.semp_4_green = dlg.semp_4_green

    settings.semp_5_red = dlg.semp_5_red
    settings.semp_5_green = dlg.semp_5_green

    settings.semp_6_red = dlg.semp_6_red
    settings.semp_6_green = dlg.semp_6_green

    settings.semp_7_red = dlg.semp_7_red
    settings.semp_7_green = dlg.semp_7_green

    settings.semp_8_red = dlg.semp_8_red
    settings.semp_8_green = dlg.semp_8_green

# Set active action handler for radio buttons
def set_prio():
    R  = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    BG = settings.BG
    C  = settings.C
    autofill_options()
    if(settings.sem_1_prio.isChecked()) :
        disable_inputs(2)
        enable_inputs(1)
    else:
        disable_inputs(1)
        enable_inputs(2)
    reset_action()



# Set value for specified input (semaphores)
def set( semaphore, field, value, direction = "from" ):
    o = obj( semaphore, field, direction )
    o.setText( str(value) )

# Set value for specified input (semaphores)
def setp( semaphore, value, direction = "from" ):
    semaphore = int(semaphore)
    semaphore -= 2
    o = objp( str(semaphore), direction )
    o.setText( str(value) )


# Check fields action handler
def setCheck():
    global isChecked

    isChecked   = False
    checkFirst  = check_first_input_group()
    checkSecond = check_second_input_group()

    if checkFirst == False and checkSecond == False :
        print("greska!!!")
        isChecked = False
    else :
        isChecked = True

# Checks first input group
def check_first_input_group():
    R  = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    BG = settings.BG
    C  = settings.C
    checkFirst = False

    if not (
        input(1, R).isdigit() and input(1, R, "to").isdigit() and
        input(1, RY).isdigit() and input(1, R, "to").isdigit() and
        input(1, G).isdigit() and input(1, G, "to").isdigit() and
        input(1, BG).isdigit() and input(1, BG, "to").isdigit() and
        input(1, Y).isdigit() and input(1, Y, "to").isdigit()
    ):
        print("Polja moraju biti celi pozitivni brojevi 1")
    else:
        if ( settings.sem_1_prio.isChecked() ):
            if (not (
                int(input(1, R)) < int(input(1, R, "to")) and
                (int(input(1, R, "to")) + 1 == int(input(1, RY))) and
                int(input(1, RY)) < int(input(1, RY, "to")) and
                (int(input(1, RY, "to")) + 1 == int(input(1, G))) and
                (int(input(1, G, "to")) + 1 == int(input(1, BG))) and
                int(input(1, BG)) < int(input(1, BG, "to")) and
                (int(input(1, BG, "to")) + 1 == int(input(1, Y))) and
                int(input(1, Y)) < int(input(1, Y, "to"))
                )) :
                print("Timeline error 1")
                return False
        else:
            if (not (
                int(input(1, R)) < int(input(1, R, "to")) and
                int(input(1, RY)) < int(input(1, RY, "to")) and
                (int(input(1, RY, "to")) + 1 == int(input(1, G))) and
                (int(input(1, G, "to")) + 1 == int(input(1, BG))) and
                int(input(1, BG)) < int(input(1, BG, "to")) and
                (int(input(1, BG, "to")) + 1 == int(input(1, Y))) and
                int(input(1, Y)) < int(input(1, Y, "to"))
                )) :
                print("Timeline error 1")
                return False

    return True

# Checks second input group
def check_second_input_group():
    R  = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    BG = settings.BG
    C  = settings.C
    checkSecond = False
    if not (
        input(2, R).isdigit() and input(2, R, "to").isdigit() and
        input(2, RY).isdigit() and input(2, R, "to").isdigit() and
        input(2, G).isdigit() and input(2, G, "to").isdigit() and
        input(2, BG).isdigit() and input(2, BG, "to").isdigit() and
        input(2, Y).isdigit() and input(2, Y, "to").isdigit()
    ):
        print("Polja moraju biti celi pozitivni brojevi 2")
    elif not (int(input(2, R)) < int(input(2, R, "to")) and
        (int(input(2, R, "to")) + 1 == int(input(2, RY))) and
        int(input(2, RY)) < int(input(2, RY, "to")) and
        (int(input(2, RY, "to")) + 1 == int(input(2, G))) and
        (int(input(2, G, "to")) + 1 == int(input(2, BG))) and
        int(input(2, BG)) < int(input(2, BG, "to")) and
        (int(input(2, BG, "to")) + 1 == int(input(2, Y))) and
        int(input(2, Y)) < int(input(2, Y, "to"))) :
        print("Timeline error 2")
    else:
        print("sve proslo 2")
        checkSecond = True
    return checkSecond

# Autofill options button event listener
def autofill_options():
    R  = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    BG = settings.BG
    C  = settings.C
    if ( settings.sem_1_prio.isChecked() ):
        # Fill fields for semaphore 2
        if ( check_first_input_group() ):
            enable_inputs(2)
            blockfrom = int(input(1, RY))
            blockto   = int(input(1, Y, "to"))

            # Other semaphore values
            yellowto   = blockfrom - 1
            yellowfrom = yellowto - 2
            bgreento   = yellowfrom - 1
            bgreenfrom = bgreento - 2
            greento    = bgreenfrom - 1

            set(2, RY, 0)
            set(2, RY, 2, "to")
            set(2, G, 3)
            set(2, R, blockfrom)
            set(2, R, blockto, "to")
            set(2, Y, blockfrom-1, "to")
            set(2, Y, blockfrom-3)
            set(2, BG, bgreenfrom)
            set(2, BG, bgreento, "to")
            set(2, G, greento, "to")
            # Passengers
            setp(3, int(input(1, R)) + 2)
            setp(3, int(input(1, R, "to")) - 2, "to")
            setp(4, int(input(2, R)) + 2)
            setp(4, int(input(2, R, "to")) - 2, "to")
    elif ( settings.sem_2_prio.isChecked() ):
        # Fill fields for semaphore 1
        if ( check_second_input_group() ):
            enable_inputs(1)
            blockfrom = int(input(2, RY))
            blockto   = int(input(2, Y, "to"))

            # Other semaphore values
            yellowto   = blockfrom - 1
            yellowfrom = yellowto - 2
            bgreento   = yellowfrom - 1
            bgreenfrom = bgreento - 2
            greento    = bgreenfrom - 1

            set(1, RY, 0)
            set(1, RY, 2, "to")
            set(1, G, 3)
            set(1, R, blockfrom)
            set(1, R, blockto, "to")
            set(1, Y, blockfrom-1, "to")
            set(1, Y, blockfrom-3)
            set(1, BG, bgreenfrom)
            set(1, BG, bgreento, "to")
            set(1, G, greento, "to")

            # Passengers
            setp(3, int(input(2, R)) + 2)
            setp(3, int(input(2, R, "to")) - 2, "to")
            setp(4, int(input(1, R)) + 2)
            setp(4, int(input(1, R, "to")) - 2, "to")

# Retrieves number of elements for transmission
def get_array_elements_number():
    R  = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    BG = settings.BG
    C  = settings.C
    if ( settings.sem_1_prio.isChecked() ) :
        return int(input(1, Y, "to"))
    else :
        return int(input(2, Y, "to"))

# Submit action function
def submit_action():
    global mutex
    if ( is_power_off() ):
        settings.mutex.acquire()
        settings.isPowerOff = True
        settings.regularThread = False
        settings.yellowThread = False
        settings.mutex.release()

        # Send data
        settings.mutex.acquire()
        send_to_msp(0,0)
        settings.mutex.release()
        return
    elif ( is_disabled() ):
        settings.mutex.acquire()
        settings.isDisabled = True
        settings.yellowThread = True
        settings.regularThread = False
        settings.yellowblink.release()
        settings.mutex.release()

    elif ( check_first_input_group() ):
        settings.mutex.acquire()
        settings.isDisabled = False
        settings.isPowerOff = False
        settings.yellowThread = False
        settings.regularThread = False
        settings.isTransition = True
        settings.transitionsem.release()
        settings.mutex.release()
        prepare_arrays()

def is_power_off():
    return settings.dlg.check_power.isChecked()

def is_disabled():
    return settings.dlg.check_disable.isChecked()

# Prepare arrays
def prepare_arrays():
    R  = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    BG = settings.BG
    C  = settings.C
    settings.elements    = get_array_elements_number() + 1
    settings.semlist1    = [None] * settings.elements
    settings.semlist2    = [None] * settings.elements
    settings.semplist3   = [R] * settings.elements
    settings.semplist4   = [R] * settings.elements
    settings.semlistcond = [R] * settings.elements

    # Handle first semaphore
    redfrom   = int(input(1, R))
    redto     = int(input(1, R, "to"))
    ryto      = int(input(1, RY, "to"))
    greento   = int(input(1, G, "to"))
    bgto      = int(input(1, BG, "to"))
    yellowto  = int(input(1, Y, "to"))
    p1_greenf = int(inputp(3))
    p1_greent = int(inputp(3, "to"))
    p2_greenf = int(inputp(4))
    p2_greent = int(inputp(4, "to"))

    i = redfrom
    while(i<=redto):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist1[j] = R
        i += 1
    while(i<=ryto):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist1[j] = RY
        i += 1
    while(i<=greento):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist1[j] = G
        i += 1
    while(i<=bgto):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist1[j] = BG
        i += 1
    while(i<=yellowto):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist1[i] = Y
        i += 1

    # Passenger semaphore
    i = 0
    while( i < settings.elements ):
        if ( i>=p1_greenf and i<=p1_greent ):
            settings.semplist3[i] = G
            if ( i>=p1_greent-2 ):
                settings.semplist3[i] = BG
        if ( i>=p2_greenf and i<=p2_greent ):
            settings.semplist4[i] = G
            if ( i>=p2_greent-2 ):
                settings.semplist4[i] = BG
        # if ( i>=condfrom and i<=condto ) :
        #     settings.semlistcond[i] = G
        i += 1

    # Handle second semaphore
    redto    = int(input(2, R, "to"))
    ryto     = int(input(2, RY, "to"))
    greento  = int(input(2, G, "to"))
    bgto     = int(input(2, BG, "to"))
    yellowto = int(input(2, Y, "to"))
    redfrom    = int(input(2, R))
    ryfrom     = int(input(2, RY))
    greenfrom  = int(input(2, G))
    bgfrom    = int(input(2, BG))
    yellowfrom = int(input(2, Y))
    i = ryfrom
    while(i<=ryto):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist2[j] = RY
        i += 1
    i = greenfrom
    while(i<=greento):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist2[j] = G
        i += 1
    i = bgfrom
    while(i<=bgto):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist2[j] = BG
        i += 1
    i = yellowfrom
    while(i<=yellowto):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist2[j] = Y
        i += 1
    i = redfrom
    while(i<=redto):
        j = i
        if i >= len(settings.semlist2):
            j = i %  len(settings.semlist2)
        elif i < 0:
            j = len(settings.semlist2) + i
        settings.semlist2[j] = R
        i += 1

    print(settings.semlist1)
    print(settings.semlist2)
    print(settings.semplist3)
    print(settings.semplist4)
    print(settings.semlistcond)


def apply_tab_order():
    dlg = settings.dlg
    # Set tab order for first semaphore inputs
    dlg.setTabOrder(dlg.input_1_red_from, dlg.input_1_red_to)
    dlg.setTabOrder(dlg.input_1_red_to, dlg.input_1_redyellow_from)
    dlg.setTabOrder(dlg.input_1_redyellow_from, dlg.input_1_redyellow_to)
    dlg.setTabOrder(dlg.input_1_redyellow_to, dlg.input_1_green_from)
    dlg.setTabOrder(dlg.input_1_green_from, dlg.input_1_green_to)
    dlg.setTabOrder(dlg.input_1_green_to, dlg.input_1_bgreen_from)
    dlg.setTabOrder(dlg.input_1_bgreen_from, dlg.input_1_bgreen_to)
    dlg.setTabOrder(dlg.input_1_bgreen_to, dlg.input_1_yellow_from)
    dlg.setTabOrder(dlg.input_1_yellow_from, dlg.input_1_yellow_to)
    dlg.setTabOrder(dlg.input_1_yellow_to, dlg.input_2_red_from)
    # Tab order for second semaphore inputs
    dlg.setTabOrder(dlg.input_2_red_from, dlg.input_2_red_to)
    dlg.setTabOrder(dlg.input_2_red_to, dlg.input_2_redyellow_from)
    dlg.setTabOrder(dlg.input_2_redyellow_from, dlg.input_2_redyellow_to)
    dlg.setTabOrder(dlg.input_2_redyellow_to, dlg.input_2_green_from)
    dlg.setTabOrder(dlg.input_2_green_from, dlg.input_2_green_to)
    dlg.setTabOrder(dlg.input_2_green_to, dlg.input_2_bgreen_from)
    dlg.setTabOrder(dlg.input_2_bgreen_from, dlg.input_2_bgreen_to)
    dlg.setTabOrder(dlg.input_2_bgreen_to, dlg.input_2_yellow_from)
    dlg.setTabOrder(dlg.input_2_yellow_from, dlg.input_2_yellow_to)

# Clears all data from fields
def reset_action():
    R = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    BG = settings.BG
    C  = settings.C
    fields = [R, G, Y, BG, Y, RY, C]
    for x in fields:
        set(1, x, "")
        set(1, x, "", "to")
        if ( x == C ):
            continue
        set(2, x, "")
        set(2, x, "", "to")
    toggle_start()

# Toggle start of the input section
def toggle_start():
    R = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    BG = settings.BG
    C  = settings.C
    if ( settings.dlg.sem_1_prio.isChecked() ):
        obj(1, R, "to").setFocus()
        set(1, R, 0)
        obj(1, R).setReadOnly(True)
    else :
        obj(2, R, "to").setFocus()
        set(2, R, 0)
        obj(2, R).setReadOnly(True)

# Close action
def close_action():
    turnoff_semaphores()
    threads.finish_threads()
    settings.dlg.close()
