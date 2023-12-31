# Form implementation generated from reading ui file 'DB_select.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt6.QtWidgets import QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 500)
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
        self.lineEdit_dbname = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_dbname.setFont(font)
        self.lineEdit_dbname.setObjectName("lineEdit_dbname")
        self.horizontalLayout.addWidget(self.lineEdit_dbname)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_tablename = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_tablename.setFont(font)
        self.lineEdit_tablename.setObjectName("lineEdit_tablename")
        self.horizontalLayout_2.addWidget(self.lineEdit_tablename)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        # 연결하기
        self.pushButton.clicked.connect(self.select_data)
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def select_data(self):
        dbname = self.lineEdit_dbname.text()
        tablename = self.lineEdit_tablename.text()
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database=dbname
            )

            mycursor = mydb.cursor() # 커서 객체 (커서는 SQL 쿼리를 실행하는 데 사용된다)
            mycursor.execute(f'SELECT * FROM {tablename}')

            result = mycursor.fetchall() # 쿼리의 결과를 가져온다 (리스트)

            self.tableWidget.setRowCount(0) # 위젯의 행의 개수를 0으로 설정하여 이전에 표시된 데이터를 지운다

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("에러 발생")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "DB 이름:"))
        self.label_2.setText(_translate("Form", "Table 이름:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "password"))
        self.pushButton.setText(_translate("Form", "데이터 보기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
