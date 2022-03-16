import pytest
from AuotTest.ApiAuto.lib.common.logger import logger
from AuotTest.ApiAuto.lib.operation.jiu_dao_yan import get_real_time_data
from AuotTest.ApiAuto.testcases.conftest import api_data


@pytest.mark.parametrize("token, curPage, pageSize, pointCode, except_result, except_code, except_msg",
                         api_data["test_get_real_time_data"])
class TestRealTimeData():
    """
    测试获取实时监测数据
    """

    def test_get_real_time_data(self, token, curPage, pageSize, pointCode, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = get_real_time_data(token, curPage, pageSize, pointCode)

        assert result.success == except_result, result.error
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.msg == except_msg
        assert result.response.json().get("code") == except_code
        print(api_data["test_get_real_time_data"])
        logger.info("*************** 结束执行用例 ***************")
