import pytest, json, ast, pytest_ordering
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jin_yang_dev import get_drain_pipe_baseinfo
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from hamcrest import *




class TestJinYangApiCreateModifyDelete:

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                             get_excel_data("jy_add_modify_delete.xlsx", "新增智能井盖"))
    def test_add_inspection_well_api(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
        """
        金阳项目-新增智能井盖信息
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

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("url_path, request_method, headers, params, json_data, data, except_code, except_msg",
                             get_excel_data("jy_add_modify_delete.xlsx", "智能井盖唯一性校验"))
    def test_verify_unique_pkid(self, url_path, request_method, headers, params, json_data, data, except_code,
                                except_msg):
        """
        金阳项目-智能井盖管理-唯一性校验
        """


        result = get_drain_pipe_baseinfo(url_path, request_method, headers, params, json_data, data)
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("data") == ast.literal_eval(except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("url_path, request_method, headers, params, json_data, data, except_code, except_msg",
                             get_excel_data("jy_add_modify_delete.xlsx", "智能井盖更新信息"))
    def test_modify_inspection_well_api(self, url_path, request_method, headers, params, json_data, data, except_code,
                                except_msg):
        """
        金阳项目-智能井盖管理-修改泵站信息
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

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("url_path, request_method, headers, params, json_data, data, except_code, except_msg",
                             get_excel_data("jy_add_modify_delete.xlsx", "智能井盖删除信息"))
    def test_delete_inspection_well_api(self, url_path, request_method, headers, params, json_data, data, except_code,
                                except_msg):
        """
        金阳项目-智能井盖管理-删除泵站信息
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