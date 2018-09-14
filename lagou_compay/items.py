# coding=utf-8
# @Author    kakunka
# @Time     :2018/9/9  

# 基本数据模型定义

class CompanyItem(object):

    #   address 公司地址字符串拼接的list，以#分割
    #   managers     公司管理团队
    #   name    公司名称
    #   intro   公司介绍
    #   info    公司基本信息
    #   info_business_type   公司业务类型
    #   info_financing   融资
    #   info_employees   人数
    #   jobs       招聘职位
    #   url_company        公司主页
    #   url     拉钩对应的网址
    def __init__(self, address, managers, name,  intro, info, info_business_type, info_financing, info_employees, jobs, url_company, url):
        self.address = address
        self.managers = managers
        self.name = name
        self.intro = intro
        self.info = info
        self.info_business_type = info_business_type
        self.info_financing = info_financing
        self.info_employees = info_employees
        self.jobs = jobs
        self.url_company = url_company
        self.url = url
