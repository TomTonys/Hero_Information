import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "python_mysql")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE lolheroinfo (
         id  INT  PRIMARY KEY AUTO_INCREMENT,
         英雄称号  CHAR(255),
         英雄名称 CHAR(255),  
         被动技能 CHAR(255),
         主动技能 CHAR(255)
         )AUTO_INCREMENT = 1
         """

cursor.execute(sql)

# 关闭数据库连接
db.close()
