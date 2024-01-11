import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QVBoxLayout, QWidget
import view.sick_leave.medical_reminder_view as mrv
import view.home_view as hv
import view.sick_leave.sick_leave_view as slv

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
        self.sick_leave_page = slv.SickLeavePage()

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

        page2_action = QAction("病假管理", self)
        page2_action.triggered.connect(self.show_sick_leave)
        menu.addAction(page2_action)

        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)
        menu.addAction(exit_action)

    def show_home(self):
        self.setCentralWidget(self.home_page)

    def show_medical_reminder(self):
        self.setCentralWidget(self.medical_reminder_page)

    def show_sick_leave(self):
        self.setCentralWidget(self.sick_leave_page)
