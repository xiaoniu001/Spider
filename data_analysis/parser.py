# coding: utf-8
from data_spider.spider import Spider
from bs4 import BeautifulSoup
from data_db.create_db import *


class Parser(object):

    """数据解析类"""

    @staticmethod
    def retrieve_data(response_data):
        import time
        soup = BeautifulSoup(response_data.text, "html5lib")
        with open("../data_html/index.html".format(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())), "w") as file:
            file.write(response_data.text)
        return soup

    @classmethod
    def language_data(cls, response_data):
        languages = []
        soup = cls.retrieve_data(response_data)
        label_a = soup.find_all("a", "filter-item")
        for label in label_a:
            languages.append(Language(text="{}".format(label.contents[2])))
        return languages


if __name__ == '__main__':
    headers = {"Content-Type": "application/json;charset=utf-8"}
    response = Spider.request_url("https://github.com/search?utf8=%E2%9C%93&q=python&type=", headers=headers)
    Parser.language_data(response)