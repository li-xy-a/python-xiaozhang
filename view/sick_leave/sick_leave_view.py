from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QWidget, QDialog, QLabel, \
    QHBoxLayout, QFormLayout, QLineEdit, QCalendarWidget
import func.medical_reminder as mr
import func.sick_leav as sl

"""
    病假页面
"""


def on_button_click():
    # 新打开一个窗口
    add_view = AddView()
    add_view.exec_()


class SickLeavePage(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        # 创建按钮
        self.button = QPushButton('新增病假', self)
        # 增加点击事件
        self.button.clicked.connect(on_button_click)
        # 按钮放入页面
        self.layout.addWidget(self.button)
        # 创建表格
        self.table_widget = QTableWidget(self)
        # 表格放入页面
        self.layout.addWidget(self.table_widget)
        # 初始化查询
        self.populate_table()

    # 查询表格数据
    def populate_table(self):
        # 查询数据
        data = sl.get_list()

        # 清空表格
        self.table_widget.clear()

        # 设置表格的行数和列数
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(len(data[0]) + 1)

        # 添加数据到表格
        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.table_widget.setItem(row_index, col_index, item)


class AddView(QDialog):
    def __init__(self):
        super().__init__()
        # 设置对话框标题
        self.setWindowTitle("新增病假")

        # 创建布局
        layout = QVBoxLayout(self)

        # 创建表单布局
        form_layout = QFormLayout()

        # 添加表单字段

        self.motorcade_input = QLineEdit(self)
        form_layout.addRow("车队:", self.motorcade_input)

        self.name_input = QLineEdit(self)
        form_layout.addRow("姓名:", self.name_input)

        self.age_input = QLineEdit(self)
        form_layout.addRow("年龄:", self.age_input)

        self.entry_time_input = QLineEdit(self)
        form_layout.addRow("入职时间:", self.entry_time_input)

        self.end_entry_time_input = QLineEdit(self)
        form_layout.addRow("退休时间:", self.end_entry_time_input)

        self.end_entry_time_input = QLineEdit(self)
        form_layout.addRow("诊断情况:", self.end_entry_time_input)

        self.end_entry_time_input = QLineEdit(self)
        form_layout.addRow("诊断医院:", self.end_entry_time_input)

        self.start_date_input = QLineEdit(self)
        form_layout.addRow("请假开始时间:", self.start_date_input)

        self.end_date_input = QLineEdit(self)
        form_layout.addRow("请假结束时间:", self.end_date_input)

        # 添加表单到总体布局
        layout.addLayout(form_layout)

        # 添加确认和取消按钮
        button_layout = QHBoxLayout()
        ok_button = QPushButton("提交", self)
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("取消", self)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)