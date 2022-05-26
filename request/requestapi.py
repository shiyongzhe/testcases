import requests
host = "http://localhost:8881/"

class requestapi:

    def __init__(self):
        """
       session管理器
       requests.session(): 维持会话,跨请求的时候保存参数
       """
        # 实例化session
        self.session = requests.session()

    def request_main(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        global re_data
        # 对异常进行捕获
        try:
            """
            封装request请求，将请求方法、请求地址，请求参数、请求头等信息入参。
            注 ：verify: True/False，默认为True，认证SSL证书开关；cert: 本地SSL证书。如果不需要ssl认证，可将这两个入参去掉
            """
            re_data = self.session.request(method, url, params=params, data=data, json=json, headers=headers, verify=False, **kwargs)
        # 异常处理 报错显示具体信息
        except Exception as e:
            # 打印异常
            print("请求失败：{0}".format(e))
        # 返回响应结果
        return re_data

    def buildheaders(self, headers):
        requestHeaders = {
            "Content-Type": "application/json"
        }
        # 判断headers是否为空
        d = requestHeaders.copy()
        if headers:
            d.update(headers)
        return d