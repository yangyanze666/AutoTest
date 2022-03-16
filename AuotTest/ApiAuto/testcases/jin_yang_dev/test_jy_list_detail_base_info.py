import pytest, ast
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jin_yang_dev import get_drain_pipe_baseinfo
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from hamcrest import *


class TestJinYangApi:
    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jin_yang_dev.xlsx", "排水管管理"))
    def test_get_drain_pipe_api(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
        """
        金阳项目-排水管信息列表及详情
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json, data)
        print(result)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jin_yang_dev.xlsx", "检查井管理"))
    def test_get_inspection_well_api(self, url_path, request_method, headers, params, json, data, except_code,
                                     except_msg):
        """
        金阳项目-检查井管理列表及详情
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")
        print("result_msg:{}".format(result.json()))

    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jin_yang_dev.xlsx", "排水户管理"))
    def test_get_drainage_api(self, url_path, request_method, headers, params, json, data, except_code,
                                     except_msg):
        """
        金阳项目-排数户管理列表及详情
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")
        print("result_msg:{}".format(result.json()))

    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jin_yang_dev.xlsx", "智能井盖管理"))
    def test_intelligent_well_lid_info_api(self, url_path, request_method, headers, params, json, data, except_code,
                              except_msg):
        """
        金阳项目-智能井盖管理列表及详情
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")
        print("result_msg:{}".format(result.json()))

    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jin_yang_dev.xlsx", "污水厂管理"))
    def test_waste_water_factory_info_api(self, url_path, request_method, headers, params, json, data, except_code,
                              except_msg):
        """
        金阳项目-污水厂管理列表及详情
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")
        print("result_msg:{}".format(result.json()))

    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jin_yang_dev.xlsx", "泵站管理"))
    def test_pump_station_info_api(self, url_path, request_method, headers, params, json, data, except_code,
                              except_msg):
        """
        金阳项目-泵站管理列表及详情
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")
        print("result_msg:{}".format(result.json()))

    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jin_yang_dev.xlsx", "监测点管理"))
    def test_monitor_point_info_api(self, url_path, request_method, headers, params, json, data, except_code,
                              except_msg):
        """
        金阳项目-监测点管理列表及详情
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")
        print("result_msg:{}".format(result.json()))

