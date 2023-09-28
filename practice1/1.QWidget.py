from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv) #QApplication 객체를 생성해야 app을 볼 수 있다

window = QWidget()

window.show()

sys.exit(app.exec())


# QWidget은 모든 사용자 인터페이스 객체의 기본 클래스이다
# 버튼, input 위젯 같은 다양한 위젯들을 올려놓을 수 있는 사각형 영역
# 즉, 그림을 그릴 수 있는 도화지
# QMainWindow와 다르게 상단의 메뉴차과 하단의 상태창을 추가할 수 없다