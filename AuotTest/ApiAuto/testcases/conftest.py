import pytest, os
from AuotTest.ApiAuto.lib.common.read_data import data
from AuotTest.ApiAuto.lib.common.logger import logger
from py.xml import html
from AuotTest.ApiAuto.lib.common.tools import list_of_group
from AuotTest.ApiAuto.lib.common.pg_operate import db

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


def get_excel_data(excel_file_name, sheet_name):
    """
    获取excel中的数据
    :return: 返回抽取的列表值
    """
    try:
        data_file_path = os.path.join(BASE_PATH, "data", excel_file_name)
        excel_data = data.load_excel(data_file_path, sheet_name=sheet_name)
        list_data = []
        result_data = []
        for item in excel_data:
            for key, value in item.items():
                list_data.append(value)
            result_data = list_of_group(list_data, 8)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return result_data


api_data = get_data("one_map_data.yml")
base_data = get_data("base_data.yml")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    在测试报告中添加用例名称
    :param item: 测试用例
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    report.extra = extra
    report.description = str(item.function.__doc__)
    return report.description


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("用例名称"))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.th(report.description))


@pytest.fixture(scope="function")
def delete_insert_data():
    """插入数据前，先删除数据，用例执行之后，再次删除以清理数据"""
    del_sql = base_data["init_sql"]["delete_data"]
    db.execute_db(del_sql)
    logger.info("插入数据")
    logger.info("执行前置SQL：{}".format(del_sql))
    yield
    db.execute_db(del_sql)
    logger.info("删除数据")
    logger.info("执行后置SQL：{}".format(del_sql))


@pytest.fixture(scope="function")
def update_data():
    """修改数据前，因为ID唯一，为了使用例重复执行，每次需要先修改ID，再执行用例"""
    update_sql = base_data["init_sql"]["update_data"]
    db.execute_db(update_sql)
    logger.info("修改数据时先修改ID，以便用例重复执行")
    logger.info("执行SQL：{}".format(update_sql))


@pytest.fixture(scope="function")
def insert_data():
    """插入数据前，因为ID唯一，为了使用例重复执行，每次需要先修改ID，再执行用例"""
    update_sql = base_data["init_sql"]["insert_data"]
    db.execute_db(update_sql)
    logger.info("插入数据时先修改ID，以便用例重复执行")
    logger.info("执行SQL：{}".format(update_sql))
