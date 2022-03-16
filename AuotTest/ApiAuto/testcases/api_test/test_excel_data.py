import pytest
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jiu_dao_yan import get_excel_data_info
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from hamcrest import *





@pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                         get_excel_data("test_data.xlsx", "Sheet1"))
class TestRealTimeData:

    def test_get_excel_data(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
        """
        九道堰接口-监测一张图测试用例
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_excel_data_info(url_path, request_method, headers, params, json, data)
        print("*************** 开始执行用例 ***************")
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")




# @pytest.mark.flaky(reruns=2, reruns_delay=5)  # 只有失败的用例才重跑
# @pytest.mark.skipif(condition=2 > 1, reason="不在本次测试范围内")
# class TestCase01():
#     print("相关功能未实现，所以本次版本不进行测试")
