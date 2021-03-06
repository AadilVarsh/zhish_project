# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json, os, pathlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)

from zhish_project.datahandler import datahndlr


CRITERIA = None


class Prompt(QDialog):
    def __init__(self, title, error_text, type, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle(title)

        if type == 1:
            Qbtn = QDialogButtonBox.Yes | QDialogButtonBox.No

            self.buttonBox = QDialogButtonBox(Qbtn)
            self.buttonBox.accepted.connect(self.accept)
            self.buttonBox.rejected.connect(self.reject)
        elif type == 2:
            Qbtn = QDialogButtonBox.Ok
            self.buttonBox = QDialogButtonBox(Qbtn)
            self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        message = QLabel(error_text)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class Ui_zhish_auto_messenger(object):
    def setupUi(self, zhish_auto_messenger):
        zhish_auto_messenger.setObjectName("zhish_auto_messenger")
        zhish_auto_messenger.resize(675, 603)
        self.centralwidget = QtWidgets.QWidget(zhish_auto_messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.message_input = QtWidgets.QTextEdit(self.centralwidget)
        self.message_input.setGeometry(QtCore.QRect(10, 10, 431, 551))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.message_input.setFont(font)
        self.message_input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.message_input.setObjectName("message_input")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(460, 160, 201, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.msg_spread_category_general = QtWidgets.QRadioButton(self.widget)
        self.msg_spread_category_general.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_spread_category_general.setAutoFillBackground(False)
        self.msg_spread_category_general.setObjectName("msg_spread_category_general")
        self.verticalLayout.addWidget(self.msg_spread_category_general)
        self.msg_spread_category_monthly = QtWidgets.QRadioButton(self.widget)
        self.msg_spread_category_monthly.setObjectName("msg_spread_category_monthly")
        self.verticalLayout.addWidget(self.msg_spread_category_monthly)
        self.msg_spread_category_custom = QtWidgets.QRadioButton(self.widget)
        self.msg_spread_category_custom.setObjectName("msg_spread_category_custom")
        self.verticalLayout.addWidget(self.msg_spread_category_custom)
        zhish_auto_messenger.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(zhish_auto_messenger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExecute = QtWidgets.QMenu(self.menubar)
        self.menuExecute.setObjectName("menuExecute")
        self.menuContact = QtWidgets.QMenu(self.menubar)
        self.menuContact.setObjectName("menuContact")
        self.menuAttachments = QtWidgets.QMenu(self.menubar)
        self.menuAttachments.setObjectName("menuAttachments")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        zhish_auto_messenger.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(zhish_auto_messenger)
        self.statusbar.setObjectName("statusbar")
        zhish_auto_messenger.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(zhish_auto_messenger)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(zhish_auto_messenger)
        self.actionExit.setObjectName("actionExit")
        self.actionQuick_Run = QtWidgets.QAction(zhish_auto_messenger)
        self.actionQuick_Run.setObjectName("actionQuick_Run")
        self.actionRun = QtWidgets.QAction(zhish_auto_messenger)
        self.actionRun.setObjectName("actionRun")
        self.actionAuthor = QtWidgets.QAction(zhish_auto_messenger)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionOpen = QtWidgets.QAction(zhish_auto_messenger)
        self.actionOpen.setObjectName("actionOpen")
        self.actionHow_to_add_variables = QtWidgets.QAction(zhish_auto_messenger)
        self.actionHow_to_add_variables.setObjectName("actionHow_to_add_variables")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menuExecute.addAction(self.actionQuick_Run)
        self.menuExecute.addAction(self.actionRun)
        self.menuContact.addAction(self.actionAuthor)
        self.menuAttachments.addAction(self.actionOpen)
        self.menuHelp.addAction(self.actionHow_to_add_variables)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuExecute.menuAction())
        self.menubar.addAction(self.menuContact.menuAction())
        self.menubar.addAction(self.menuAttachments.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(zhish_auto_messenger)
        QtCore.QMetaObject.connectSlotsByName(zhish_auto_messenger)

    def retranslateUi(self, zhish_auto_messenger):
        _translate = QtCore.QCoreApplication.translate
        zhish_auto_messenger.setWindowTitle(_translate("zhish_auto_messenger", "ZHISH UTIL"))
        self.msg_spread_category_general.setText(_translate("zhish_auto_messenger", "GENERAL"))
        self.msg_spread_category_monthly.setText(_translate("zhish_auto_messenger", "MONTHLY"))
        self.msg_spread_category_custom.setText(_translate("zhish_auto_messenger", "CUSTOM"))
        self.menuFile.setTitle(_translate("zhish_auto_messenger", "File"))
        self.menuExecute.setTitle(_translate("zhish_auto_messenger", "Execute"))
        self.menuContact.setTitle(_translate("zhish_auto_messenger", "Contact"))
        self.menuAttachments.setTitle(_translate("zhish_auto_messenger", "Attachments"))
        self.menuHelp.setTitle(_translate("zhish_auto_messenger", "Help"))
        self.actionAbout.setText(_translate("zhish_auto_messenger", "About"))
        self.actionExit.setText(_translate("zhish_auto_messenger", "Exit"))
        self.actionExit.setShortcut(_translate("zhish_auto_messenger", "Ctrl+Q"))
        self.actionQuick_Run.setText(_translate("zhish_auto_messenger", "Quick-Run"))
        self.actionQuick_Run.setShortcut(_translate("zhish_auto_messenger", "F5"))
        self.actionRun.setText(_translate("zhish_auto_messenger", "Run"))
        self.actionRun.setShortcut(_translate("zhish_auto_messenger", "Ctrl+F5"))
        self.actionAuthor.setText(_translate("zhish_auto_messenger", "Author"))
        self.actionOpen.setText(_translate("zhish_auto_messenger", "Open"))
        self.actionOpen.setShortcut(_translate("zhish_auto_messenger", "Ctrl+O"))
        self.actionHow_to_add_variables.setText(_translate("zhish_auto_messenger", "How to add variables?"))

        self.actionExit.triggered.connect(lambda: self.exit(zhish_auto_messenger))
        self.msg_spread_category_general.toggled.connect(lambda: self.category_selected(1))
        self.msg_spread_category_custom.toggled.connect(lambda: self.category_selected(2))
        self.msg_spread_category_monthly.toggled.connect(lambda: self.category_selected(3))

        self.actionQuick_Run.triggered.connect(lambda: self.quick_run())
        self.actionRun.triggered.connect(lambda: self.run())

    def exit(self, main_widget):
        main_widget.close()

    def category_selected(self, category):
        global CRITERIA
        if category == 1:
            CRITERIA = "general"
        elif category == 2:
            CRITERIA = "custom"
        elif category == 3:
            CRITERIA = "monthly"
        else:
            CRITERIA = "general"

    def quick_run(self):

        message = self.message_input.toPlainText()
        self.criteria = CRITERIA
        
        datahndlr.update_data(message = message, criteria = CRITERIA)

        self.message_input.clear()


    def run(self):
        prmpt = Prompt('COnfirm Prompt', 'Confirm?', 1)
        if prmpt.exec_():
            if CRITERIA is not None:
                message = self.message_input.toPlainText()
                self.criteria = CRITERIA
                datahndlr.update_data(message = message , criteria = CRITERIA)
                # print(message, CRITERIA)
                self.message_input.clear()
            else:
                prmpt = Prompt('invalid input', 'Criteria is None', 2)
                prmpt.exec_()

        else:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    zhish_auto_messenger = QtWidgets.QMainWindow()
    ui = Ui_zhish_auto_messenger()
    ui.setupUi(zhish_auto_messenger)
    zhish_auto_messenger.show()
    sys.exit(app.exec_())
