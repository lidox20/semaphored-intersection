# app.py
from PyQt5 import QtWidgets, uic
from settings import *
from functions import *
from threads import *
from mspdebug import *
from painting import *

dlg.button_submit.clicked.connect(submit_action)
dlg.button_autofill.clicked.connect(autofill_options)
dlg.sem_1_prio.toggled.connect(set_prio)
dlg.button_close.clicked.connect(close_action)

# Do the work!

initiate_variables()

apply_tab_order()

send_to_msp(0,0)

disable_inputs(2)

toggle_start()

start_threads()

# Execute application
dlg.show()
app.exec()

finish_threads()
send_to_msp(0,0)
