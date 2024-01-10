# global_params.py

# 定义全局参数
# 病假execl位置
sick_leave_execl_path = '/Users/lixinyun/PycharmProjects/xiaozhang/2024年病假审批表.xlsx'
sick_leave_execl_sheet_name = '医疗期提醒'


# 修改病假execl位置
def update_global_sick_leave_execl_path(new_value):
    global sick_leave_execl_path
    sick_leave_execl_path = new_value
