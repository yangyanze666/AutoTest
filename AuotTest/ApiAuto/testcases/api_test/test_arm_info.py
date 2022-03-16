import pytest, ast
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jiu_dao_yan import get_excel_data_info
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from hamcrest import *





@pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                         get_excel_data("test_arm_data.xlsx", "Sheet1"))
class TestRealTimeData:

    def test_get_excel_data(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
        """
        九道堰接口-告警查询
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_excel_data_info(url_path, request_method, headers, params, json, data)

        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        data = result.json()
        list = data.get("data")["rows"]
        for item in list:
            assert_that(item.get("armTypeView"), equal_to("数据异常"))
        logger.info("*************** 结束执行用例 ***************")