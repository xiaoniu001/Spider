# coding: utf-8

import requests


class Spider(object):

    """蜘蛛，爬虫类"""

    @staticmethod
    def request_url(url):
        if url:
            response = requests.get(url)
            if response.status_code == "404":
                url = input("地址请求失败，重新输入：")
                Spider.request_url(url)
            else:
                return response
        else:
            url = input("请输入链接地址：")
            Spider.request_url(url)


if __name__ == '__main__':
    Spider.request_url("")




