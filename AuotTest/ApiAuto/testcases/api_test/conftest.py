import pytest
from AuotTest.ApiAuto.testcases.conftest import get_excel_data
from datetime import datetime
from py.xml import html



@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_excel_data.get(testcase_name)

@pytest.fixture(scope="function")
def update_user_telephone():
    """修改用户前，因为手机号唯一，为了使用例重复执行，每次需要先修改手机号，再执行用例"""
    update_sql = base_data["init_sql"]["update_user_telephone"]
    db.execute_db(update_sql)
    step_first()
    logger.info("修改用户操作：手工修改用户的手机号，以便用例重复执行")
    logger.info("执行SQL：{}".format(update_sql))



# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th("Description"))
#     cells.insert(1, html.th("Time", class_="sortable time", col="time"))
#     cells.pop()
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))
#     cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
#     cells.pop()
#
# @pytest.mark.hookwrapper
# def pytest_runtest_markerport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)