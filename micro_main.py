# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!
import requests
import urllib.request, json

from PyQt5 import QtCore, QtGui, QtWidgets
from stud import Ui_MainWindow_Stud
from Teacher import Ui_MainWindow_Teacher
import stud
import Teacher
user=""
userid=""
class Ui_MainWindow(object):
    def open_student(self):
        self.MainWindow_Stud = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Stud()
        self.ui.setupUi(self.MainWindow_Stud)
        self.MainWindow_Stud.show()
    def open_teacher(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_Teacher()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 523)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.181818 rgba(225, 126, 255, 255), stop:1 rgba(147, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Main_layout = QtWidgets.QTabWidget(self.centralwidget)
        self.Main_layout.setObjectName("Main_layout")
        self.Tab_Student = QtWidgets.QWidget()
        self.Tab_Student.setObjectName("Tab_Student")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Tab_Student)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Tab_Stud = QtWidgets.QTabWidget(self.Tab_Student)
        self.Tab_Stud.setObjectName("Tab_Stud")
        self.Tab_Stud_Login = QtWidgets.QWidget()
        self.Tab_Stud_Login.setObjectName("Tab_Stud_Login")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.Tab_Stud_Login)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line_6 = QtWidgets.QFrame(self.Tab_Stud_Login)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_6.addWidget(self.line_6)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.Tab_Stud_Login)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_14.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.Tab_Stud_Login)
        self.lineEdit_5.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_14.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.Tab_Stud_Login)
        self.lineEdit_6.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_14.addWidget(self.lineEdit_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Button_Stud_Login = QtWidgets.QPushButton(self.Tab_Stud_Login)
        self.Button_Stud_Login.setStyleSheet("background-color:white;")
        self.Button_Stud_Login.setObjectName("Button_Stud_Login")
        self.horizontalLayout_6.addWidget(self.Button_Stud_Login)
        self.verticalLayout_14.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem3)
        self.label_8 = QtWidgets.QLabel(self.Tab_Stud_Login)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_14.addWidget(self.label_8)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem4)
        self.line_5 = QtWidgets.QFrame(self.Tab_Stud_Login)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_14.addWidget(self.line_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_14)
        self.verticalLayout_10.addLayout(self.verticalLayout_6)
        self.Tab_Stud.addTab(self.Tab_Stud_Login, "")
        self.Tab_Stud_Register = QtWidgets.QWidget()
        self.Tab_Stud_Register.setObjectName("Tab_Stud_Register")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Tab_Stud_Register)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.line = QtWidgets.QFrame(self.Tab_Stud_Register)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.Tab_Stud_Register)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_13.addWidget(self.label)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem6)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.Tab_Stud_Register)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_13.addWidget(self.lineEdit_9)
        self.lineEdit = QtWidgets.QLineEdit(self.Tab_Stud_Register)
        self.lineEdit.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_13.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Tab_Stud_Register)
        self.lineEdit_2.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_13.addWidget(self.lineEdit_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Button_Stud_Register = QtWidgets.QPushButton(self.Tab_Stud_Register)
        self.Button_Stud_Register.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255)\n"
"\n"
"}")
        self.Button_Stud_Register.setAutoDefault(True)
        self.Button_Stud_Register.setDefault(True)
        self.Button_Stud_Register.setFlat(False)
        self.Button_Stud_Register.setObjectName("Button_Stud_Register")
        self.horizontalLayout_2.addWidget(self.Button_Stud_Register)
        self.verticalLayout_13.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem8)
        self.label_7 = QtWidgets.QLabel(self.Tab_Stud_Register)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem9)
        self.line_2 = QtWidgets.QFrame(self.Tab_Stud_Register)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_13.addWidget(self.line_2)
        self.verticalLayout_11.addLayout(self.verticalLayout_13)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.Tab_Stud.addTab(self.Tab_Stud_Register, "")
        self.verticalLayout_2.addWidget(self.Tab_Stud)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.Main_layout.addTab(self.Tab_Student, "")
        self.Tab_Teacher = QtWidgets.QWidget()
        self.Tab_Teacher.setObjectName("Tab_Teacher")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Tab_Teacher)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Tab_Teacher_2 = QtWidgets.QTabWidget(self.Tab_Teacher)
        self.Tab_Teacher_2.setTabBarAutoHide(False)
        self.Tab_Teacher_2.setObjectName("Tab_Teacher_2")
        self.Tab_Teacher_Login = QtWidgets.QWidget()
        self.Tab_Teacher_Login.setObjectName("Tab_Teacher_Login")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Tab_Teacher_Login)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line_4 = QtWidgets.QFrame(self.Tab_Teacher_Login)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_7.addWidget(self.line_4)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem10)
        self.label_2 = QtWidgets.QLabel(self.Tab_Teacher_Login)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem11)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Tab_Teacher_Login)
        self.lineEdit_3.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_9.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.Tab_Teacher_Login)
        self.lineEdit_4.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_9.addWidget(self.lineEdit_4)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem12)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Button_Teacher_Login = QtWidgets.QPushButton(self.Tab_Teacher_Login)
        self.Button_Teacher_Login.setStyleSheet("background-color:white;")
        self.Button_Teacher_Login.setObjectName("Button_Teacher_Login")
        self.horizontalLayout_5.addWidget(self.Button_Teacher_Login)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem13)
        self.label_6 = QtWidgets.QLabel(self.Tab_Teacher_Login)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem14)
        self.line_3 = QtWidgets.QFrame(self.Tab_Teacher_Login)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_9.addWidget(self.line_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.Tab_Teacher_2.addTab(self.Tab_Teacher_Login, "")
        self.Tab_Teacher_Register = QtWidgets.QWidget()
        self.Tab_Teacher_Register.setObjectName("Tab_Teacher_Register")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Tab_Teacher_Register)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_8 = QtWidgets.QFrame(self.Tab_Teacher_Register)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_8.addWidget(self.line_8)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem15)
        self.label_4 = QtWidgets.QLabel(self.Tab_Teacher_Register)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_15.addWidget(self.label_4)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem16)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.Tab_Teacher_Register)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_15.addWidget(self.lineEdit_10)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.Tab_Teacher_Register)
        self.lineEdit_7.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_15.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.Tab_Teacher_Register)
        self.lineEdit_8.setStyleSheet("background-color:white;\n"
"color:rgb(128, 128, 128)")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_15.addWidget(self.lineEdit_8)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem17)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Button_Teacher_Register = QtWidgets.QPushButton(self.Tab_Teacher_Register)
        self.Button_Teacher_Register.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 255, 255)\n"
"\n"
"}")
        self.Button_Teacher_Register.setAutoDefault(True)
        self.Button_Teacher_Register.setDefault(True)
        self.Button_Teacher_Register.setFlat(False)
        self.Button_Teacher_Register.setObjectName("Button_Teacher_Register")
        self.horizontalLayout_7.addWidget(self.Button_Teacher_Register)
        self.verticalLayout_15.addLayout(self.horizontalLayout_7)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem18)
        self.label_5 = QtWidgets.QLabel(self.Tab_Teacher_Register)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_15.addWidget(self.label_5)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem19)
        self.line_7 = QtWidgets.QFrame(self.Tab_Teacher_Register)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_15.addWidget(self.line_7)
        self.verticalLayout_8.addLayout(self.verticalLayout_15)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.Tab_Teacher_2.addTab(self.Tab_Teacher_Register, "")
        self.verticalLayout_4.addWidget(self.Tab_Teacher_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.Main_layout.addTab(self.Tab_Teacher, "")
        self.verticalLayout.addWidget(self.Main_layout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 369, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Main_layout.setCurrentIndex(1)
        self.Tab_Stud.setCurrentIndex(0)
        self.Tab_Teacher_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "APP NAME"))
        self.lineEdit_5.setText(_translate("MainWindow", "USERID"))
        self.lineEdit_6.setText(_translate("MainWindow", "PASSWORD"))
        self.Button_Stud_Login.setText(_translate("MainWindow", "LOGIN"))
        self.Button_Stud_Login.clicked.connect(self.stud_login)  # Function Name
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.Tab_Stud.setTabText(self.Tab_Stud.indexOf(self.Tab_Stud_Login), _translate("MainWindow", "STUDENT LOGIN"))
        self.label.setText(_translate("MainWindow", "APP NAME"))
        self.lineEdit_9.setText(_translate("MainWindow", "USERID"))
        self.lineEdit.setText(_translate("MainWindow", "USERNAME"))
        self.lineEdit_2.setText(_translate("MainWindow", "PASSWORD"))
        self.Button_Stud_Register.setText(_translate("MainWindow", "REGISTER"))
        self.Button_Stud_Register.clicked.connect(self.stud_reg)                    # Function Name
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.Tab_Stud.setTabText(self.Tab_Stud.indexOf(self.Tab_Stud_Register), _translate("MainWindow", "STUDENT REGISTER"))
        self.Main_layout.setTabText(self.Main_layout.indexOf(self.Tab_Student), _translate("MainWindow", "STUDENT"))
        self.label_2.setText(_translate("MainWindow", "APP NAME"))
        self.lineEdit_3.setText(_translate("MainWindow", "USERID"))
        self.lineEdit_4.setText(_translate("MainWindow", "PASSWORD"))
        self.Button_Teacher_Login.setText(_translate("MainWindow", "LOGIN"))
        self.Button_Teacher_Login.clicked.connect(self.teach_login)
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.Tab_Teacher_2.setTabText(self.Tab_Teacher_2.indexOf(self.Tab_Teacher_Login), _translate("MainWindow", "TEACHER LOGIN"))
        self.label_4.setText(_translate("MainWindow", "APP NAME"))
        self.lineEdit_10.setText(_translate("MainWindow", "USERID"))
        self.lineEdit_7.setText(_translate("MainWindow", "USERNAME"))
        self.lineEdit_8.setText(_translate("MainWindow", "PASSWORD"))
        self.Button_Teacher_Register.setText(_translate("MainWindow", "REGISTER"))
        self.Button_Teacher_Register.clicked.connect(self.teach_reg)
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.Tab_Teacher_2.setTabText(self.Tab_Teacher_2.indexOf(self.Tab_Teacher_Register), _translate("MainWindow", "TEACHER REGISTER"))
        self.Main_layout.setTabText(self.Main_layout.indexOf(self.Tab_Teacher), _translate("MainWindow", "TEACHER"))
    def stud_reg(self):
        user = self.lineEdit.text()
        userid = self.lineEdit_9.text()
        password = self.lineEdit_2.text()
        d = {}
        with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/StudentRegister.php") as url:
            data = json.loads(url.read().decode())
            already_registered=True
            for x in data['Details']:
                if (userid == x['UserID']):
                    self.label_7.setText("UserId already Registered")
                    user_in = False
                    already_registered = True
                    break
                else:
                    already_registered = False
            if (already_registered == False):
                self.label_7.setText("Successfully Registered")
                user_in = True
                values = {'UserID': userid, 'password': password, 'UserName': user, 'ask': ''}
                requests.post("https://melvinmathew0102.000webhostapp.com/Student_ask.php", values)
    def stud_login(self):
        try:
            user = ""
            userid = self.lineEdit_5.text()
            password = self.lineEdit_6.text()
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/StudentRegister.php") as url:
                data = json.loads(url.read().decode())
                already_registered=True
                for x in data['Details']:
                    if (userid == x['UserID'] and password == x['Password']):
                        user = x['UserName']
                        self.label_8.setText("Successfully Loged IN")
                        user_in = True
                        already_registered = True
                        self.open_student()
                        stud.userid = userid
                        break
                    else:
                        already_registered = False
                if (already_registered == False):
                    self.label_8.setText("Login UnSuccessfull")
                    user_in = False
        except:
            self.label_8.setText("Network Error")
    def teach_reg(self):
        user = self.lineEdit_7.text()
        userid =self.lineEdit_10.text()
        password =self.lineEdit_8.text()
        d = {}
        with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/TeacherRegister.php") as url:
            data = json.loads(url.read().decode())
            already_registered=True
            for x in data['Details']:
                if (userid == x['T_ID']):
                    self.label_5.setText("T_Id already Registered")
                    user_in = False
                    already_registered = True
                    break
                else:
                    already_registered = False
            if (already_registered == False):
                self.label_5.setText("Successfully Registered")
                user_in = True
                values = {'UserID': userid, 'password': password, 'UserName': user}
                requests.post("https://melvinmathew0102.000webhostapp.com/teacher.php", values)
    def teach_login(self):
        try:
            user_id = self.lineEdit_3.text()
            password =self.lineEdit_4.text()
            with urllib.request.urlopen("https://melvinmathew0102.000webhostapp.com/TeacherRegister.php") as url:
                data = json.loads(url.read().decode())
                already_registered=True
                for x in data['Details']:
                    if (user_id == x['T_ID'] and password == x['T_Password']):
                        user = x['T_Name']
                        self.label_6.setText("Successfully Loged IN")
                        already_registered = True
                        self.open_teacher()
                        Teacher.userid=user_id
                        break
                    else:
                        already_registered = False
                if (already_registered == False):
                    self.label_6.setText("Login UnSuccessfull")
        except:
            self.label_6.setText("Network Error")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

