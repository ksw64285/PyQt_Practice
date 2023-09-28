from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget): # 클래스를 만들고 부모 클래스 QWidget을 상속받음
    def __init__(self): # 생성자 (클래스에서 객체가 생성될 때 호출되며, 이를 통해 클래스 초기화)
        super().__init__() # 부모(QWidget) 클래스의 속성 및 메소드를 불러와 해당 클래스에서도 사용 가능하도록 해줌

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("파이큐티 연습하기")
        self.setWindowIcon(QIcon("images/favicon.ico"))

        self.setStyleSheet('background-color:yellow')
        self.setWindowOpacity(0.5)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())