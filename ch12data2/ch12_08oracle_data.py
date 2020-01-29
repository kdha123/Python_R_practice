import cx_Oracle
import os

# 한글처리
os.environ["NLS_LANG"] = ".UTF8"

connection = cx_Oracle.connect("c##java04/java04@402-oracle:1521/orcl")
cur = connection.cursor()

sql = "select * from member"
# sql2 = "insert into member values ('inserttest', '1111', '테스트', '2020-01-02', '남자', '010-0000-0000', " \
#        "'dlapdlf@naver.com', '구로', 1, 1, 0) "
#
# cur.execute(sql2)
# connection.commit()

cur.execute(sql)

for x in cur:
    print(x)

connection.close()
