import pymysql
'''
用前先看

必须使用mysql数据库
如果没有：https://mp.weixin.qq.com/s/TnrMKJOn086wpVch7_5qtQ，自行安装。
当然，你也可以使用其他的数据库

要安装pymysql库

修改user和password，将它们改成自己mysql的用户名和密码，
确保自己的mysql中有数据库’pythondb‘，没有的话创建，语句为：create database pythondb
当然，也可以修改链接的数据库
'''

'''


创建表的语句
create table addressBook(
id int primary key AUTO_INCREMENT,
name varchar(5) not null,
adress text(50),
tel varchar(11))

查询语句
select name,adress,tel from addressBook
select name,adress,tel from addressBook where name=?
select name,adress,tel from addressBook where name like ''

添加语句
insert into addressBook(name,adress,tel) values(?,?,?)

删除语句
delete from addressBook where name=?
delete from addressBook where name like ''
delete from addressBook where id=?

'''

user = 'root'#数据库用户名
password = '137928'#数据库密码，要使用自己的
db = None#数据库对象
cursor = None#游标对象


#函数的作用：获取数据库链接对象和游标对象
def getconnection():
    global db#声明全局变量
    global cursor
    db = pymysql.connect(host='localhost', user=user, password=password
                         , port=3306, db="pythondb")#获取数据库链接对象
    cursor = db.cursor()#获取游标
    sql = "select * from addressBook"#查询语句
    try:
        cursor.execute(sql,())#执行查询语句，为了判断数据库中是否有对应的数据表
    except Exception:
        #如果没有对应的数据表，就会出错，从而执行创建数据库的语句
        createTablesSql = '''
        create table addressBook(
        id int primary key AUTO_INCREMENT,
        name varchar(5) not null,
        adress text(50),
        tel varchar(11))
        '''
        cursor.execute(createTablesSql)
        print("创建数据表成功")

#在退出时关闭数据库链接和游标链接
def close():
    cursor.close()
    db.close()
persons = []


#查询说有的数据
def listPerson():
    querySql = 'select name,adress,tel from addressBook'
    cursor.execute(querySql,())
    persons = cursor.fetchall()
    showMessage(persons)

#插入数据，其中，名字是必须的，而其他的是次要的，可以为空
def insertPerson(name,adress='',tel=''):
    sql = "insert into addressBook(name,adress,tel) values(%s,%s,%s)"
    cursor.execute(sql,(name,adress,tel))
    db.commit()
    print("插入成功")

#删除对应人员，其中，为了防止用户的输入了一个在数据表中没有的人员
#在删除之前，先对数据进行查找，如果有对应数据就删除，没有就返回状态信息
def delPerson(name):
    sql = "select name,adress,tel from addressBook where name=%s"
    cursor.execute(sql, (name))
    if cursor.rowcount == 0:
        return 0
    sql = "delete  from addressBook where name=%s"
    cursor.execute(sql,(name))
    db.commit()
    print("删除成功")
    return 1

#查早对应人员，如果没有找到对应人员，再使用模糊查找，如果还没有找到，就返回错误信息
def findByName(name):
    sql = "select name,adress,tel from addressBook where name=%s"
    cursor.execute(sql,(name))
    if cursor.rowcount == 0:
        sql = "select name,adress,tel from addressBook where name like %s"
        name = "%"+name+"%"
        cursor.execute(sql,(name))
        if cursor.rowcount == 0:
            return 0
        persons = cursor.fetchall()
        showMessage(persons)
        return 1

#展示数据，将数据更加美观
def showMessage(persons):
    print("-" * 60)
    print("\t姓名",end="\t\t\t\t\t")
    print("电话",end="\t\t\t")
    print("地址")
    print("-"*60)
    for person in persons:
        print("\t",end="")
        print("%-9s"%person[0],end="")
        print("\t|",end="")
        temps = packageString(person[1])
        print("%12s"%person[2],end="\t")
        print("|", end="\t")
        print("%-25s"%temps)
        print("-"*60)

#判断电话号码是不是就11位
def isTelNumber(s):
    for i in range(11):
        try:
            int(s[i])
        except Exception:
            print("您输入的电话号码有误，请重新输入！！")
            print("如果您不想输入，按0退出")
            x = input()
            if x == '0':
                return 0
            isTelNumber(x)
    return 1

#对于过长的数据进行替换
def packageString(s):
    if len(s) >= 12:
        return s[0:9]+"..."
    return s

def main():
    #必须先获取数据库链接
    getconnection()
    while True:
        print('1. create person')
        print('2. list all persons')
        print('3. query person')
        print('4. delete person')
        print('5. quit')
        choice = input('enter a number(1-5):')

        if choice == '1':
            # create person
            name = input('name:')
            addr = input('address:')
            phone = input('phone:')
            if isTelNumber(phone) == 0:
                continue
            insertPerson(name,addr,phone)

        elif choice == '2':
            # list all persons
            listPerson()

        elif choice == '3':
            # query person
            name = input('name:')
            if findByName(name) == 0:
                print("没有您要找的人")


        elif choice == '4':
            # delete person
            name = input('name:')
            x = delPerson(name)
            if x == 0:
                print("没有您要删除的人")

        elif choice == '5':
            break
        else:
            print('invalid choice')
    close()

if __name__ == '__main__':
    main()


