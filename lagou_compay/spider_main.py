# coding=utf-8
# @Author    kakunka
# @Time     :2018/9/9


from url_manager import  UrlManager
from middlewares import  Downloader
from middlewares import  Parser
from pipeline    import  Pipeline

# 爬虫的主类
class SpiderMain(object):
    def __init__(self, pageLimit):
        self.urls = UrlManager()                    # url管理器，负责url分发
        self.downloader = Downloader()              # 根据url抓取网页数据
        self.parser = Parser()                      # 解析下载的网页
        self.pipeline = Pipeline()                  # 数据清洗、验证、存储
