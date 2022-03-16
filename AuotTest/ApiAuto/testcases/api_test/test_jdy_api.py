import pytest
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jiu_dao_yan import get_excel_data_info
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from hamcrest import *


@pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                         get_excel_data("test_data.xlsx", "Sheet3"))
class TestOneMap:

    def test_one_map_api(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
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


@pytest.mark.smoke
@pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                         get_excel_data("test_data.xlsx", "Sheet4"))
class TestRealInfo:

    def test_one_map_api(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
        """
        冒烟测试：
        九道堰接口-告警消息测试用例
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_excel_data_info(url_path, request_method, headers, params, json, data)
        print("*************** 开始执行用例 ***************")
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code


@pytest.mark.flaky(reruns=3, reruns_delay=5)
@pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                         get_excel_data("test_data.xlsx", "Sheet5"))
class TestHistoryData:

    def test_one_map_api(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
        """
        九道堰接口-监测历史测试用例
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_excel_data_info(url_path, request_method, headers, params, json, data)
        print("*************** 开始执行用例 ***************")
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
