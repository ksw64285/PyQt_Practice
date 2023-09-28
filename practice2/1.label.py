from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie

class Window(QWidget): # 클래스를 만들고 부모 클래스 QWidget을 상속받음
    def __init__(self): # 생성자 (클래스에서 객체가 생성될 때 호출되며, 이를 통해 클래스 초기화)
        super().__init__() # 부모(QWidget) 클래스의 속성 및 메소드를 불러와 해당 클래스에서도 사용 가능하도록 해줌

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("파이큐티 연습하기")
        self.setWindowIcon(QIcon("images/favicon.ico"))

        ''' 텍스트 연습
        label = QLabel("텍스트 연습하기", self)
        label.setText("텍스트 연습하기2")
        label.move(100, 100)
        label.setFont(QFont("Sanserif", 15))
        label.setStyleSheet('color:blue')

        label.setNum(9999)
        label.clear()
        '''


        ''' 라벨에 이미지 넣기
        label = QLabel(self)
        pixmap = QPixmap('images/favicon.ico')
        label.setPixmap(pixmap)
        '''

        # 애니메이션 넣기
        label = QLabel(self)
        movie = QMovie('images/dog.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())