import pymysql
#添加数据
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='Aa,123456', db='test')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)





#查询数据
row_affected=cursor.execute("select * from TEST") 
#返回的是一个数据数量
print(row_affected)

# 取出一条数据
# one=cursor.fetchone()
# print(one)

# 取出所有数据
all=cursor.fetchall()
print(all)

# 取出多条数据
# many=cursor.fetchmany(5)
# print(many)





conn.commit()
#提交
cursor.close()
conn.close()