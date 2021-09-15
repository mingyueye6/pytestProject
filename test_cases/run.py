import pytest

if __name__ == '__main__':
    # 生成python-html报告
    pytest.main(['-s', '-v', '--html=../reports/report.html'])