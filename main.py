# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from entity.params import params
from excel.read import readexcel
from request.requestapi import requestapi
from excel.export import exportexcel
import json


def main():
    host = "http://localhost:8881"
    rx = readexcel()
    cases = rx.start_read()
    api = requestapi()
    list = []
    # 获取测试用例 开始请求接口
    for index in range(len(cases)):
        p = cases[index]
        # 请求地址
        url = host + p.apipath
        # 请求头
        headers = api.buildheaders({})
        # 调用request_main，并将参数传过去
        request_data = api.request_main(str(p.requestmethod).lower(), url, json=json.loads(p.params), headers=headers)
        p.expectresult = request_data.text
        p.params = json.loads(p.params)
        list.append(p)
    # 测试结果返回生成excel 测试用例
    export = exportexcel()
    export.createsheet(list)
    print(list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
