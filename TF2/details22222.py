from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout

class DetailsWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle('Details Window')

        layout = QVBoxLayout()

        key = ['index', 'location', 'du_id', 'du_name', 'ru_name', 'pci', 'cell_info', 'type', 'rssi']
        for i in range(len(data)):
            label = QLabel(f'{key[i]} = {data[i]}')
            layout.addWidget(label)

        self.setLayout(layout)
