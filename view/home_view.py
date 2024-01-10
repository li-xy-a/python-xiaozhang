from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


# 主页菜单
class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel("来喽小张")
        self.layout.addWidget(self.label)
