# settings.py
from PyQt5 import QtWidgets, uic
from threading import Semaphore

# Define constants
R  = 0
RY = 1
G  = 2
BG = 3
Y  = 4
C  = 5

app = QtWidgets.QApplication([])
dlg = uic.loadUi("raskrsnica.ui")

# UI variables
input_1_red_from = ""
input_1_red_to = ""
input_1_redyellow_from = ""
input_1_redyellow_to = ""
input_1_green_from = ""
input_1_green_to = ""
input_1_bgreen_from = ""
input_1_bgreen_to = ""
input_1_yellow_from = ""
input_1_yellow_to = ""
input_1_con_from = ""
input_1_con_to = ""
input_2_red_from = ""
input_2_red_to = ""
input_2_redyellow_from = ""
input_2_redyellow_to = ""
input_2_green_from = ""
input_2_green_to = ""
input_2_bgreen_from = ""
input_2_bgreen_to = ""
input_2_yellow_from = ""
input_2_yellow_to = ""
input_p1_green_from = ""
input_p1_green_to = ""
input_p2_green_from = ""
input_p2_green_to = ""
sem_1_prio = ""
sem_2_prio = ""

# Semaphores in graphic
sem_1_red = ""
sem_1_yellow = ""
sem_1_green = ""

sem_2_red = ""
sem_2_yellow = ""
sem_2_green = ""

sem_3_red = ""
sem_3_yellow = ""
sem_3_green = ""

sem_4_red = ""
sem_4_yellow = ""
sem_4_green = ""

semp_1_red = ""
semp_1_green = ""

semp_2_red = ""
semp_2_green = ""

semp_3_red = ""
semp_3_green = ""

semp_4_red = ""
semp_4_green = ""

semp_5_red = ""
semp_5_green = ""

semp_6_red = ""
semp_6_green = ""

semp_7_red = ""
semp_7_green = ""

semp_8_red = ""
semp_8_green = ""

# Thread & Serial variables
t_fasttimer = None
t_regulartimer = None
t_fasttimer_cond = True
t_regulartimer_cond = True
t_yellowblink = True
sem = Semaphore(value = 0)
yellowblink = Semaphore(value = 0)
transitionsem = Semaphore(value = 0)
mutex = Semaphore(value = 1)
devserial = "/dev/ttyACM0"

elements = 0
semlist1 = []
semlist2 = []
semplist3 = []
semplist4 = []
semlistcond = []

isChecked = False
isActive = False
checkFirst = False
checkSecond = False
isDisabled = False
isTransition = False
isPowerOff = True
yellowThread = False
regularThread = False
