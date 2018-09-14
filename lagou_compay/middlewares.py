# coding=utf-8
# @Author   kakunka
# @Time     :2018/9/9
import urllib
from bs4 import BeautifulSoup

# 网页数据下载
from items import CompanyItem


class Downloader(object):
    def download(self, url):
        if url is None:
            return None
        header = {
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/" \
            "537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        }
        req = urllib.request.Request(url, headers=header)
        response = urllib.request.urlopen(req)

        if response.getcode() != 200:
            return None

        return response.read()



# 网页解析
class Parser(object):

    def parse_content(self,  url, content):
        # 将所有的评分和内容解析出来
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

        address_all = soup.find(attrs={'id': 'location_container'}).find_all(attrs={'class': 'mlist_li_desc'}) #地址列表 <p>
        address = ""  #  地址
        for address_container in address_all:
            address += address_container.string.strip()
            address += "#"    # 添加分隔符

        manager_all = soup2.find(attrs={'id':'company_managers'}).find_all(attrs={'class':'item_manager_name'})

        name = soup.find_all(attrs={'class': 'hovertips'})[0].get('title') # 公司名


        return comments

    def parse_total_page(self, content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        css_class = soup.find(attrs={'class': 'is-active'})
        total_page_string =  css_class.find('span').string
        total_page = total_page_string.split('(')[1].strip(')')
        return total_page




