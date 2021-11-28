import pymysql

print(
    '==== MAIN MENU ==== \n1. Add books \n2. Delete book \n3. Search book \n4. Sort all books \n5. List books \n6. Borrow book \n')
conn = pymysql.connect(host='127.0.0.1', user='root', password='137928', database='db', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 连接数据库


# 关闭数据库连接
# conn.close()
# cursor.close()
# 添加book1
def func1():
    name = input('请输入书名:')
    bookcode = input('请输入书的编码:')
    genre = input('请输入书的类型:')
    author = input('请输入书的作者:')
    # 添加书籍默认未借出
    sql = f"insert into book (name,bookcode,genre,author) VALUES ('{name}','{bookcode}', '{genre}','{author}')"
    cursor.execute(sql)
    return 0


# Delete book
def func2():
    name = input('请输入一个需要删除的书名:')
    sql = f"delete from book where name='{name}'"
    # 执行SQL语句
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)
    return 0


# Search book
def func3():
    name = input('请输入一个需要查询的书名:')
    sql = f"select * from book where name='{name}'"
    # 执行SQL语句
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)
    return 0


def func4():
    print('将按照id对所有书籍排序。')
    sql = f"select * from book order by id"
    # 执行SQL语句
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)
    return 0


# book列表 5
def func5():
    sql = f'select * from book'
    # 执行SQL语句
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)
    return 0


# Borrow book 6
def func6():
    name = input('请输入需要借阅图书的名称:')
    student = input('请输入借书同学的学号:')
    # 修改语句
    sql = f"update  book set holder='{student}' where name='{name}'"
    # 执行SQL语句
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)
    return 0


if __name__ == "__main__":
    while 1:
        num = int(input('Please enter a number to continue:'))
        if num == 1:
            func1()
            func5()
        elif num == 2:
            func2()
            func5()
        elif num == 3:
            func3()
            func5()
        elif num == 4:
            func4()
        elif num == 5:
            func5()
        else:
            func6()
            func5()
