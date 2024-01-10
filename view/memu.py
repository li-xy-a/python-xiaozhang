import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QVBoxLayout, QWidget
import view.medical_reminder_view as mrv
import view.home_view as hv

"""
    主菜单页面
"""

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("小张的工具箱")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = None  # 初始时 central_widget 为 None
        self.home_page = hv.HomePage()
        self.medical_reminder_page = mrv.MedicalReminderPage()
        self.page2 = Page2()

        self.setCentralWidget(self.home_page)  # 设置初始的 central_widget

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel("来喽小张", self.central_widget)
        self.layout.addWidget(self.label)
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        menu = menubar.addMenu("菜单")

        home_action = QAction("首页", self)
        home_action.triggered.connect(self.show_home)
        menu.addAction(home_action)

        page1_action = QAction("医疗期提醒", self)
        page1_action.triggered.connect(self.show_medical_reminder)
        menu.addAction(page1_action)

        page2_action = QAction("病假显示", self)
        page2_action.triggered.connect(self.show_page2)
        menu.addAction(page2_action)

        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)
        menu.addAction(exit_action)

    def show_home(self):
        self.setCentralWidget(self.home_page)
        self.label.setText("小张来啦")

    def show_medical_reminder(self):
        self.setCentralWidget(self.medical_reminder_page)
        self.label.setText("医疗期提醒页面")

    def show_page2(self):
        self.setCentralWidget(self.page2)
        self.label.setText("这是页面 2")


class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel("这是页面 2")
        self.layout.addWidget(self.label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
