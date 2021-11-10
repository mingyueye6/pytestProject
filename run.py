import os
import pytest
import shutil


if __name__ == '__main__':
    # 生成python-html报告
    # pytest.main(['-s', '-v', '--html=./reports/reports.html'])

    # 使用allure生成报告
    if os.path.exists('./report2'):
        shutil.rmtree('./report2')
    pytest.main(['--alluredir=./report2/xml'])
    # pytest.main(['-m', 'demo', '--alluredir=./report2/xml'])
    os.system('allure generate ./report2/xml -o ./report2/result')

