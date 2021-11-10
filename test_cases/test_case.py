import json
import os

import jsonpath
import pytest
from tools.operation_excel import ReadExcel
from tools.setting import *
from tools.send_request import SendRequest
from tools.operation_json import OperetionJson
import allure


class TestCase():
    casexlsx_path = os.path.join(project_path, 'data/test_case.xlsx')
    cases = ReadExcel(casexlsx_path, "case").get_all_values()
    send_rqeuest = SendRequest()

    # @pytest.mark.demo
    # @allure.feature("测试")
    @pytest.mark.parametrize("case", cases)
    def test_request(self, case):
        if case[is_run_col] == "yes":
            row = case[row_num_col]
            # 判断是否有依赖数据
            rely_row = case[rely_row_col]
            if rely_row:
                response_path = os.path.join(project_path, 'data/response_datas.json')
                rely_data = OperetionJson().read_data(response_path, rely_row)
                key = case[rely_field_col]
                value = jsonpath.jsonpath(rely_data, case[rely_data_col])[0]
            url = case[request_url_col]
            method = case[request_method_col]
            data = case[request_data_col]
            # 判断是否有请求数据
            if data:
                data = json.loads(data)
                if rely_row:
                    data["csrfmiddlewaretoken"] = value
            # 判断是否有请求头
            header = case[request_header_col]
            if header:
                header = json.loads(header)
                if rely_row:
                    header["Cookie"] = key + "=" + value
            response_type = case[response_type_col]
            res_data = self.send_rqeuest.send_request(url, method, data, header, response_type)
            # 保存响应数据
            response_path = os.path.join(project_path, 'data/response_datas.json')
            OperetionJson().write_data(response_path, row, res_data)
            # 判断是否有断言
            expected_result = case[expected_result_col]
            run_result = "pass"
            if expected_result:
                expected_result = expected_result.split(",")
                data = res_data["data"]
                for i in expected_result:
                    key = i.split("=")[0]
                    value = "=".join(i.split("=")[1:])
                    res_value = jsonpath.jsonpath(data, key)[0]
                    if value != res_value:
                        run_result = "fail"
            test_case_path = os.path.join(project_path, 'data/test_case.xlsx')
            ReadExcel(test_case_path, "case").write_value(row + 1, run_result_col, run_result)
            if run_result == "fail":
                pass