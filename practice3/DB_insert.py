# Form implementation generated from reading ui file 'DB_insert.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_username = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout.addWidget(self.lineEdit_username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_pw = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pw.setFont(font)
        self.lineEdit_pw.setObjectName("lineEdit_pw")
        self.horizontalLayout_2.addWidget(self.lineEdit_pw)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        # 연결하기
        self.pushButton.clicked.connect(self.login)
        self.verticalLayout.addWidget(self.pushButton)
        self.label_result = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def login(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="apple"
            )

            mycursor = mydb.cursor()

            username = self.lineEdit_username.text()
            password = self.lineEdit_pw.text()

            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            value = (username, password)

            mycursor.execute(query, value)

            mydb.commit()
            self.label_result.setText("데이터 추가 성공")

        except mc.Error as e:
            self.label_result.setText("데이터 추가 실패")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "이름:"))
        self.label_2.setText(_translate("Form", "암호:"))
        self.pushButton.setText(_translate("Form", "로그인"))
        self.label_result.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
