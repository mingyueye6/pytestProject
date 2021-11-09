import os
import pytest
import shutil

# pytest.main(['-s', '-v', '--html=./reports/reports.html'])
if __name__ == '__main__':
    # 生成python-html报告
    # pytest.main(['-s', '-v', '--html=./reports/reports.html'])

    # 使用allure生成报告
    if os.path.exists('./report2'):
        shutil.rmtree('./report2')
    pytest.main(['--alluredir','./report2/xml'])
    os.system('allure genera te ./report2/xml -o ./report2/result')