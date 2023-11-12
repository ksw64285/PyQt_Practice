from PyQt6.QtWidgets import QApplication, QDialog
import sys

app = QApplication(sys.argv) #QApplication 객체를 생성해야 app을 볼 수 있다

window = QDialog()

window.show()

sys.exit(app.exec())


# QDialog는 대화 상자 창의 기본 클래스이고 대화 상자 창은 최상위 창이다
# 항상 별도의 창에 표시되는 대화상자로, 주로 우리가 흔히 보는 팝업창이나 경고창 역할