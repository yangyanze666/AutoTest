import pytest, time, os
import pytest_rerunfailures

file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
dir_path = file_path + "/ApiAuto/testcases/"
data_string = time.strftime('%Y-%m-%d %H%M%S', time.localtime())
report_name = "report-" + data_string + ".html"


def html_report(report_name):

    html_commandline = "--html=report/{}".format(report_name)
    return html_commandline


def allure_report():
    allure_commandline = "--alluredir= report/html --clean-alluredir"
    return allure_commandline



if __name__ == '__main__':
    # 执行指定组别，如执行冒烟测试用例 '-m smoke'
    # 执行匹配名字测试用例 -k "method_01 or method_02 " "class or function"
    # 执行用例遇到失败的就停止运行 -x
    # 执行用例遇到需要失败重新跑 --reruns n（重新运行次数）–reruns-delay m（等待运行秒数）
    # 执行指定某个.py模块下, 整个类下所有的测试用例
    # pytest.main('v', '{}api_test/test_excel_data.py::TestRealTimeData::test_get_excel_data'.format(dir_path)])
    # 执行指定某个.py模块下，类里面的具体，某个用例
    # #pytest.main(['-v', '-s', report(),
    #              '{}api_test/test_excel_data.py::TestRealTimeData::test_get_excel_data'.format(dir_path)])
    pytest.main(['-v', '-s', html_report(report_name), '{}jin_yang_dev'.format(dir_path)])
    # pytest.main(['-v', '-s', '-m smoke', report(), '{}api_test/test_jdy_api.py'.format(dir_path)])
    # pytest.main(['-v', allure_report(), '-k {}api_test/test_jdy_api.py'.format(dir_path)])
