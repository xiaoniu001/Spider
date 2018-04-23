# coding: utf-8
from data_spider.spider import Spider
from bs4 import BeautifulSoup


class Parser(object):

    """数据解析类"""

    @staticmethod
    def retrieve_data(url_response):
        import time
        soup = BeautifulSoup(url_response.text, "html5lib")
        with open("../data_html/{0}.html".format(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())), "w") as file:
            file.write(url_response.text)
        return soup


if __name__ == '__main__':
    headers = {"Content-Type": "application/json;charset=utf-8"}
    response = Spider.request_url("https://github.com/search?utf8=%E2%9C%93&q=python&type=", headers=headers)
    data_json = Parser.retrieve_data(response)
