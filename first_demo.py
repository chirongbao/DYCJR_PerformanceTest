import requests
import json


def isDianzi():
    baseUrl = 'http://crmapi-test.victorplus.cn/system/home'
    header = {'vkey': 'ta8JmkuiG7mZ0Nkk4G2z5D47j67IVB10d6Q68PMwTATB0ZeiolezajGcX/5Z/1JU3SfAl615EBF+g3TgZAV5CQ==', 'X-di': 'b7788172face52f6', 'Content-Type': 'application/json'}
    # param = {'appCode': 'SN190604155914000323'}
    isDianziTest = requests.get(baseUrl, headers=header)
    print(isDianziTest.text)


isDianzi()
