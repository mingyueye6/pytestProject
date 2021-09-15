import json


class OperetionJson:
    # 读取json文件
    def read_data(self, filename, key=None):
        with open(filename) as fp:
            data = json.load(fp)
            if key:
                data = data[str(key)]
            return data

    # 写json
    def write_data(self, filename, key, value):
        with open(filename) as fp:
            try:
                data = json.load(fp)
            except:
                data = {}
        with open(filename, 'w') as fp:
            data[str(key)] = value
            fp.write(json.dumps(data))


if __name__ == '__main__':
    OperetionJson().read_data('../data/request_headers.json', "login")
    OperetionJson().write_data('../data/response_datas.json', 1, {"cookie":{}, "data":{}})