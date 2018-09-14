# coding=utf-8
# @Author    kakunka
# @Time     :2018/9/9
import pymysql

# 数据清洗、验证、存储
class Pipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "admin123", "douban")
        self.cursor = self.db.cursor()
        
    def insert(self, review):
        sql = "insert into lagou_company values ('%s', 's', '%d')" % (review.content, review.url. review.star)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)


    def close(self):
        self.db.close()
        