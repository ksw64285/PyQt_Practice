from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QSize, QUrl
import sys

class Window(QMainWindow): # 클래스를 만들고 부모 클래스 QWidget을 상속받음
    def __init__(self): # 생성자 (클래스에서 객체가 생성될 때 호출되며, 이를 통해 클래스 초기화)
        super().__init__() # 부모(QWidget) 클래스의 속성 및 메소드를 불러와 해당 클래스에서도 사용 가능하도록 해줌

        self.setGeometry(200, 200, 1200, 600)
        self.setWindowTitle("조항민 대리님 짱")
        self.setWindowIcon(QIcon("images/favicon.ico"))

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("images/back.png"))
        self.backButton.setIconSize(QSize(32, 32))
        self.backButton.clicked.connect(self.backBtn) # backBtn 연결
        toolbar.addWidget(self.backButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("images/forward.png"))
        self.forwardButton.setIconSize(QSize(32, 32))
        self.forwardButton.clicked.connect(self.forwardBtn) # forwardBtn 연결
        toolbar.addWidget(self.forwardButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("images/reload.png"))
        self.reloadButton.setIconSize(QSize(32, 32))
        self.reloadButton.clicked.connect(self.reloadBtn)  # reloadBtn 연결
        toolbar.addWidget(self.reloadButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("images/home.png"))
        self.homeButton.setIconSize(QSize(32, 32))
        self.homeButton.clicked.connect(self.homeBtn) # homeBtn 연결
        toolbar.addWidget(self.homeButton)

        self.addLineEdit = QLineEdit()
        self.addLineEdit.setFont(QFont("Times", 14))
        self.addLineEdit.returnPressed.connect(self.searchBtn) # 엔터로 검색 가능
        self.addLineEdit.setStyleSheet('''
            QLineEdit{
                background-color: #E1E1E2;
                border-radius: 12px;
            }
        ''')
        toolbar.addWidget(self.addLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("images/search.png"))
        self.searchButton.setIconSize(QSize(32, 32))
        self.searchButton.clicked.connect(self.searchBtn) # searchBtn 연결하기
        toolbar.addWidget(self.searchButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'https://www.google.com'
        self.addLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))



    def searchBtn(self):
        myurl = self.addLineEdit.text()
        self.webEngineView.load(QUrl(myurl))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()

    def homeBtn(self):
        self.webEngineView.load(QUrl('https://www.google.com'))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())