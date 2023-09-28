from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv) #QApplication 객체를 생성해야 app을 볼 수 있다

window = QMainWindow()
window.statusBar().showMessage("KT MOS 남부") # 상태표시줄 입력
window.menuBar().addMenu("File") # 메뉴 추가

window.show()

sys.exit(app.exec())


# QMainWindow는 기본 응용프로그램 창을 제공
# QWidget과 비슷하지만 조금 다르다
# QMainWindow는 최상위 위젯으로, 메뉴바, 도구모음, 상태바 등이 포함된 미리 정의된 레이아울을 가진다