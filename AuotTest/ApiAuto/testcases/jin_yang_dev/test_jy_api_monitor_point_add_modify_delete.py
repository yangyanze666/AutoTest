import pytest, json, ast
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jin_yang_dev import get_drain_pipe_baseinfo
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from hamcrest import *




class TestJinYangApiCreateModifyDelete:

    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jy_add_modify_delete.xlsx", "新增监测点基本信息"))
    def test_add_monitor_point_api(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
        """
        金阳项目-新增监测点信息
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")
        global pkid
        pkid = result.json().get("data")["pkid"]



    @pytest.mark.parametrize("url_path, request_method, headers, params, json_data, data, except_code, except_msg",
                             get_excel_data("jy_add_modify_delete.xlsx", "监测点位信息唯一性校验"))
    def test_verify_unique_pkid(self, url_path, request_method, headers, params, json_data, data, except_code,
                                except_msg):
        """
        金阳项目-监测点管理-唯一性校验
        """

        pkid_data = json.loads(json_data)
        pkid_data["pkid"] = pkid

        json_data_modify = json.dumps(pkid_data)

        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json_data_modify, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("data") == ast.literal_eval(except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.parametrize("url_path, request_method, headers, params, json_data, data, except_code, except_msg",
                             get_excel_data("jy_add_modify_delete.xlsx", "监测点位信息更新"))
    def test_modify_monitor_point_api(self, url_path, request_method, headers, params, json_data, data, except_code,
                                except_msg):
        """
        金阳项目-监测点管理-修改监测点信息
        """

        pkid_data = json.loads(json_data)
        pkid_data["pkid"] = pkid
        json_data_modify = json.dumps(pkid_data)

        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json_data_modify, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.parametrize("url_path, request_method, headers, params, json_data, data, except_code, except_msg",
                             get_excel_data("jy_add_modify_delete.xlsx", "监测点位信息删除"))
    def test_delete_monitor_point_api(self, url_path, request_method, headers, params, json_data, data, except_code,
                                except_msg):
        """
        金阳项目-监测点管理-删除监测点信息
        """

        pkid_data = json.loads(json_data)
        pkid_data["pkid"] = pkid
        json_data_modify = json.dumps(pkid_data)

        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json_data_modify, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        logger.info("*************** 结束执行用例 ***************")