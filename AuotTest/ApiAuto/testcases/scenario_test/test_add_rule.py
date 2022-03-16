import pytest
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jiu_dao_yan import get_excel_data_info
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from hamcrest import *


@pytest.mark.usefixtures("insert_data")
@pytest.mark.parametrize("url_path, request_method, headers, params, json, data, except_code, except_msg",
                         get_excel_data("test_data_rule.xlsx", "Sheet1"))
class TestAddRule:

    def test_get_excel_data(self, url_path, request_method, headers, params, json, data, except_code, except_msg):
        """
        九道堰接口-添加数据规则
        """

        logger.info("*************** 开始执行用例 ***************")
        result = get_excel_data_info(url_path, request_method, headers, params, json, data)
        print("*************** 开始执行用例 ***************")
        assert_that(result.json().get("code"), equal_to(except_code))
        assert result.json().get("code") == except_code
        assert_that(result.json().get("code"), except_msg)
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.json().get("code")))
        assert result.json().get("code") == except_code
        list = result.json().get("data")["rows"]
        rule_names = []
        for item in list:
            rule_names.append(item.get("ruleName"))
        assert_that("AutoTest04", is_in(rule_names))



        logger.info("*************** 结束执行用例 ***************")
