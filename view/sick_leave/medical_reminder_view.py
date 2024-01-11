from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QWidget
import func.medical_reminder as mr

"""
    医疗期提醒页面
"""


class MedicalReminderPage(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        # 创建按钮
        self.button = QPushButton('点击更新医疗期到期人员', self)
        # 增加点击事件
        self.button.clicked.connect(self.on_button_click)
        # 按钮放入页面
        self.layout.addWidget(self.button)

        # 创建表格
        self.table_widget = QTableWidget(self)
        # 表格放入页面
        self.layout.addWidget(self.table_widget)

        res = mr.get_list()
        self.populate_table(res)

    # 更新提醒数据
    def on_button_click(self):
        # 更新方法
        mr.get_expire()
        # 刷新列表
        res = mr.get_list()
        self.populate_table(res)

    # 查询表格数据
    def populate_table(self, data):
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
            if row_index != 0:
                # 创建自定义按钮
                button = QPushButton("点击已提醒")
                button.clicked.connect(lambda _, row=row_data: self.go_remind(row))

                # 将按钮添加到表格中
                self.table_widget.setCellWidget(row_index, len(data[0]), button)

    # 去提醒
    def go_remind(self, row):
        mr.remind(row[0])
        res = mr.get_list()
        self.populate_table(res)


if __name__ == "__main__":
    # 你的应用程序入口
    pass
