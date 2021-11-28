import os


# 删除文件
def menu():
    print(
        '==== MAIN MENU ==== \n1. 创建文件夹 \n2. 删除文件夹 \n3. 重命名文件 \n4. 查看文件列表 \n==== MAIN MENU ====')


# 创建文件夹
def mkdi():
    try:
        name = input('请输入需要创建的文件夹名称：')
        os.mkdir(name)
    except:
        print('创建失败！')
    else:
        print("文件夹——>{}<——创建成功！".format(name))


# 重命名
def reName():
    try:
        name = input('请输入修改的文件名称：')
        rName = input('你将文件名修改为：')
        os.rename(name, rName)
    except:
        print('修改失败！')
    else:
        print("文件名——>{}<——修改成功！".format(name))


# 删除文件
def delFile():
    try:
        name = input('请输入需要删除的文件夹名称：')
        os.rmdir(name)
    except IOError:
        print('删除失败！')
    else:
        print("删除成功！")


def lookFile():
    names = os.listdir()
    for i in names:
        print(i)


def login(name, passw):
    if name == 'admin' and passw == 'admin':
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
                    mkdi()
                elif cmdStr == '2':
                    delFile()
                elif cmdStr == '3':
                    reName()
                elif cmdStr == '4':
                    lookFile()
            else:
                print('再见！！')
                break
    else:
        print('账号密码不对哦亲！！')
