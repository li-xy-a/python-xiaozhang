import openpyxl as op
import config.global_params as gp

"""
    病假列表  倒序
"""


def get_list():
    list_res = []
    try:
        wb = op.load_workbook(gp.sick_leave_execl_path)
        sheet = wb[gp.sick_leave_log_execl_sheet_name]
        for row in sheet.iter_rows(values_only=True):
            list_res.append(row)
        # 保留第一条数据
        first = list_res[0]
        list_res.remove(first)
        list_res = sorted(list_res, reverse=True)
        list_res.insert(0, first)
    except Exception as e:
        print(e)
    return list_res
