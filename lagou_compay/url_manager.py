# coding=utf-8
# @Author   kakunka
# @Time     :2018/9/9

class UrlManager(object):
    # 记录要爬取的url和未爬取的url
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.companys = 0

    #  添加新的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.old_urls and url not in self.new_urls:
            self.new_urls.add(url)
            self.companys += 1


    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    #   是否还有没有爬取的公司网页
    def has_new_url(self):
        return len(self.new_urls) != 0

    #   取出一个url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return  new_url

  


