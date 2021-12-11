from tkinter import *

scoreInfo = []
def counResult(name):
    tall = float(input('请输入身高:'))
    heavy = float(input('请输入体重:'))
    fei = float(input('请输入肺活量:'))
    up = float(input('请输入引体向上:'))
    jump = float(input('立定跳远(cm):'))
    sr = float(input('50m短跑(s):'))
    lr = float(input('1000长跑(min):'))
    qu = float(input('坐位体前屈(cm):'))
    # 肺活量成绩
    if fei < 2460:
        gfei = 10
    elif fei >= 2400 and fei < 2620:
        gfei = 20
    elif fei >= 2620 and fei < 2780:
        gfei = 30
    elif fei >= 2780 and fei < 2940:
        gfei = 40
    elif fei >= 2940 and fei < 3100:
        gfei = 50
    elif fei >= 3100 and fei < 3200:
        gfei = 60
    elif fei >= 3200 and fei < 3340:
        gfei = 62
    elif fei >= 3340 and fei < 3460:
        gfei = 64
    elif fei >= 3460 and fei < 3580:
        gfei = 66
    elif fei >= 3580 and fei < 3700:
        gfei = 68
    elif fei >= 3700 and fei < 3820:
        gfei = 70
    elif fei >= 3820 and fei < 3940:
        gfei = 72
    elif fei >= 3940 and fei < 4060:
        gfei = 74
    elif fei >= 4060 and fei < 4180:
        gfei = 76
    elif fei >= 4180 and fei < 4300:
        gfei = 78
    elif fei >= 4300 and fei < 4550:
        gfei = 80
    elif fei >= 4550 and fei < 4800:
        gfei = 85
    elif fei >= 4800 and fei < 4920:
        gfei = 90
    elif fei >= 4920 and fei < 5040:
        gfei = 95
    elif fei >= 5040:
        gfei = 100

    # 50m成绩
    if sr <= 6.7:
        gsr = 100
    elif sr > 6.7 and sr <= 6.8:
        gsr = 95
    elif sr > 6.8 and sr <= 6.9:
        gsr = 90
    elif sr > 6.9 and sr <= 7:
        gsr = 85
    elif sr > 7 and sr <= 7.1:
        gsr = 80
    elif sr > 7.1 and sr <= 7.3:
        gsr = 78
    elif sr > 7.3 and sr <= 7.5:
        gsr = 76
    elif sr > 7.5 and sr <= 7.7:
        gsr = 74
    elif sr > 7.7 and sr <= 7.9:
        gsr = 72
    elif sr > 7.9 and sr <= 8.1:
        gsr = 70
    elif sr > 8.1 and sr <= 8.3:
        gsr = 68
    elif sr > 8.3 and sr <= 8.5:
        gsr = 66
    elif sr > 8.5 and sr <= 8.7:
        gsr = 64
    elif sr > 8.7 and sr <= 8.9:
        gsr = 62
    elif sr > 8.9 and sr <= 9.1:
        gsr = 60
    elif sr > 9.1 and sr <= 9.3:
        gsr = 50
    elif sr > 9.3 and sr <= 9.5:
        gsr = 40
    elif sr > 9.5 and sr <= 9.7:
        gsr = 30
    elif sr > 9.7 and sr <= 9.9:
        gsr = 20
    elif sr > 9.9 and sr <= 10.1:
        gsr = 10
    elif sr > 10.1:
        gsr = 10

    # 1000m成绩
    if lr <= 3.17:
        glr = 100
    elif lr > 3.17 and lr <= 3.22:
        glr = 95
    elif lr > 3.22 and lr <= 3.27:
        glr = 90
    elif lr > 3.27 and lr <= 3.34:
        glr = 85
    elif lr > 3.34 and lr <= 3.42:
        glr = 80
    elif lr > 3.42 and lr <= 3.47:
        glr = 78
    elif lr > 3.47 and lr <= 3.52:
        glr = 76
    elif lr > 3.52 and lr <= 3.57:
        glr = 74
    elif lr > 3.57 and lr <= 4.02:
        glr = 72
    elif lr > 4.02 and lr <= 4.07:
        glr = 70
    elif lr > 4.07 and lr <= 4.12:
        glr = 68
    elif lr > 4.12 and lr <= 4.17:
        glr = 68
    elif lr > 4.17 and lr <= 4.22:
        glr = 66
    elif lr > 4.22 and lr <= 4.27:
        glr = 66
    elif lr > 4.27 and lr <= 4.32:
        glr = 64
    elif lr > 4.32 and lr <= 4.52:
        glr = 62
    elif lr > 4.52 and lr <= 5.12:
        glr = 60
    elif lr > 5.12 and lr <= 5.32:
        gsr = 50
    elif lr > 5.32 and lr <= 5.52:
        glr = 40
    elif lr > 5.52 and lr <= 6.12:
        glr = 30
    elif lr > 6.12:
        glr = 20

    # 坐位体前屈成绩
    gqu = 0
    if qu < -0.3:
        gqu = 10
    elif qu >= -0.3 and qu < 0.7:
        gqu = 20
    elif qu >= 0.7 and qu < 1.7:
        gqu = 30
    elif qu >= 1.7 and qu < 2.7:
        gqu = 40
    elif qu >= 2.7 and qu < 3.7:
        gqu = 50
    elif qu >= 3.7 and qu < 5.1:
        gqu = 60
    elif qu >= 5.1 and qu < 6.5:
        gqu = 62
    elif qu >= 6.5 and qu < 7.9:
        gqu = 64
    elif qu >= 7.9 and qu < 9.3:
        gqu = 66
    elif qu >= 9.3 and qu < 10.7:
        gqu = 68
    elif qu >= 10.7 and qu < 12.1:
        gfei = 70
    elif qu >= 12.1 and qu < 13.5:
        gqu = 72
    elif qu >= 13.5 and qu < 14.9:
        gqu = 74
    elif qu >= 14.9 and qu < 16.3:
        gqu = 76
    elif qu >= 16.3 and qu < 17.7:
        gqu = 78
    elif qu >= 17.7 and qu < 19.5:
        gqu = 80
    elif qu >= 19.5 and qu < 21.3:
        gqu = 85
    elif qu >= 21.3 and qu < 23.1:
        gqu = 90
    elif qu >= 23.1 and qu < 24.9:
        gqu = 95
    elif qu >= 24.9:
        gqu = 100

    # 立定跳远成绩
    if jump < 188:
        gjump = 10
    elif jump >= 188 and jump < 193:
        gjump = 20
    elif jump >= 193 and jump < 198:
        gjump = 30
    elif jump >= 198 and jump < 203:
        gjump = 40
    elif jump >= 203 and jump < 208:
        gjump = 50
    elif jump >= 208 and jump < 212:
        gjump = 60
    elif jump >= 212 and jump < 216:
        gjump = 62
    elif jump >= 216 and jump < 220:
        gjump = 64
    elif jump >= 220 and jump < 224:
        gjump = 66
    elif jump >= 224 and jump < 228:
        gjump = 68
    elif jump >= 228 and jump < 232:
        gjump = 70
    elif jump >= 232 and jump < 236:
        gjump = 72
    elif jump >= 236 and jump < 240:
        gjump = 74
    elif jump >= 240 and jump < 244:
        gjump = 76
    elif jump >= 244 and jump < 248:
        gjump = 78
    elif jump >= 248 and jump < 256:
        gjump = 80
    elif jump >= 256 and jump < 263:
        gjump = 85
    elif jump >= 263 and jump < 268:
        gjump = 90
    elif jump >= 268 and jump < 273:
        gjump = 95
    elif jump >= 273:
        gjump = 100

    # 引体向上成绩
    if up < 6:
        gup = 10
    elif up >= 6 and up < 7:
        gup = 20
    elif up >= 7 and up < 8:
        gup = 30
    elif up >= 8 and up < 9:
        gup = 40
    elif up >= 9 and up < 10:
        gup = 50
    elif up >= 10 and up < 11:
        gup = 60
    elif up >= 11 and up < 12:
        gup = 64
    elif up >= 12 and up < 13:
        gup = 68
    elif up >= 13 and up < 14:
        gup = 72
    elif up >= 14 and up < 15:
        gup = 76
    elif up >= 15 and up < 16:
        gup = 80
    elif up >= 16 and up < 17:
        gup = 85
    elif up >= 17 and up < 18:
        gup = 90
    elif up >= 18 and up < 19:
        gup = 95
    elif up >= 19 and up < 30:
        gup = 100 + (up - 19) * 10
    elif up >= 30:
        gup = 200

    # 身高体重成绩
    ht = heavy / (tall * tall)
    if ht >= 17.9 and ht <= 23.9:
        ght = 100
    elif ht <= 17.8:
        ght = 80
    elif ht >= 24 and ht <= 27.9:
        ght = 80
    elif ht >= 28:
        ght = 60

    # 总成绩
    sco = (ght + gfei) * 0.15 + (gsr + glr) * 0.2 + (gqu + gjump + gup) * 0.1
    # print(result)
    # tall = float(input('请输入身高:'))
    # heavy = float(input('请输入体重:'))
    # fei = float(input('请输入肺活量:'))
    # up = float(input('请输入引体向上:'))
    # jump = float(input('立定跳远(cm):'))
    # sr = float(input('50m短跑(s):'))
    # lr = float(input('1000长跑(min):'))
    # qu = float(input('坐位体前屈(cm):'))
    result = {
        "name": name,
        "tall": tall,
        "heavy": heavy,
        "fei": fei,
        "up": up,
        "jump": jump,
        "sr": sr,
        "lr": lr,
        "qu": qu,
        "sco": sco,
    }
    return result


def menu():
    print(
        '==== MAIN MENU ==== \n1. 查看录入的列表 \n2. 添加学生成绩 \n3. 修改学生体侧成绩 \n4. 删除学生成绩 \n5. 计算体侧成绩 \n6. 显示操作菜单\n==== MAIN MENU ====')


def getList():
    for i in scoreInfo:
        print('学生姓名：{},身高：{},体重：{},肺活量：{},引体向上：{},立定跳远：{},50m短跑(min)：{},1000长跑(min):{},坐位体前屈(cm):{},综合成绩为：{}'.format(
            i['name'], i['tall'], i['heavy'], i['fei'], i['up'], i['jump'], i['sr'], i['lr'], i['qu'], i['sco']))
    return 0


def addInfo():
    name = input('请录入学生姓名：')
    result = counResult(name)
    scoreInfo.append(result)


def reName():
    name = input('请输入需要修改的学生姓名：')
    result = counResult(name)
    for i in range(0, len(scoreInfo)):
        if scoreInfo[i]['name'] == str(name):
            scoreInfo[i]['tall'] = result['tall']
            scoreInfo[i]['heavy'] = result['heavy']
            scoreInfo[i]['fei'] = result['fei']
            scoreInfo[i]['up'] = result['up']
            scoreInfo[i]['jump'] = result['jump']
            scoreInfo[i]['sr'] = result['sr']
            scoreInfo[i]['lr'] = result['lr']
            scoreInfo[i]['qu'] = result['qu']
            scoreInfo[i]['sco'] = result['sco']
            print('修改{}的信息成功！'.format(name))
            break
    else:
        print('修改失败！！！当前不存在当前输入的学生')


def delInfo():
    name = input('请输入需要删除的学生姓名：')
    for i in range(0, len(scoreInfo)):
        if scoreInfo[i]['name'] == str(name):
            scoreInfo.pop(i)  # 删除数组中一个数据
            print('删除{}相关信息成功！'.format(name))
            break
    else:
        print('删除失败！！！当前不存在当前输入的学生')


class MY_GUI():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("体测计算器")

        self.init_window_name.geometry('400x700+300+200')

        # 身高
        self.tall_data_label = Label(self.init_window_name, text="身高(m)")
        self.tall_data_label.grid(row=3, column=1)

        # 体重
        self.heavy_data_label = Label(self.init_window_name, text="体重(kg)")
        self.heavy_data_label.grid(row=5, column=1)

        # 肺活量
        self.fei_data_label = Label(self.init_window_name, text="肺活量(ml)")
        self.fei_data_label.grid(row=7, column=1)

        # 引体向上
        self.up_data_label = Label(self.init_window_name, text="引体向上(个)")
        self.up_data_label.grid(row=9, column=1)

        # 立定跳远
        self.jump_data_label = Label(self.init_window_name, text="立定跳远(cm)")
        self.jump_data_label.grid(row=11, column=1)

        # 50m短跑
        self.sr_data_label = Label(self.init_window_name, text="50m短跑(s)")
        self.sr_data_label.grid(row=13, column=1)

        # 1000长跑
        self.lr_data_label = Label(self.init_window_name, text="1000长跑(min)")
        self.lr_data_label.grid(row=15, column=1)

        # 坐位体前屈
        self.qu_data_label = Label(self.init_window_name, text="坐位体前屈(cm)")
        self.qu_data_label.grid(row=17, column=1)

        # 结果
        self.log_label = Label(self.init_window_name, text="结果")
        self.log_label.grid(row=19, column=1)

        # 身高 输入
        self.tall_data_Text = Text(self.init_window_name, width=60, height=2)
        self.tall_data_Text.grid(row=4, column=1, rowspan=1, columnspan=10)

        # 体重 输入
        self.heavy_data_Text = Text(self.init_window_name, width=60, height=2)
        self.heavy_data_Text.grid(row=6, column=1, columnspan=10)

        # 肺活量 输入
        self.fei_data_Text = Text(self.init_window_name, width=60, height=2)
        self.fei_data_Text.grid(row=8, column=1, columnspan=10)

        # 引体向上 输入
        self.up_data_Text = Text(self.init_window_name, width=60, height=2)
        self.up_data_Text.grid(row=10, column=1, columnspan=10)

        # 立定跳远 输入
        self.jump_data_Text = Text(self.init_window_name, width=60, height=2)
        self.jump_data_Text.grid(row=12, column=1, columnspan=10)

        # 50m短跑 输入
        self.sr_data_Text = Text(self.init_window_name, width=60, height=2)
        self.sr_data_Text.grid(row=14, column=1, columnspan=10)

        # 1000m长跑 输入
        self.lr_data_Text = Text(self.init_window_name, width=60, height=2)
        self.lr_data_Text.grid(row=16, column=1, columnspan=10)

        # 坐位体前屈 输入
        self.qu_data_Text = Text(self.init_window_name, width=60, height=2)
        self.qu_data_Text.grid(row=18, column=1, columnspan=10)

        # 计算
        self.str_button = Button(self.init_window_name, text="计算", bg="lightblue", width=10,
                                 command=self.get_result_count)  # 调用内部方法  加()为直接调用
        self.str_button.grid(row=19, column=4)

        # 结果
        self.result_data_Text = Text(self.init_window_name, width=60, height=10)  # 处理结果展示
        self.result_data_Text.grid(row=20, column=1, rowspan=10, columnspan=10)

    def get_result_count(self):
        try:
            tall = float(self.tall_data_Text.get(1.0, END).strip().replace("\n", ""))
            heavy = float(self.heavy_data_Text.get(1.0, END).strip().replace("\n", ""))
            fei = float(self.fei_data_Text.get(1.0, END).strip().replace("\n", ""))
            up = float(self.up_data_Text.get(1.0, END).strip().replace("\n", ""))
            jump = float(self.jump_data_Text.get(1.0, END).strip().replace("\n", ""))
            sr = float(self.sr_data_Text.get(1.0, END).strip().replace("\n", ""))
            lr = float(self.lr_data_Text.get(1.0, END).strip().replace("\n", ""))
            qu = float(self.qu_data_Text.get(1.0, END).strip().replace("\n", ""))

            # 肺活量成绩
            if fei < 2460:
                gfei = 10
            elif fei >= 2400 and fei < 2620:
                gfei = 20
            elif fei >= 2620 and fei < 2780:
                gfei = 30
            elif fei >= 2780 and fei < 2940:
                gfei = 40
            elif fei >= 2940 and fei < 3100:
                gfei = 50
            elif fei >= 3100 and fei < 3200:
                gfei = 60
            elif fei >= 3200 and fei < 3340:
                gfei = 62
            elif fei >= 3340 and fei < 3460:
                gfei = 64
            elif fei >= 3460 and fei < 3580:
                gfei = 66
            elif fei >= 3580 and fei < 3700:
                gfei = 68
            elif fei >= 3700 and fei < 3820:
                gfei = 70
            elif fei >= 3820 and fei < 3940:
                gfei = 72
            elif fei >= 3940 and fei < 4060:
                gfei = 74
            elif fei >= 4060 and fei < 4180:
                gfei = 76
            elif fei >= 4180 and fei < 4300:
                gfei = 78
            elif fei >= 4300 and fei < 4550:
                gfei = 80
            elif fei >= 4550 and fei < 4800:
                gfei = 85
            elif fei >= 4800 and fei < 4920:
                gfei = 90
            elif fei >= 4920 and fei < 5040:
                gfei = 95
            elif fei >= 5040:
                gfei = 100

            # 50m成绩
            if sr <= 6.7:
                gsr = 100
            elif sr > 6.7 and sr <= 6.8:
                gsr = 95
            elif sr > 6.8 and sr <= 6.9:
                gsr = 90
            elif sr > 6.9 and sr <= 7:
                gsr = 85
            elif sr > 7 and sr <= 7.1:
                gsr = 80
            elif sr > 7.1 and sr <= 7.3:
                gsr = 78
            elif sr > 7.3 and sr <= 7.5:
                gsr = 76
            elif sr > 7.5 and sr <= 7.7:
                gsr = 74
            elif sr > 7.7 and sr <= 7.9:
                gsr = 72
            elif sr > 7.9 and sr <= 8.1:
                gsr = 70
            elif sr > 8.1 and sr <= 8.3:
                gsr = 68
            elif sr > 8.3 and sr <= 8.5:
                gsr = 66
            elif sr > 8.5 and sr <= 8.7:
                gsr = 64
            elif sr > 8.7 and sr <= 8.9:
                gsr = 62
            elif sr > 8.9 and sr <= 9.1:
                gsr = 60
            elif sr > 9.1 and sr <= 9.3:
                gsr = 50
            elif sr > 9.3 and sr <= 9.5:
                gsr = 40
            elif sr > 9.5 and sr <= 9.7:
                gsr = 30
            elif sr > 9.7 and sr <= 9.9:
                gsr = 20
            elif sr > 9.9 and sr <= 10.1:
                gsr = 10
            elif sr > 10.1:
                gsr = 10

            # 1000m成绩
            if lr <= 3.17:
                glr = 100
            elif lr > 3.17 and lr <= 3.22:
                glr = 95
            elif lr > 3.22 and lr <= 3.27:
                glr = 90
            elif lr > 3.27 and lr <= 3.34:
                glr = 85
            elif lr > 3.34 and lr <= 3.42:
                glr = 80
            elif lr > 3.42 and lr <= 3.47:
                glr = 78
            elif lr > 3.47 and lr <= 3.52:
                glr = 76
            elif lr > 3.52 and lr <= 3.57:
                glr = 74
            elif lr > 3.57 and lr <= 4.02:
                glr = 72
            elif lr > 4.02 and lr <= 4.07:
                glr = 70
            elif lr > 4.07 and lr <= 4.12:
                glr = 68
            elif lr > 4.12 and lr <= 4.17:
                glr = 68
            elif lr > 4.17 and lr <= 4.22:
                glr = 66
            elif lr > 4.22 and lr <= 4.27:
                glr = 66
            elif lr > 4.27 and lr <= 4.32:
                glr = 64
            elif lr > 4.32 and lr <= 4.52:
                glr = 62
            elif lr > 4.52 and lr <= 5.12:
                glr = 60
            elif lr > 5.12 and lr <= 5.32:
                gsr = 50
            elif lr > 5.32 and lr <= 5.52:
                glr = 40
            elif lr > 5.52 and lr <= 6.12:
                glr = 30
            elif lr > 6.12:
                glr = 20

            # 坐位体前屈成绩
            if qu < -0.3:
                gqu = 10
            elif qu >= -0.3 and qu < 0.7:
                gqu = 20
            elif qu >= 0.7 and qu < 1.7:
                gqu = 30
            elif qu >= 1.7 and qu < 2.7:
                gqu = 40
            elif qu >= 2.7 and qu < 3.7:
                gqu = 50
            elif qu >= 3.7 and qu < 5.1:
                gqu = 60
            elif qu >= 5.1 and qu < 6.5:
                gqu = 62
            elif qu >= 6.5 and qu < 7.9:
                gqu = 64
            elif qu >= 7.9 and qu < 9.3:
                gqu = 66
            elif qu >= 9.3 and qu < 10.7:
                gqu = 68
            elif qu >= 10.7 and qu < 12.1:
                gfei = 70
            elif qu >= 12.1 and qu < 13.5:
                gqu = 72
            elif qu >= 13.5 and qu < 14.9:
                gqu = 74
            elif qu >= 14.9 and qu < 16.3:
                gqu = 76
            elif qu >= 16.3 and qu < 17.7:
                gqu = 78
            elif qu >= 17.7 and qu < 19.5:
                gqu = 80
            elif qu >= 19.5 and qu < 21.3:
                gqu = 85
            elif qu >= 21.3 and qu < 23.1:
                gqu = 90
            elif qu >= 23.1 and qu < 24.9:
                gqu = 95
            elif qu >= 24.9:
                gqu = 100

            # 立定跳远成绩
            if jump < 188:
                gjump = 10
            elif jump >= 188 and jump < 193:
                gjump = 20
            elif jump >= 193 and jump < 198:
                gjump = 30
            elif jump >= 198 and jump < 203:
                gjump = 40
            elif jump >= 203 and jump < 208:
                gjump = 50
            elif jump >= 208 and jump < 212:
                gjump = 60
            elif jump >= 212 and jump < 216:
                gjump = 62
            elif jump >= 216 and jump < 220:
                gjump = 64
            elif jump >= 220 and jump < 224:
                gjump = 66
            elif jump >= 224 and jump < 228:
                gjump = 68
            elif jump >= 228 and jump < 232:
                gjump = 70
            elif jump >= 232 and jump < 236:
                gjump = 72
            elif jump >= 236 and jump < 240:
                gjump = 74
            elif jump >= 240 and jump < 244:
                gjump = 76
            elif jump >= 244 and jump < 248:
                gjump = 78
            elif jump >= 248 and jump < 256:
                gjump = 80
            elif jump >= 256 and jump < 263:
                gjump = 85
            elif jump >= 263 and jump < 268:
                gjump = 90
            elif jump >= 268 and jump < 273:
                gjump = 95
            elif jump >= 273:
                gjump = 100

            # 引体向上成绩
            if up < 6:
                gup = 10
            elif up >= 6 and up < 7:
                gup = 20
            elif up >= 7 and up < 8:
                gup = 30
            elif up >= 8 and up < 9:
                gup = 40
            elif up >= 9 and up < 10:
                gup = 50
            elif up >= 10 and up < 11:
                gup = 60
            elif up >= 11 and up < 12:
                gup = 64
            elif up >= 12 and up < 13:
                gup = 68
            elif up >= 13 and up < 14:
                gup = 72
            elif up >= 14 and up < 15:
                gup = 76
            elif up >= 15 and up < 16:
                gup = 80
            elif up >= 16 and up < 17:
                gup = 85
            elif up >= 17 and up < 18:
                gup = 90
            elif up >= 18 and up < 19:
                gup = 95
            elif up >= 19 and up < 30:
                gup = 100 + (up - 19) * 10
            elif up >= 30:
                gup = 200

            # 身高体重成绩
            ht = heavy / (tall * tall)
            if ht >= 17.9 and ht <= 23.9:
                ght = 100
            elif ht <= 17.8:
                ght = 80
            elif ht >= 24 and ht <= 27.9:
                ght = 80
            elif ht >= 28:
                ght = 60

            # 总成绩
            result = (ght + gfei) * 0.15 + (gsr + glr) * 0.2 + (gqu + gjump + gup) * 0.1

            self.write_to_Text(result)
        except Exception as e:
            self.write_to_Text(result)

            # 输出结果

    def write_to_Text(self, result):
        self.result_data_Text.delete(1.0, 10.0)
        self.result_data_Text.insert(END, result)


def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()


if __name__ == '__main__':
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
                gui_start()
            elif cmdStr == '6':
                menu()
        else:
            print('再见！！')
            break
