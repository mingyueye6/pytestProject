import re
import json
import pytest
import requests

user_list = json.load(open("data/users.json", mode="r", encoding="utf-8"))

@pytest.mark.parametrize("user", user_list["user_list"])
def test_login(user):
    base_url = 'http://192.168.24.1:8000/api-auth/login/'
    res = requests.get(url=base_url)
    cookies = res.headers.get("Set-Cookie", '')
    csrftoken = re.findall('csrftoken=(.*?);', cookies)[0]
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookies,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }
    data = {
        "csrfmiddlewaretoken": csrftoken,
        "next": "/?format=json",
        "username": user[0]["username"],
        "password": user[0]["password"],
        "submit": "Log in"
    }
    res = requests.post(url=base_url, data=data, headers=headers)
    code = res.status_code
    json_str = res.json()
    assert code == user[1]
    # print(json_str)
