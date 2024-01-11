from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel


# 主页菜单
class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        # 添加背景图片
        self.background_label = QLabel(self)
        pixmap = QPixmap("img/bac.jpeg")
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())
        self.layout.addWidget(self.background_label)

        # 添加其他内容
        self.label = QLabel("来喽小张", self)
        self.layout.addWidget(self.label)