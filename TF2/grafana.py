from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt6.QtWidgets import QTableWidgetItem, QPushButton
from details import DetailsWindow


class Ui_Form(object):
    def setupUi(self, Form):
        self.details_windows=[]
        Form.setObjectName("Form")
        Form.resize(1185, 855)
        Form.setStyleSheet("background-color:rgb(44, 50, 53);")
        self.label_icon = QtWidgets.QLabel(parent=Form)
        self.label_icon.setGeometry(QtCore.QRect(0, 0, 61, 61))
        self.label_icon.setStyleSheet("border-image:url(\"C:/Users/82105/Desktop/grafana_icon\")")
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")
        self.label_icon.mousePressEvent = self.clear_table # 아이콘 클릭 시 테이블 초기화
        # 삼성, 노키아, 에릭슨 버튼
        self.button_samsung = QPushButton('삼성', parent=Form)
        self.button_nokia = QPushButton('노키아', parent=Form)
        self.button_ericsson = QPushButton('에릭슨', parent=Form)
        # 버튼 배경색/글자색/위치 조정
        self.button_samsung.setStyleSheet("background-color: rgba(76, 175, 80, 0.5); color: white;")
        self.button_nokia.setStyleSheet("background-color: rgba(0, 140, 186, 0.5); color: white;")
        self.button_ericsson.setStyleSheet("background-color: rgba(244, 67, 54, 0.5); color: white;")
        self.button_samsung.setGeometry(QtCore.QRect(62, 0, 61, 61))
        self.button_nokia.setGeometry(QtCore.QRect(124, 0, 61, 61))
        self.button_ericsson.setGeometry(QtCore.QRect(186, 0, 61, 61))
        # 버튼 클릭 이벤트
        self.button_samsung.clicked.connect(self.show_samsung_table)
        self.button_nokia.clicked.connect(self.show_nokia_table)
        self.button_ericsson.clicked.connect(self.show_ericsson_table)

        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(50, 60, 1081, 731))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_du_id = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_du_id.setFont(font)
        self.label_du_id.setStyleSheet("color: rgb(52, 162, 230);\n"
                                       "background-color:rgb(32, 34, 38);")
        self.label_du_id.setObjectName("label_du_id")
        self.verticalLayout.addWidget(self.label_du_id)
        self.label_du_name = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_du_name.setFont(font)
        self.label_du_name.setStyleSheet("color: rgb(52, 162, 230);\n"
                                         "background-color:rgb(32, 34, 38);")
        self.label_du_name.setObjectName("label_du_name")
        self.verticalLayout.addWidget(self.label_du_name)
        self.label_ru_name = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ru_name.setFont(font)
        self.label_ru_name.setStyleSheet("color: rgb(52, 162, 230);\n"
                                         "background-color:rgb(32, 34, 38);")
        self.label_ru_name.setObjectName("label_ru_name")
        self.verticalLayout.addWidget(self.label_ru_name)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_du_id = QtWidgets.QLineEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_du_id.setFont(font)
        self.lineEdit_du_id.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color:rgb(32, 34, 38);")
        self.lineEdit_du_id.setObjectName("lineEdit_du_id")
        self.verticalLayout_2.addWidget(self.lineEdit_du_id)
        self.lineEdit_du_name = QtWidgets.QLineEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_du_name.setFont(font)
        self.lineEdit_du_name.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color:rgb(32, 34, 38);")
        self.lineEdit_du_name.setObjectName("lineEdit_du_name")
        self.verticalLayout_2.addWidget(self.lineEdit_du_name)
        self.lineEdit_ru_name = QtWidgets.QLineEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_ru_name.setFont(font)
        self.lineEdit_ru_name.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "background-color:rgb(32, 34, 38);")
        self.lineEdit_ru_name.setText("")
        self.lineEdit_ru_name.setObjectName("lineEdit_ru_name")
        self.verticalLayout_2.addWidget(self.lineEdit_ru_name)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color:rgb(32, 34, 38);")
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.verticalLayout_4.addWidget(self.tableWidget)

        # 테이블 초기화 코드
        self.tableWidget.setStyleSheet(
            "QTableWidget QHeaderView::section {"
            "background-color: rgb(32, 34, 38);"
            "color: rgb(52, 162, 230);"
            "}"
        )

        self.tableWidget.itemDoubleClicked.connect(self.show_details) # 더블클릭 이벤트 연결
        self.details_dialog = None
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers) # 아이템 편집 비활성화
        self.tableWidget.itemClicked.connect(self.highlight_row) # 클릭 시 하이라이트
        self.previous_row = None

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 텍스트 변경 이벤트 처리
        self.lineEdit_du_id.textChanged.connect(self.filter_data)
        self.lineEdit_du_name.textChanged.connect(self.filter_data)
        self.lineEdit_ru_name.textChanged.connect(self.filter_data)

        Form.setWindowTitle("승우의 Grafana")

    def show_details(self, item): # 더블클릭한 행의 데이터를 새 창에서 띄우기
        row = item.row()
        data = []

        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            data.append(item.text())

        table_name = self.get_current_table_name(data[1]) # 위치 정보를 통해 현재 테이블이 무엇인지 가져온다

        cursor = None
        mydb = None

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="apple"
            )

            cursor = mydb.cursor()
            cursor.execute(f"SELECT output, vswr, rssi FROM {table_name} WHERE idx = %s", (data[0],))
            result = cursor.fetchone()
            output_value, vswr_value, rssi_value = result
            data.extend([str(output_value), str(vswr_value), str(rssi_value)])

        except mc.Error as e:
            print(f'더블클릭 시 Error: {e}')

        finally:
            if cursor is not None:
                cursor.close()
            if mydb is not None:
                mydb.close()

        # 새로운 창 열어서 데이터 보여주기
        details_window = DetailsWindow(data)
        self.details_windows.append(details_window)
        details_window.showNormal()

    def get_current_table_name(self, location):
        if location == '충청' or location == '대전' or location == '부산' or location == '대구':
            return "samsung"
        elif location == '분당' or location == '판교':
            return "nokia"
        elif location == '제어망4팀' or location == 'TF':
            return "ericsson"
        else:
            return None

    def show_samsung_table(self):
        self.select_data("samsung")
        self.current_table = "samsung"

    def show_nokia_table(self):
        self.select_data("nokia")
        self.current_table = "nokia"

    def show_ericsson_table(self):
        self.select_data("ericsson")
        self.current_table = "ericsson"

    def clear_table(self, event):
        self.tableWidget.setRowCount(0)

    def select_data(self, table_name):
        cursor = None
        mydb = None
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="apple"
            )

            cursor = mydb.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            result = cursor.fetchall()

            # 테이블에 데이터 추가
            self.tableWidget.setRowCount(len(result))
            for i, row in enumerate(result):
                for j, col in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(col))
                    item.setForeground(QtGui.QColor(255, 255, 255))
                    self.tableWidget.setItem(i, j, item)

        except mc.Error as e:
            print(f'버튼 클릭 시 테이블 조회 Error: {e}')

        finally:
            if cursor is not None:
                cursor.close()
            if mydb is not None:
                mydb.close()

    def filter_data(self):
        filter_du_id = self.lineEdit_du_id.text()
        filter_du_name = self.lineEdit_du_name.text()
        filter_ru_name = self.lineEdit_ru_name.text()

        cursor = None
        mydb = None

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="apple"
            )

            cursor = mydb.cursor()
            # 입력된 값으로 필터링
            cursor.execute(f"SELECT * FROM {self.current_table} WHERE du_id LIKE %s AND du_name LIKE %s AND ru_name LIKE %s",
                           ('%' + filter_du_id + '%', '%' + filter_du_name + '%', '%' + filter_ru_name + '%'))
            result = cursor.fetchall()

            # 테이블 초기화
            self.tableWidget.setRowCount(0)

            # 필터링된 데이터를 테이블에 추가
            for i, row in enumerate(result):
                self.tableWidget.insertRow(i)
                for j, col in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(col))
                    item.setForeground(QtGui.QColor(255, 255, 255))
                    self.tableWidget.setItem(i, j, item)

        except mc.Error as e:
            print(f'필터 기능 Error: {e}')

        finally:
            if cursor is not None:
                cursor.close()
            if mydb is not None:
                mydb.close()

    def highlight_row(self, item): # 행 클릭 시 하이라이트 / 이전 행은 원상복구
        row = item.row()
        for column in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, column)
            item.setBackground(QtGui.QColor(255, 0, 0))

        if self.previous_row is not None and self.previous_row != row:
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(self.previous_row, column)
                if item is not None: # item이 None이 아닌 경우에만 배경색을 바꾸도록 수정
                    item.setBackground(QtGui.QColor(44, 50, 53))

        self.previous_row = row

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_du_id.setText(_translate("Form", "du_id"))
        self.label_du_name.setText(_translate("Form", "du_name"))
        self.label_ru_name.setText(_translate("Form", "ru_name"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "index"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "location"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "du_id"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "du_name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "ru_name"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "pci"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "cell_info"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())