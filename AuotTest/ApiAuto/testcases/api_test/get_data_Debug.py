import pytest, ast
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jin_yang_dev import get_drain_pipe_baseinfo
from AuotTest.ApiAuto.lib.operation.jiu_dao_yan import get_excel_data_info
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from hamcrest import *



#excel_data = get_excel_data("test_arm_data.xlsx", "Sheet1")
excel_data = get_excel_data("jin_yang_dev.xlsx", "Sheet1")
print("excel_data:{}".format(excel_data))



def get_drain_pipe(url_path=excel_data[0][0], request_method=excel_data[0][1], headers=excel_data[0][2], params=excel_data[0][3], json=excel_data[0][4], data=excel_data[0][5]):
    """
    金阳项目-排水管详细信息
    """

    #result = get_excel_data_info(url_path, request_method, headers, params, json, data)
    result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json,data)
    print(result)

get_drain_pipe()