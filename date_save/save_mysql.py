#  导入相应的库
import pymysql
from config import config
#  定义函数链接数据库
def connect_database():
    db =pymysql.connect()