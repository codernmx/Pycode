# 删除文件
def menu():
    print(
        '==== MAIN MENU ==== \n1. 查看学生列表 \n2. 添加学生 \n3. 修改学生信息 \n4. 删除学生 \n5. 显示操作菜单\n==== MAIN MENU ====')


studentList = [
    {
        "id": "179010212",  # 学号
        "name": "小明",  # 姓名
        "age": "18",  # 年龄
        "sex": "男",  # 性别
        "cla": '软件工程101',  # 班级
    },
    {
        "id": "179010213",  # 学号
        "name": "小红",  # 姓名
        "age": "19",  # 年龄
        "sex": "女",  # 性别
        "cla": '软件工程101',  # 班级
    },
    {
        "id": "179010212",  # 学号
        "name": "李华",  # 姓名
        "age": "20",  # 年龄
        "sex": "男",  # 性别
        "cla": '软件工程101',  # 班级
    }
]


# 查看学生列表
def getList():
    for i in studentList:
        print('学号：{},姓名：{},年龄：{},性别：{},班级：{}'.format(i['id'], i['name'], i['age'], i['sex'], i['cla']))


# 修改学生信息
def reName():
    id = input('请输入需要修改的学生学号：')
    name = input('请输入学生新姓名：')
    age = input('请输入学生新年龄：')
    sex = input('请输入学生新性别：')
    cla = input('请输入学生新班级：')

    for i in range(0, len(studentList)):
        if studentList[i]['id'] == str(id):
            studentList[i]['name'] = name
            studentList[i]['age'] = age
            studentList[i]['sex'] = sex
            studentList[i]['cla'] = cla
            print('修改学号{}的信息成功！'.format(id))
            break


# 删除学生信息
def delInfo():
    id = input('请输入需要删除的学生学号：')
    for i in range(0, len(studentList)):
        if studentList[i]['id'] == str(id):
            studentList.pop(i)  # 删除数组中一个数据
            print('删除{}成功！'.format(id))
            break


def addInfo():
    id = input('请输入学生学号：')
    name = input('请输入学生姓名：')
    age = input('请输入学生年龄：')
    sex = input('请输入学生性别：')
    cla = input('请输入学生班级：')
    # 判断id是否重复
    for i in range(0,len(studentList)):
        if studentList[i]['id'] == str(id):
            id = input('当前学号重复，请重新输入：')
            break
    info = {
        "id": id,  # 学号
        "name": name,  # 姓名
        "age": age,  # 年龄
        "sex": sex,  # 性别
        "cla": cla,  # 班级
    }
    studentList.append(info)


def login(name, passw):
    if name == 'admin' and passw == 'admin':
        print('登录成功，欢迎你，{}'.format(name))
        return True
    else:
        return False


if __name__ == "__main__":
    name = input('请输入用户名:')
    passw = input('请输入密码:')
    if login(name, passw):
        menu()
        while True:
            cmdStr = input('请输入一个代码执行操作exit()退出：')
            if 'exit()' not in cmdStr:
                if cmdStr == '1':
                    getList()
                elif cmdStr == '2':
                    addInfo()
                elif cmdStr == '3':
                    reName()
                elif cmdStr == '4':
                    delInfo()
                elif cmdStr == '5':
                    menu()
            else:
                print('再见！！')
                break
    else:
        print('账号密码不对哦亲！！')
