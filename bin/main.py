import sys
from PyQt5 import  QtWidgets

from gui.UI import *

app = QtWidgets.QApplication(sys.argv)
zhish_auto_messenger = QtWidgets.QMainWindow()
ui = Ui_zhish_auto_messenger()
ui.setupUi(zhish_auto_messenger)
zhish_auto_messenger.show()
sys.exit(app.exec_())