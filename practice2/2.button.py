from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget): # 클래스를 만들고 부모 클래스 QWidget을 상속받음
    def __init__(self): # 생성자 (클래스에서 객체가 생성될 때 호출되며, 이를 통해 클래스 초기화)
        super().__init__() # 부모(QWidget) 클래스의 속성 및 메소드를 불러와 해당 클래스에서도 사용 가능하도록 해줌

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("파이큐티 연습하기")
        self.setWindowIcon(QIcon("images/favicon.ico"))

        self.create_button()

    def create_button(self):
        btn = QPushButton("클릭!!!", self)
        btn.setGeometry(100, 100, 120, 120)
        btn.setFont(QFont('Times', 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon('images/favicon.ico'))
        btn.setIconSize(QSize(35, 35))

        # 버튼에 메뉴 넣기
        menu = QMenu()
        menu.setFont(QFont('Times', 14, QFont.Weight.ExtraBold))
        menu.addAction("복사")
        menu.addAction("잘라내기")
        menu.addAction("붙여넣기")
        btn.setMenu(menu)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())