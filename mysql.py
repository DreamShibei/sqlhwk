import pymysql
pageNum = 4
class Mysql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost',user='root',password='root',database='henanopera',charset="utf8")
            self.cursor = self.conn.cursor()  # 游标对象
            print("连接数据库成功")
        except:
            print("连接失败")

    def getNum(self):
        sql = "select count(*) as num from 视频"
        dd = self.cursor.execute(sql)
        data = self.cursor.fetchmany(dd)
        return data[0][0]


    def getMovies(self, page):
        sql = "select 并列题名,团体名称,URL from 视频"
        start = (int(page) - 1) * 4
        sql = sql + " limit " + str(start) + ",4"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        return items

    def getText(self, page):
        sql = "select 并列题名,文本内容,URL from 文本"
        start = (int(page) - 1) * 4
        sql = sql + " limit " + str(start) + ",4"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        return items

    def getPicture(self, page):
        sql = "select 并列题名,URI,摘要 from 图片"
        start = (int(page) - 1) * 4
        sql = sql + " limit " + str(start) + ",4"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        return items

    def getMusic(self, page):
        sql = "select 并列题名,URI from 音频"
        start = (int(page) - 1) * 4
        sql = sql + " limit " + str(start) + ",4"
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        return items
