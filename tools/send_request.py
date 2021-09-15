import requests
import json


class SendRequest:
    def send_request(self, url, method="GET", data=None, headers=None, response_type="txt"):
        if method.upper() == "GET":
            res = requests.get(url=url, data=data, headers=headers)
        elif method.upper() == "POST":
            res = requests.post(url=url, data=data, headers=headers)
        elif method.upper() == "DELETE":
            res = requests.delete(url=url, data=data, headers=headers)
        elif method.upper() == "PUT":
            res = requests.put(url=url, data=data, headers=headers)
        else:
            return None
        if response_type.lower() == "json":
            data = res.json()
        else:
            data = res.content.decode()
        cookies = requests.utils.dict_from_cookiejar(res.cookies)
        return {"cookies": cookies, "data": data}


if __name__ == '__main__':
    run_method = SendRequest()
    data1 = run_method.send_request("http://49.235.168.69:8000/api-auth/login/?next=/")
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cache-Control": "max-age=0",
        "Connection": "keep-alive", "Host": "49.235.168.69:8000", "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Cookie": "csrftoken=%s" % data1["cookies"]["csrftoken"]
    }
    data = {
        "csrfmiddlewaretoken": data1["cookies"]["csrftoken"],
        "next": "/?format=json",
        "username": "test001",
        "password": "ceshi001",
        "submit": "Log in"
    }
    data2 = run_method.send_request("http://49.235.168.69:8000/api-auth/login/?next=/", "post", data=data,
                                    headers=headers)
    print([data1])
    print([data2])
    headers2 = headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Cache-Control": "max-age=0",
        "Connection": "keep-alive", "Host": "49.235.168.69:8000", "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Referer": "http://49.235.168.69:8000/userfavs/?format=json",
        "Cookie": "csrftoken=%s" % data1["cookies"]["csrftoken"]
    }
    data3 = run_method.send_request("http://49.235.168.69:8000/userfavs/1", "delete",
                                    headers=headers)
    print(data3)


