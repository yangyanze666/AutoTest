import pytest, json, ast
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jin_yang_dev import get_drain_pipe_baseinfo
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from hamcrest import *




class TestJYWasteWaterFactoryApiCreateModifyDelete:


    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jy_add_modify_delete.xlsx", "新增污水厂信息"))
    def test_add_waste_water_factory_api(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
        """
        金阳项目-新增污水厂信息
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
                             get_excel_data("jy_add_modify_delete.xlsx", "污水厂唯一性校验"))
    def test_verify_unique_pkid(self, url_path, request_method, headers, params, json_data, data, except_code,
                                except_msg):
        """
        金阳项目-污水厂管理-唯一性校验
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
                             get_excel_data("jy_add_modify_delete.xlsx", "污水厂信息更新"))
    def test_modify_add_waste_water_factory_api(self, url_path, request_method, headers, params, json_data, data, except_code,
                                     except_msg):
        """
        金阳项目-修改污水厂信息
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
                             get_excel_data("jy_add_modify_delete.xlsx", "污水厂信息删除"))
    def test_delete_add_waste_water_factory_api(self, url_path, request_method, headers, params, json_data, data, except_code,
                                     except_msg):
        """
        金阳项目-删除污水厂信息
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