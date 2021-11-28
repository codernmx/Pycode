import sys
import pygame
import random
import base64

# 读取加密图片和声音
def read_secret(png):
    string = b'z'
    with open(png, "r") as f:
        imgdata = base64.b64decode(f.read())
        file = open("pictures/1.png", 'wb')
        file.write(imgdata)
        file.close()
        img = pygame.image.load('pictures/1.png')
        file = open("pictures/1.png", 'wb')
        file.write(string)
        file.close()
        return img
def read_secret_sound(sound):
    string = b'z'
    with open(sound, "r") as f:
        imgdata = base64.b64decode(f.read())
        file = open("sounds/1.ogg", 'wb')
        file.write(imgdata)
        file.close()
        img = pygame.mixer.Sound('sounds/1.ogg')
        file = open("sounds/1.ogg", 'wb')
        file.write(string)
        file.close()
        return img
pygame.init()
pygame.mixer.init()
# 全局变量################################################################
font_name = pygame.font.match_font('arial')  # 定义字体
FPS = 60  # 游戏帧数
PLANEHENG, PLANESHU = 144, 110  # 己方飞机像素大小
MENUHENG, MENUSHU = 200, 50  # 开始菜单的【开始游戏，退出游戏】像素大小
HENG, SHU = 1000, 1080  # 屏幕大小
PLANESPEEDHENG, PLANESPEEDSHU = 10, 5  # 己方飞机速度
ENERYTOTAL = 15  # 当前敌机数目
PLAYERTOTAL = 0  # 当前玩家分数
BOSSLIFE = 500  # BOSS生命值
PLAYERPOWERMAX = 8  # 玩家炮弹最高等级
ENERYNEWDELAY = 200  # 敌机生成间隔
ENERYPRECENT = 1  # 敌机血量百分比
BOSSLIMIT = 700  # BOSS产生分数
SOUNDS = True  # 声音开关
PLAYER1HP, PLAYER1MP = 20, 100  # 设定四种战机血量蓝量
PLAYER2HP, PLAYER2MP = 16, 120
PLAYER3HP, PLAYER3MP = 10, 150
PLAYER4HP, PLAYER4MP = 5, 200
# 其他全局变量############################################################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (250, 128, 10)
YELLOW = (255, 255, 0)  # RGB色彩定义
SHOOTSOUND = read_secret_sound('sounds/shoot1.xml')  # 玩家射击声音
PLAYERBULLETCPS = 0  # 炮弹图片补偿
ENERYNEWNOWTIME = pygame.time.get_ticks()  # 敌机生成间隔1
ENERYNEWPRETIME = pygame.time.get_ticks()  # 敌机生成间隔2
BOSSNOW = False  # BOSS状态
heroflag = 0  # 标记战机种类
MAIN_RUN = False
CHOOSE_RUN = False
RULE_RUN = False
PAUSE_RUN = False
AGAIN_RUN = False
MENU_RUN = False#########################################################################
#共计18个函数，9个类，代码量1500

# 死亡判定函数
def death():
    global bgm
    if player1.hp <= 0:
        draw_text(screen, "GAME OVER!!!", 100, HENG / 2, SHU / 3)
        pygame.display.update()
        boomsound = read_secret_sound('sounds/boom4.xml')
        if SOUNDS is True:
            boomsound.play()
        pygame.time.wait(1000)
        bgm.stop()
        again(2)


# 通关判定函数
def though():
    global bgm
    if boss1.hp <= 0:
        draw_text(screen, "CONGRATULATIONS!!!", 80, HENG / 2, SHU / 3)
        boomsound = read_secret_sound('sounds/boom4.xml')
        if SOUNDS is True:
            boomsound.play()
        pygame.time.wait(1000)
        bgm.stop()
        again(1)


# 重置参数
def init():
    global player1, boss1, PLAYERTOTAL
    PLAYERTOTAL = 0
    lifebars.empty()
    enerys.empty()
    players.empty()
    player1 = Player()
    players.add(player1)
    playerbullets.empty()
    enerybullets.empty()
    skillbullets.empty()
    booms.empty()
    bloodupprops.empty()
    powerupprops.empty()
    mpprops.empty()
    bosses.empty()
    bossbullets.empty()
    boss1 = Boss()
    bosses.add(boss1)
    menu_sound.stop()
    menu()


# 分割加载图片函数
def load_image(filename, width, height, rows, columns, images=None):
    if images is None:
        images = []
    frame_width = width // columns
    frame_height = height // rows
    boom_picture = read_secret(filename)
    for row in range(rows):
        for col in range(columns):
            frame = boom_picture.subsurface([col * frame_width, row * frame_height, frame_width, frame_height])
            images.append(frame)
    return images


# 倒计时函数
def countdown():
    screen.fill(BLACK)
    readybackground = read_secret('pictures/backgrounds/readybackground.xml')
    screen.blit(readybackground, (0, 0))
    pygame.display.update()
    getready = read_secret_sound('sounds/getready.xml')
    if SOUNDS is True:
        getready.play()
    pygame.display.update()
    pygame.time.wait(1000)


# 显示文本函数
def draw_text(surf, text, size, x, y, COLOR = WHITE):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, COLOR)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


# 检测敌机是否过少
def newenery():
    global ENERYNEWPRETIME
    ENERYNEWNOWTIME = pygame.time.get_ticks()
    if (len(enerys) < ENERYTOTAL) and (ENERYNEWNOWTIME - ENERYNEWPRETIME > ENERYNEWDELAY):
        ENERYNEWPRETIME = pygame.time.get_ticks()
        enery = Enery()
        enerys.add(enery)


# 碰撞检测函数
def collide():
    global PLAYERTOTAL, BOSSLIFE
    a = pygame.sprite.groupcollide(enerys, playerbullets, False, False)  # 玩家子弹与敌机碰撞检测
    aa = pygame.sprite.groupcollide(playerbullets, enerys, True, False)
    if a != []:
        for i in range(len(a)):
            for i in a:
                i.hp = i.hp - len(aa)
                if i.hp <= 0:
                    PLAYERTOTAL = PLAYERTOTAL + i.score
                    boomsound = read_secret_sound('sounds/boom.xml')
                    boomsound.set_volume(5)
                    if SOUNDS is True:
                        boomsound.play()
                    i.kill()
                    boom(a, 2)
                    newprop(a)

    b = pygame.sprite.spritecollide(player1, enerys, True, pygame.sprite.collide_mask)  # 敌机与玩家碰撞检测
    player1.hp = player1.hp - len(b)
    if b != []:
        for i in b:
            i.hp = 0
            boom(b, 2)
            boomsound = read_secret_sound('sounds/boom.xml')
            boomsound.set_volume(5)
            if SOUNDS is True:
                boomsound.play()
            newprop(b)
        player1.powerlever = player1.powerlever - 2
        if player1.powerlever <= 0:
            player1.powerlever = 1

    c = pygame.sprite.spritecollide(player1, enerybullets, True, pygame.sprite.collide_mask)  # 敌机子弹与玩家碰撞检测
    player1.hp = player1.hp - len(c)
    if c != []:
        boom(c, 4)
        player1.powerlever = player1.powerlever - 1
        if player1.powerlever <= 0:
            player1.powerlever = 1

    d = pygame.sprite.groupcollide(enerybullets, playerbullets, True, True)  # 玩家子弹与敌机子弹碰撞检测
    if d != []:
        boom(d, 4)

    e = pygame.sprite.spritecollide(player1, bloodupprops, True, pygame.sprite.collide_mask)  # 加血道具与玩家碰撞检测
    if player1.hp < player1.fullhp:
        player1.hp = player1.hp + len(e)

    f = pygame.sprite.spritecollide(player1, powerupprops, True, pygame.sprite.collide_mask)  # 炮弹升级道具与玩家碰撞检测
    if f != [] and player1.powerlever < PLAYERPOWERMAX:
        player1.powerlever = player1.powerlever + 1

    g = pygame.sprite.groupcollide(bossbullets, playerbullets, True, True)  # BOSS子弹与玩家子弹碰撞检测
    if g != []:
        boom(g, 4)

    if BOSSNOW is True:
        h = pygame.sprite.spritecollide(boss1, playerbullets, True, pygame.sprite.collide_mask)  # BOSS与玩家子弹碰撞检测
        if h != []:
            boss1.hp = boss1.hp - len(h)
            boom(h, 3)

    i = pygame.sprite.spritecollide(player1, bossbullets, True, pygame.sprite.collide_mask)  # BOSS子弹与玩家碰撞检测
    if i != []:
        player1.hp = player1.hp - len(i)
        boom(i, 4)
        player1.powerlever = player1.powerlever - 1
        if player1.powerlever <= 1:
            player1.powerlever = 1

    j = pygame.sprite.groupcollide(enerys, skillbullets, True, False)  # 技能子弹与敌机碰撞检测
    if g != []:
        for i in j:
            i.hp = 0
            if i.hp <= 0:
                i.kill()
                PLAYERTOTAL = PLAYERTOTAL + 1
                boom(j, 2)
                boomsound = read_secret_sound('sounds/boom.xml')
                boomsound.set_volume(5)
                if SOUNDS is True:
                    boomsound.play()
                newprop(j)

    k = pygame.sprite.groupcollide(enerybullets, skillbullets, True, False)  # 技能子弹与敌机子弹碰撞检测
    if k != []:
        boom(k, 4)

    if BOSSNOW == True:
        l = pygame.sprite.spritecollide(boss1, skillbullets, False)  # BOSS与技能子弹碰撞检测
        if l != []:
            boss1.hp = boss1.hp - len(l) * 1
            boom(l, 4)
    m = pygame.sprite.spritecollide(player1, mpprops, True, pygame.sprite.collide_mask)  # 回复蓝量道具与玩家碰撞检测
    if m != []:
        player1.mp = player1.mp + 20
        if player1.mp > player1.fullmp:
            player1.mp = player1.fullmp


# 生成道具
propnowtime = proppretime = pygame.time.get_ticks()
def newprop(a):
    global propnowtime, proppretime
    propnowtime = pygame.time.get_ticks()
    if propnowtime - proppretime > 2000:
        flag = random.randint(1, 3)
        if flag == 1 and len(bloodupprops) < 3:
            for i in a:
                prop = Prop(1)
                prop.setpos(i.rect.center)
                bloodupprops.add(prop)
        elif flag == 2 and len(powerupprops) < 2:
            for i in a:
                prop = Prop(2)
                prop.setpos(i.rect.center)
                powerupprops.add(prop)
        elif flag == 3 and len(mpprops) < 2:
            for i in a:
                prop = Prop(3)
                prop.setpos(i.rect.center)
                mpprops.add(prop)
        proppretime = pygame.time.get_ticks()


# 爆炸生成
def boom(spr, flag):
    for i in spr:
        boom = Boom(flag)
        boom.setpos(i.rect.center)
        booms.add(boom)


# 绘制血条与蓝条
def drawplayerlife():
    draw_text(screen, "Your Score is: " + str(PLAYERTOTAL), 30, HENG / 2, 10)
    pygame.draw.rect(screen, RED, (800, 1050, 200, 10), 1)
    pygame.draw.rect(screen, BLUE, (800, 1060, 200, 10), 1)
    pygame.draw.rect(screen, ORANGE, (800, 1045, 200, 5), 1)
    pygame.draw.rect(screen, ORANGE, (800, 1045, player1.charge / player1.fullcharge * 1.0 * 200, 5), 0)
    pygame.draw.rect(screen, RED, (800, 1050, player1.hp / player1.fullhp * 1.0 * 200, 10), 0)
    pygame.draw.rect(screen, BLUE, (800, 1060, player1.mp / player1.fullmp * 1.0 * 200, 10), 0)
    draw_text(screen, str(player1.hp) + "/" + str(player1.fullhp), 10, 780, 1048)
    draw_text(screen, str(player1.mp) + "/" + str(player1.fullmp), 10, 780, 1060)


# 游戏难度递增函数
def leverup():
    global PLAYERTOTAL, ENERYTOTAL, ENERYNEWDELAY, ENERYPRECENT
    if PLAYERTOTAL > 0:
        ENERYTOTAL = 25
        ENERYNEWDELAY = 150
        ENERYPRECENT = 1
    if PLAYERTOTAL > 300:
        ENERYTOTAL = 26
        ENERYNEWDELAY = 150
        ENERYPRECENT = 1.5
    if PLAYERTOTAL > 500:
        ENERYTOTAL = 30
        ENERYNEWDELAY = 100
        ENERYPRECENT = 2
    if PLAYERTOTAL > 700:
        ENERYTOTAL = 15
        ENERYNEWDELAY = 150
        ENERYPRECENT = 2.5


# 界面函数
def menu():
    pygame.mouse.set_visible(True)
    global menu_sound, MAIN_RUN, CHOOSE_RUN, RULE_RUN, PAUSE_RUN, AGAIN_RUN, MENU_RUN
    MAIN_RUN = False
    CHOOSE_RUN = False
    RULE_RUN = False
    PAUSE_RUN = False
    AGAIN_RUN = False
    MENU_RUN = True
    if SOUNDS is True:
        menu_sound.play(-1)
    menu = read_secret('pictures/backgrounds/logobackground.xml')
    screen.blit(menu, (0, 0))
    startimage = read_secret('pictures/buttons/startgame.xml')
    quitimage = read_secret('pictures/buttons/quitgame.xml')
    ruleimage = read_secret('pictures/buttons/rule.xml')
    screen.blit(startimage, (400, SHU - 300))
    screen.blit(quitimage, (400, SHU - 200))
    screen.blit(ruleimage, (400, SHU - 100))
    pygame.display.update()
    while MENU_RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 400) and (event.pos[0] < 600) and (event.pos[1] > 780) and (event.pos[1] < 830):
                    screen.blit(startimage, (400 + 2, SHU - 300 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    choose()
                elif (event.pos[0] > 400) and (event.pos[0] < 600) and (event.pos[1] > 880) and (event.pos[1] < 930):
                    screen.blit(quitimage, (400 + 2, SHU - 200 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    pygame.quit()
                    quit()
                elif (event.pos[0] > 400) and (event.pos[0] < 600) and (event.pos[1] > 980) and (event.pos[1] < 1030):
                    screen.blit(ruleimage, (400 + 2, SHU - 100 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    rule()
            key_press = pygame.key.get_pressed()  # 读取键盘输入
            if key_press[pygame.K_ESCAPE]:
                pygame.quit()
                quit()


# 选择战机界面
def choose():
    pygame.mouse.set_visible(True)
    global PLAYERBULLETCPS, SHOOTSOUND, PLAYERWHO, heroflag, PLAYERBULLETIMG, PLAYER1HP, PLAYER1MP, PLAYER2HP, \
        PLAYER2MP, PLAYER3HP, PLAYER3MP, PLAYER4HP, PLAYER4MP, MAIN_RUN, CHOOSE_RUN, RULE_RUN, PAUSE_RUN, AGAIN_RUN, MENU_RUN
    MAIN_RUN = False
    CHOOSE_RUN = True
    RULE_RUN = False
    PAUSE_RUN = False
    AGAIN_RUN = False
    MENU_RUN = False
    playerimg1x = 56
    playerimg2x = 292
    playerimg3x = 528
    playerimg4x = 764
    y = 750
    selx = 180
    sely = 190
    hero1 = read_secret('pictures/hero/planeselect1.xml')
    hero2 = read_secret('pictures/hero/planeselect2.xml')
    hero3 = read_secret('pictures/hero/planeselect3.xml')
    hero4 = read_secret('pictures/hero/planeselect4.xml')
    selectimg = read_secret('pictures/hero/plane_sel.xml')
    back = read_secret('pictures/buttons/back.xml')
    background = read_secret('pictures/backgrounds/choosebackground.xml')
    go = read_secret('pictures/buttons/go.xml')
    show = read_secret('pictures/hero/show.xml')
    selectimgx = playerimg1x
    heroflag = 1
    while CHOOSE_RUN:
        if heroflag == 1:
            choosebackground = read_secret('pictures/hero/hero1.xml')
            screen.blit(background, (0, 0))
            screen.blit(choosebackground, (212, 500))
            draw_text(screen, " × " + str(PLAYER1HP), 20, 870, 260, RED)
            draw_text(screen, " × " + str(PLAYER1MP), 20, 870, 310, BLUE)
        elif heroflag == 2:
            choosebackground = read_secret('pictures/hero/hero2.xml')
            screen.blit(background, (0, 0))
            screen.blit(choosebackground, (212, 500))
            draw_text(screen, " × " + str(PLAYER2HP), 20, 870, 260, RED)
            draw_text(screen, " × " + str(PLAYER2MP), 20, 870, 310, BLUE)
        elif heroflag == 3:
            choosebackground = read_secret('pictures/hero/hero3.xml')
            screen.blit(background, (0, 0))
            screen.blit(choosebackground, (212, 500))
            draw_text(screen, " × " + str(PLAYER3HP), 20, 870, 260, RED)
            draw_text(screen, " × " + str(PLAYER3MP), 20, 870, 310, BLUE)
        elif heroflag == 4:
            choosebackground = read_secret('pictures/hero/hero4.xml')
            screen.blit(background, (0, 0))
            screen.blit(choosebackground, (75, 300))
            draw_text(screen, " × " + str(PLAYER4HP), 20, 870, 260, RED)
            draw_text(screen, " × " + str(PLAYER4MP), 20, 870, 310, BLUE)
        screen.blit(back, (50, 1000))
        screen.blit(go, (750, 1000))
        if heroflag == 1:
            selectimgx = playerimg1x
        elif heroflag == 2:
            selectimgx = playerimg2x
        elif heroflag == 3:
            selectimgx = playerimg3x
        elif heroflag == 4:
            selectimgx = playerimg4x
        screen.blit(show, (800, 240))
        screen.blit(hero1, (playerimg1x, y))
        screen.blit(hero2, (playerimg2x, y))
        screen.blit(hero3, (playerimg3x, y))
        screen.blit(hero4, (playerimg4x, y))
        screen.blit(selectimg, (selectimgx - 10, y - 10))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > playerimg1x) and (event.pos[0] < playerimg1x + selx) and (
                        event.pos[1] > y + 50) and (event.pos[1] < y + sely - 50):
                    heroflag = 1
                elif (event.pos[0] > playerimg2x) and (event.pos[0] < playerimg2x + selx) and (
                        event.pos[1] > y + 50) and (event.pos[1] < y + sely - 50):
                    heroflag = 2
                elif (event.pos[0] > playerimg3x) and (event.pos[0] < playerimg3x + selx) and (
                        event.pos[1] > y + 50) and (event.pos[1] < y + sely - 50):
                    heroflag = 3
                elif (event.pos[0] > playerimg4x) and (event.pos[0] < playerimg4x + selx) and (event.pos[1] > y) and (
                        event.pos[1] < y + sely):
                    heroflag = 4
                elif (event.pos[0] > 750) and (event.pos[0] < 950) and (event.pos[1] > 1000) and (event.pos[1] < 1050):
                    screen.blit(go, (750 + 2, 1000 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    if heroflag == 1:
                        player1.load_image('pictures/hero/hero1.xml', 576, 110, 1, 4, HENG / 2, 950)
                        PLAYERBULLETIMG = load_image('pictures/hero/bullet1.xml', 228, 52, 1, 4)
                        SHOOTSOUND = read_secret_sound('sounds/shoot1.xml')
                        player1.sethpmp(PLAYER1HP, PLAYER1MP)
                        PLAYERBULLETCPS = 0
                        start()
                    elif heroflag == 2:
                        player1.load_image('pictures/hero/hero2.xml', 576, 110, 1, 4, HENG / 2, 950)
                        PLAYERBULLETIMG = load_image('pictures/hero/bullet2.xml', 228, 54, 1, 4)
                        SHOOTSOUND = read_secret_sound('sounds/shoot2.xml')
                        player1.sethpmp(PLAYER2HP, PLAYER2MP)
                        PLAYERBULLETCPS = 0
                        start()
                    elif heroflag == 3:
                        player1.load_image('pictures/hero/hero3.xml', 576, 110, 1, 4, HENG / 2, 950)
                        PLAYERBULLETIMG = load_image('pictures/hero/bullet3.xml', 228, 78, 1, 4)
                        SHOOTSOUND = read_secret_sound('sounds/shoot3.xml')
                        SHOOTSOUND.set_volume(5)
                        PLAYERBULLETCPS = 0
                        player1.sethpmp(PLAYER3HP, PLAYER3MP)
                        start()
                    elif heroflag == 4:
                        player1.load_image('pictures/hero/hero4.xml', 850, 400, 2, 5, HENG / 2, 950, 1)
                        PLAYERBULLETIMG = load_image('pictures/hero/bullet4.xml', 228, 77, 1, 4)
                        PLAYERBULLETCPS = 15
                        SHOOTSOUND = read_secret_sound('sounds/shoot4.xml')
                        SHOOTSOUND.set_volume(0.5)
                        player1.sethpmp(PLAYER4HP, PLAYER4MP)
                        start()
                elif (event.pos[0] > 50) and (event.pos[0] < 250) and (event.pos[1] > 1000) and (event.pos[1] < 1050):
                    screen.blit(back, (50 + 2, 1000 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    menu_sound.stop()
                    menu()


# 再来一次界面
def again(flag):
    pygame.mouse.set_visible(True)
    global BOSSNOW, MAIN_RUN, CHOOSE_RUN, RULE_RUN, PAUSE_RUN, AGAIN_RUN, MENU_RUN, screen
    screen = pygame.display.set_mode((HENG, SHU), pygame.FULLSCREEN)
    MAIN_RUN = False
    CHOOSE_RUN = False
    RULE_RUN = False
    PAUSE_RUN = False
    AGAIN_RUN = True
    MENU_RUN = False
    BOSSNOW = False
    againbackground = None
    if flag == 1:
        againbackground = read_secret('pictures/backgrounds/again1.xml')
    elif flag == 2:
        againbackground = read_secret('pictures/backgrounds/again2.xml')
    again = read_secret('pictures/buttons/again.xml')
    quitgame = read_secret('pictures/buttons/quitgame.xml')
    while AGAIN_RUN:
        screen.blit(againbackground, (0, 0))
        screen.blit(again, (750, 1000))
        screen.blit(quitgame, (50, 1000))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 750) and (event.pos[0] < 950) and (event.pos[1] > 1000) and (event.pos[1] < 1050):
                    screen.blit(again, (750 + 2, 1000 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    init()
                elif (event.pos[0] > 50) and (event.pos[0] < 250) and (event.pos[1] > 1000) and (event.pos[1] < 1050):
                    screen.blit(quitgame, (50 + 2, 1000 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    pygame.quit()
                    quit()


# 暂停界面
def pause():
    pygame.mouse.set_visible(True)
    global bgm, MAIN_RUN, CHOOSE_RUN, RULE_RUN, PAUSE_RUN, AGAIN_RUN, MENU_RUN, screen
    screen = pygame.display.set_mode((HENG, SHU), pygame.FULLSCREEN)
    MAIN_RUN = False
    CHOOSE_RUN = False
    RULE_RUN = False
    PAUSE_RUN = True
    AGAIN_RUN = False
    MENU_RUN = False
    bgm.stop()
    pausewrite = read_secret('pictures/backgrounds/pausebg/pause.xml')
    pausebackground = read_secret('pictures/backgrounds/pausebg/pause1.xml')
    conti = read_secret('pictures/buttons/continue.xml')
    quitgame = read_secret('pictures/buttons/quitgame.xml')
    again = read_secret('pictures/buttons/again.xml')
    flag = random.randint(1, 5)
    if flag == 1:
        pausebackground = read_secret('pictures/backgrounds/pausebg/pause1.xml')
    elif flag == 2:
        pausebackground = read_secret('pictures/backgrounds/pausebg/pause2.xml')
    elif flag == 3:
        pausebackground = read_secret('pictures/backgrounds/pausebg/pause3.xml')
    elif flag == 4:
        pausebackground = read_secret('pictures/backgrounds/pausebg/pause4.xml')
    elif flag == 5:
        pausebackground = read_secret('pictures/backgrounds/pausebg/pause5.xml')
    while PAUSE_RUN:
        screen.blit(pausebackground, (0, 0))
        screen.blit(pausewrite, (0, 0))
        screen.blit(again, (400, 1000))
        screen.blit(conti, (750, 1000))
        screen.blit(quitgame, (50, 1000))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > 750) and (event.pos[0] < 950) and (event.pos[1] > 1000) and (event.pos[1] < 1050):
                    screen.blit(conti, (750 + 2, 1000 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    start()
                elif (event.pos[0] > 400) and (event.pos[0] < 600) and (event.pos[1] > 1000) and (event.pos[1] < 1050):
                    screen.blit(again, (400 + 2, 1000 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    init()
                elif (event.pos[0] > 50) and (event.pos[0] < 250) and (event.pos[1] > 1000) and (event.pos[1] < 1050):
                    screen.blit(quitgame, (50 + 2, 1000 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    pygame.quit()
                    quit()


# 规则界面
def rule():
    pygame.mouse.set_visible(True)
    global MAIN_RUN, CHOOSE_RUN, RULE_RUN, PAUSE_RUN, AGAIN_RUN, MENU_RUN, menu_sound
    MAIN_RUN = False
    CHOOSE_RUN = False
    RULE_RUN = True
    PAUSE_RUN = False
    AGAIN_RUN = False
    MENU_RUN = False
    img1 = 750
    screen.fill(BLACK)
    rulebackground = read_secret('pictures/backgrounds/rulebackground.xml')
    back = read_secret('pictures/buttons/back.xml')
    screen.blit(rulebackground, (0, 0))
    screen.blit(back, (img1, SHU - 80))
    pygame.display.update()
    while RULE_RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0] > img1) and (event.pos[0] < img1 + MENUHENG) and (event.pos[1] > SHU - 80) and \
                        (event.pos[1] < SHU - 80 + MENUSHU):
                    screen.blit(back, (img1 + 2, SHU - 80 + 2))
                    pygame.display.update()
                    pygame.time.wait(200)
                    menu_sound.stop()
                    menu()


# 游戏主循环
def start():
    global BOSSNOW, timepre, menu_sound, bgm, MAIN_RUN, CHOOSE_RUN, RULE_RUN, PAUSE_RUN, AGAIN_RUN, MENU_RUN, screen
    ruleright = read_secret('pictures/backgrounds/rule.xml')
    rulewrite = read_secret('pictures/backgrounds/rulewrite.xml')
    MAIN_RUN = False
    CHOOSE_RUN = False
    RULE_RUN = False
    PAUSE_RUN = False
    AGAIN_RUN = False
    MENU_RUN = True
    menu_sound.stop()
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    if SOUNDS is True:
        bgm.play(-1)
    countdown()  # 倒计时进入
    screen = pygame.display.set_mode((1500, SHU), pygame.FULLSCREEN)
    while MENU_RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        key_press = pygame.key.get_pressed()  # 读取键盘输入
        if key_press[pygame.K_p]:
            pause()
        player1.move(key_press)  # 键盘交互函数
        collide()  # 碰撞检测
        screen.fill(BLACK)
        backgrounds.update()
        backgrounds.draw(screen)
        leverup()
        if BOSSNOW is False and PLAYERTOTAL > BOSSLIMIT:  # 判断是否生成BOSS
            boss1.show = True
            BOSSNOW = True
        newenery()
        enerys.update()  # 敌机绘制
        enerys.draw(screen)
        players.update()
        playerbullets.update()  # 子弹绘制
        playerbullets.draw(screen)
        skillbullets.update()
        skillbullets.draw(screen)
        enerybullets.update()
        enerybullets.draw(screen)
        booms.update()  # 爆炸绘制
        booms.draw(screen)
        bloodupprops.update()  # 道具绘制
        bloodupprops.draw(screen)
        powerupprops.update()
        powerupprops.draw(screen)
        mpprops.update()
        mpprops.draw(screen)
        bosses.update()
        bosses.draw(screen)
        bossbullets.update()
        bossbullets.draw(screen)
        lifebars.update()
        lifebars.draw(screen)
        drawplayerlife()
        player1.draw(screen)  # 玩家绘制
        screen.blit(ruleright, (1000, 0))
        screen.blit(rulewrite, (1000, 0))
        pygame.display.update()
        clock.tick(FPS)  # 帧数
        death()  # 死亡判定
        though()  # 通关判定


# 背景地图类
class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = read_secret('pictures/backgrounds/background1.xml')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 3
    def update(self):
        global BACKGROUNDNUM
        self.rect.y = self.rect.y + self.speed
        if self.rect.y == 1080:
            self.rect.y = -4920

    def setpos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# 血条类
class Lifebar(pygame.sprite.Sprite):
    def __init__(self, who, flag):  # flag代表血条是 1 BOSS 2 敌机
        pygame.sprite.Sprite.__init__(self)
        self.flag = flag
        self.who = who
        self.oldpercent = 0
        self.image = pygame.Surface((self.who.rect.width, 12))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        if self.flag == 1:
            self.color = ORANGE
            self.wid = 10
        elif self.flag == 2:
            self.color = YELLOW
            self.wid = 2

    def draw(self, screen):
        pygame.draw.rect(self.image, (0, 255, 0), (0, 0, self.who.rect.width, self.wid), 1)
        self.rect = self.image.get_rect()
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.percent = self.who.hp / self.who.fullhp * 1.0
        if self.percent != self.oldpercent:
            pygame.draw.rect(self.image, BLACK, (1, 1, self.who.rect.width - 1, self.wid), 0)
            pygame.draw.rect(self.image, self.color, (1, 1, int(self.who.rect.width * self.percent), self.wid), 0)
        self.oldpercent = self.percent
        self.rect.centerx = self.who.rect.centerx
        self.rect.centery = self.who.rect.centery - self.who.rect.height / 2 - 10
        if self.who.hp < 1 or self.who.rect.y > SHU:
            self.kill()


# BOSS类
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = read_secret('pictures/bosses/boss1.xml')
        self.rect = self.image.get_rect()
        self.rect.x = HENG / 3
        self.rect.y = -200
        self.mask = pygame.mask.from_surface(self.image)
        self.nowtime = self.pretime = pygame.time.get_ticks()
        self.speedx = 2
        self.bulletkind = 0
        self.show = False
        self.hp = BOSSLIFE
        self.fullhp = BOSSLIFE
        lifebar = Lifebar(self, 1)
        lifebars.add(lifebar)

    def update(self):
        if self.show is True:
            if self.rect.y < 100:
                self.rect.y = self.rect.y + 5
            else:
                self.rect.x = self.rect.x + self.speedx
            if self.rect.x > HENG - 326:
                self.speedx = -self.speedx
            elif self.rect.x < 0:
                self.speedx = -self.speedx
            self.shoot()

    def bulletchoose(self):
        flag = random.randint(1, 5)
        if flag == 1 or flag == 4 or flag == 5:
            for i in range(11):
                bullet = Bullet(3)
                j = random.randint(1, 8)
                if j == 1:
                    bullet.load_image('pictures/bosses/bossbullet/0-0.xml', 72, 36, 1, 2)
                elif j == 2:
                    bullet.load_image('pictures/bosses/bossbullet/0-1.xml', 72, 36, 1, 2)
                elif j == 3:
                    bullet.load_image('pictures/bosses/bossbullet/0-2.xml', 72, 36, 1, 2)
                elif j == 4:
                    bullet.load_image('pictures/bosses/bossbullet/0-3.xml', 72, 36, 1, 2)
                elif j == 5:
                    bullet.load_image('pictures/bosses/bossbullet/0-4.xml', 72, 36, 1, 2)
                elif j == 6:
                    bullet.load_image('pictures/bosses/bossbullet/0-5.xml', 72, 36, 1, 2)
                elif j == 7:
                    bullet.load_image('pictures/bosses/bossbullet/0-6.xml', 72, 36, 1, 2)
                elif j == 8:
                    bullet.load_image('pictures/bosses/bossbullet/0-7.xml', 72, 36, 1, 2)
                bullet.setpos(self.rect.x + 150, self.rect.y + 100)
                bullet.setspeedxy(i - 6, 5)
                bossbullets.add(bullet)
        elif flag == 2:
            for k in range(6):
                bullet1 = Bullet(3)
                l = random.randint(1, 3)
                if l == 1:
                    bullet1.load_image('pictures/bosses/bossbullet/1-1.xml', 180, 65, 1, 3)
                elif l == 2:
                    bullet1.load_image('pictures/bosses/bossbullet/1-2.xml', 180, 65, 1, 3)
                elif l == 3:
                    bullet1.load_image('pictures/bosses/bossbullet/1-3.xml', 180, 65, 1, 3)
                bullet1.setpos(self.rect.x + 50, self.rect.y + 90, True)
                bullet1.setspeedxy(random.randint(-5, 5), random.randint(2, 5))
                bullet1.setdelay(200)
                bossbullets.add(bullet1)
            for k in range(6):
                bullet1 = Bullet(3)
                l = random.randint(1, 3)
                if l == 1:
                    bullet1.load_image('pictures/bosses/bossbullet/1-1.xml', 180, 65, 1, 3)
                elif l == 2:
                    bullet1.load_image('pictures/bosses/bossbullet/1-2.xml', 180, 65, 1, 3)
                elif l == 3:
                    bullet1.load_image('pictures/bosses/bossbullet/1-3.xml', 180, 65, 1, 3)
                bullet1.setpos(self.rect.x + 220, self.rect.y + 90, True)
                bullet1.setspeedxy(random.randint(-5, 5), random.randint(2, 5))
                bullet1.setdelay(200)
                bossbullets.add(bullet1)
        elif flag == 3:
            for m in range(10):
                bullet = Bullet(3)
                bullet.load_image('pictures/bosses/bossbullet/3-1.xml', 60, 93, 1, 2)
                bullet.setpos(self.rect.x + m * 30 + 20, self.rect.y + 120)
                bullet.setspeedxy(0, 10)
                bullet.setdelay(1000)
                bossbullets.add(bullet)

    def shoot(self):
        self.nowtime = pygame.time.get_ticks()
        if (self.nowtime - self.pretime) > random.randint(1000, 2000):
            self.bulletchoose()
            self.pretime = pygame.time.get_ticks()
        else:
            pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.rect = None
        self.image = None
        self.mask = None
        self.last_time = pygame.time.get_ticks()
        self.frame = 0
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.nowtime1 = self.pretime1 = pygame.time.get_ticks()
        self.powerlever = 1
        self.shootdelay = 300
        self.hp = 20
        self.fullhp = 20
        self.mp = 100
        self.fullmp = 100
        self.flag = 0
        self.rate = 100
        self.skillmp = 50
        self.charge = self.fullcharge = 300

    def sethpmp(self, hp, mp):
        self.hp = self.fullhp = hp
        self.mp = self.fullmp = mp

    def move(self, key_press):
        if key_press[pygame.K_SPACE]:
            self.shoot()
        if key_press[pygame.K_UP]:
            self.rect.y = self.rect.y - PLANESPEEDSHU * 2
        if key_press[pygame.K_DOWN]:
            self.rect.y = self.rect.y + PLANESPEEDSHU
        if key_press[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + PLANESPEEDHENG
        if key_press[pygame.K_LEFT]:
            self.rect.x = self.rect.x - PLANESPEEDHENG
        if key_press[pygame.K_z]:
            self.skill()
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > HENG - PLANEHENG:
            self.rect.x = HENG - PLANEHENG
        if self.rect.y < 450:
            self.rect.y = 450
        if self.rect.y > SHU - PLANESHU:
            self.rect.y = SHU - PLANESHU

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def power(self, powerlever):
        if powerlever == 1:
            bullet = Bullet(1)
            bullet.setpos(self.shootx, self.shooty)
            playerbullets.add(bullet)
            self.shootdelay = 300
        elif powerlever == 2:
            bullet1 = Bullet(1)
            bullet2 = Bullet(1)
            bullet1.setpos(self.shootx - 15, self.shooty)
            bullet2.setpos(self.shootx + 15, self.shooty)
            playerbullets.add(bullet1, bullet2)
            self.shootdelay = 300
        elif powerlever == 3:
            bullet1 = Bullet(1)
            bullet2 = Bullet(1)
            bullet3 = Bullet(1)
            bullet1.setpos(self.shootx - 30, self.shooty)
            bullet2.setpos(self.shootx, self.shooty)
            bullet3.setpos(self.shootx + 30, self.shooty)
            playerbullets.add(bullet1, bullet2, bullet3)
            self.shootdelay = 300
        elif powerlever == 4:
            bullet1 = Bullet(1)
            bullet2 = Bullet(1)
            bullet3 = Bullet(1)
            bullet4 = Bullet(1)
            bullet1.setpos(self.shootx - 15, self.shooty)
            bullet2.setpos(self.shootx + 15, self.shooty)
            bullet3.setpos(self.shootx + 45, self.shooty)
            bullet4.setpos(self.shootx - 45, self.shooty)
            playerbullets.add(bullet1, bullet2, bullet3, bullet4)
            self.shootdelay = 400
        elif powerlever == 5:
            bullet1 = Bullet(1)
            bullet2 = Bullet(1)
            bullet3 = Bullet(1)
            bullet4 = Bullet(1)
            bullet5 = Bullet(1)
            bullet1.setpos(self.shootx, self.shooty)
            bullet2.setpos(self.shootx - 60, self.shooty + 40)
            bullet3.setpos(self.shootx + 60, self.shooty + 40)
            bullet4.setpos(self.shootx + 30, self.shooty + 20)
            bullet5.setpos(self.shootx - 30, self.shooty + 20)
            playerbullets.add(bullet1, bullet2, bullet3, bullet4, bullet5)
            self.shootdelay = 500
        elif powerlever == 6:
            bullet1 = Bullet(1)
            bullet2 = Bullet(1)
            bullet3 = Bullet(1)
            bullet4 = Bullet(1)
            bullet5 = Bullet(1)
            bullet6 = Bullet(1)
            bullet1.setpos(self.shootx + 15, self.shooty)
            bullet2.setpos(self.shootx - 15, self.shooty)
            bullet3.setpos(self.shootx + 45, self.shooty + 10)
            bullet3.setspeedxy(+1, -10)
            bullet4.setpos(self.shootx - 45, self.shooty + 10)
            bullet4.setspeedxy(-1, -10)
            bullet5.setpos(self.shootx + 75, self.shooty + 20)
            bullet5.setspeedxy(+2, -10)
            bullet6.setpos(self.shootx - 75, self.shooty + 20)
            bullet6.setspeedxy(-2, -10)
            playerbullets.add(bullet1, bullet2, bullet3, bullet4, bullet5, bullet6)
            self.shootdelay = 600
        elif powerlever == 7:
            bullet1 = Bullet(1)
            bullet2 = Bullet(1)
            bullet3 = Bullet(1)
            bullet4 = Bullet(1)
            bullet5 = Bullet(1)
            bullet6 = Bullet(1)
            bullet7 = Bullet(1)
            bullet8 = Bullet(1)
            bullet1.setpos(self.shootx + 15, self.shooty)
            bullet2.setpos(self.shootx - 15, self.shooty)
            bullet3.setpos(self.shootx + 45, self.shooty + 10)
            bullet3.setspeedxy(+1, -10)
            bullet4.setpos(self.shootx - 45, self.shooty + 10)
            bullet4.setspeedxy(-1, -10)
            bullet5.setpos(self.shootx + 75, self.shooty + 20)
            bullet5.setspeedxy(+2, -10)
            bullet6.setpos(self.shootx - 75, self.shooty + 20)
            bullet6.setspeedxy(-2, -10)
            bullet7.setpos(self.shootx + 15, self.shooty + 40)
            bullet8.setpos(self.shootx - 15, self.shooty + 40)
            playerbullets.add(bullet1, bullet2, bullet3, bullet4, bullet5, bullet6, bullet7, bullet8)
            self.shootdelay = 650
        elif powerlever == 8:
            bullet1 = Bullet(1)
            bullet2 = Bullet(1)
            bullet3 = Bullet(1)
            bullet4 = Bullet(1)
            bullet5 = Bullet(1)
            bullet6 = Bullet(1)
            bullet7 = Bullet(1)
            bullet8 = Bullet(1)
            bullet9 = Bullet(1)
            bullet10 = Bullet(1)
            bullet11 = Bullet(1)
            bullet12 = Bullet(1)
            bullet1.setpos(self.shootx + 15, self.shooty)
            bullet2.setpos(self.shootx - 15, self.shooty)
            bullet3.setpos(self.shootx + 45, self.shooty + 10)
            bullet3.setspeedxy(+1, -10)
            bullet4.setpos(self.shootx - 45, self.shooty + 10)
            bullet4.setspeedxy(-1, -10)
            bullet5.setpos(self.shootx + 75, self.shooty + 20)
            bullet5.setspeedxy(+2, -10)
            bullet6.setpos(self.shootx - 75, self.shooty + 20)
            bullet6.setspeedxy(-2, -10)
            bullet7.setpos(self.shootx + 15, self.shooty + 40)
            bullet8.setpos(self.shootx - 15, self.shooty + 40)
            bullet9.setpos(self.shootx + 45, self.shooty + 50)
            bullet9.setspeedxy(+1, -10)
            bullet10.setpos(self.shootx - 45, self.shooty + 50)
            bullet10.setspeedxy(-1, -10)
            bullet11.setpos(self.shootx + 75, self.shooty + 60)
            bullet11.setspeedxy(+2, -10)
            bullet12.setpos(self.shootx - 75, self.shooty + 60)
            bullet12.setspeedxy(-2, -10)
            playerbullets.add(bullet1, bullet2, bullet3, bullet4, bullet5, bullet6, bullet7, bullet8, bullet9, bullet10,
                              bullet11, bullet12)
            self.shootdelay = 700

    def shoot(self):
        self.nowtime1 = pygame.time.get_ticks()
        self.shootx = self.rect.x + PLANEHENG / 2 - 30 + PLAYERBULLETCPS
        self.shooty = self.rect.y
        if (self.nowtime1 - self.pretime1) > self.shootdelay:
            shootsound = SHOOTSOUND
            if SOUNDS is True:
                shootsound.play()
            self.power(self.powerlever)
            self.pretime1 = pygame.time.get_ticks()
        else:
            pass

    def skillpower(self):
        global PLAYERBULLETTCP
        skillbullet1 = Skillbullet(heroflag)
        if heroflag == 2:
            skillbullet1.setpos(self.shootx - 100, self.shooty + 200)
        else:
            skillbullet1.setpos(self.shootx - 150 + PLAYERBULLETCPS, self.shooty + 200)
        skillbullets.add(skillbullet1)

    def skill(self):
        self.shootx = self.rect.x + PLANEHENG / 2 - 30 + PLAYERBULLETCPS * 3
        self.shooty = self.rect.y
        if self.charge >= self.fullcharge and self.mp >= self.skillmp:
            self.skillpower()
            self.mp = self.mp - self.skillmp
            self.charge = 0
        else:
            pass

    def load_image(self, filename, width, height, rows, columns, x, y, flag=0):
        self.flag = flag
        frame_width = width // columns
        frame_height = height // rows
        self.boom_picture = read_secret(filename)
        for row in range(rows):
            for col in range(columns):
                frame = self.boom_picture.subsurface([col * frame_width, row * frame_height, frame_width, frame_height])
                self.images.append(frame)
        self.image = self.images[0]
        self.last_frame = rows * columns - 1
        self.rect = self.images[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.flag == 0:
            if self.powerlever == 1 or self.powerlever == 2:
                self.image = self.images[0]
            elif self.powerlever == 3 or self.powerlever == 4:
                self.image = self.images[1]
            elif self.powerlever == 5 or self.powerlever == 6 or self.powerlever == 7:
                self.image = self.images[2]
            elif self.powerlever == 8:
                self.image = self.images[3]
        else:
            current_time = pygame.time.get_ticks()
            if current_time > self.last_time + self.rate:
                self.last_time = current_time
                self.image = self.images[self.frame]
                self.frame += 1
                if self.frame > self.last_frame:
                    self.frame = 1
        self.charge += 1
        if self.charge > self.fullcharge:
            self.charge = self.fullcharge


# 敌方飞机类
class Enery(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        flag = random.randint(1, 4)  # 敌机种类
        self.speed = random.randint(5, 10)
        self.shootflag = 1  # 是否能射击 1能
        if PLAYERTOTAL <= 100:
            flag = random.randint(1, 4)
        elif (PLAYERTOTAL > 100) and (PLAYERTOTAL <= 200):
            flag = random.randint(2, 5)
        elif (PLAYERTOTAL > 200) and (PLAYERTOTAL <= 500):
            flag = random.randint(1, 6)
        elif (PLAYERTOTAL > 500) and (PLAYERTOTAL <= 700):
            flag = random.randint(3, 7)
        elif PLAYERTOTAL > 700:
            flag = random.randint(4, 9)
        if flag == 1:
            self.image = read_secret('pictures/enemys/enemy1.xml')
            self.hp = 2 * ENERYPRECENT
            self.fullhp = 2 * ENERYPRECENT
            self.speed = random.randint(5, 6)
            self.score = 1
        elif flag == 2:
            self.image = read_secret('pictures/enemys/enemy2.xml')
            self.hp = 2 * ENERYPRECENT
            self.fullhp = 2 * ENERYPRECENT
            self.speed = random.randint(5, 7)
            self.score = 1
        elif flag == 3:
            self.image = read_secret('pictures/enemys/enemy3.xml')
            self.hp = 4 * ENERYPRECENT
            self.fullhp = 4 * ENERYPRECENT
            self.speed = random.randint(5, 6)
            self.score = 1
        elif flag == 4:
            self.image = read_secret('pictures/enemys/enemy4.xml')
            self.hp = 4 * ENERYPRECENT
            self.fullhp = 4 * ENERYPRECENT
            self.speed = random.randint(5, 9)
            self.score = 1
        elif flag == 5:
            self.image = read_secret('pictures/enemys/enemy5.xml')
            self.hp = 6 * ENERYPRECENT
            self.fullhp = 6 * ENERYPRECENT
            self.speed = random.randint(5, 7)
            self.score = 1
        elif flag == 6:
            self.image = read_secret('pictures/enemys/enemy6.xml')
            self.hp = 6 * ENERYPRECENT
            self.fullhp = 6 * ENERYPRECENT
            self.speed = random.randint(5, 8)
            self.score = 1
        elif flag == 7:
            self.image = read_secret('pictures/enemys/enemy7.xml')
            self.hp = 10 * ENERYPRECENT
            self.fullhp = 10 * ENERYPRECENT
            self.speed = 3
            self.score = 2
            self.shootflag = 0
        elif flag == 8:
            self.image = read_secret('pictures/enemys/enemy8.xml')
            self.hp = 14 * ENERYPRECENT
            self.fullhp = 14 * ENERYPRECENT
            self.speed = 4
            self.score = 3
        elif flag == 9:
            self.image = read_secret('pictures/enemys/enemy9.xml')
            self.hp = 2 * ENERYPRECENT
            self.fullhp = 2 * ENERYPRECENT
            self.speed = random.randint(15, 20)
            self.shootflag = 0
            self.score = 1
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1 + PLANEHENG / 2, HENG - PLANEHENG / 2)
        self.rect.y = -100
        self.shootdelay = random.randint(2000, 5000)
        self.mask = pygame.mask.from_surface(self.image)
        self.nowtime = self.pretime = pygame.time.get_ticks()
        lifebar = Lifebar(self, 2)
        lifebars.add(lifebar)

    def update(self):
        self.rect.y += self.speed
        self.shoot()
        if self.rect.y > SHU:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self):
        self.nowtime = pygame.time.get_ticks()
        self.shootxy = self.rect.midleft
        if (self.nowtime - self.pretime) > self.shootdelay and self.shootflag == 1:
            bullet = Bullet(2)
            bullet.setpos(self.shootxy[0] + 10, self.shootxy[1])
            enerybullets.add(bullet)
            self.pretime = pygame.time.get_ticks()
        else:
            pass


# 技能子弹类
class Skillbullet(pygame.sprite.Sprite):
    def __init__(self, flag):
        pygame.sprite.Sprite.__init__(self)
        self.rect = None
        self.image = None
        self.last_time = pygame.time.get_ticks()
        self.frame = 0
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.images = []
        self.rate = 100
        self.speed = 20
        self.flag = flag
        self.mask = None
        if heroflag == 1:
            self.load_image('pictures/hero/heroskill1.xml', 1024, 1024, 4, 3)
        elif heroflag == 2:
            self.load_image('pictures/hero/heroskill2.xml', 1024, 512, 2, 4)
        elif heroflag == 3:
            self.load_image('pictures/hero/heroskill3.xml', 1024, 1024, 3, 3)
        elif heroflag == 4:
            self.load_image('pictures/hero/heroskill4.xml', 1024, 1024, 3, 4)

    def load_image(self, filename, width, height, rows, columns):
        frame_width = width // columns
        frame_height = height // rows
        self.boom_picture = read_secret(filename)
        for row in range(rows):
            for col in range(columns):
                frame = self.boom_picture.subsurface([col * frame_width, row * frame_height, frame_width, frame_height])
                self.images.append(frame)
        self.image = self.images[0]
        self.last_frame = rows * columns - 1
        self.rect = self.images[0].get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time > self.last_time + self.rate:
            self.last_time = current_time
            self.image = self.images[self.frame]
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = 1
        self.rect.y = self.rect.y - self.speed
        if self.rect.y <= -300 or self.rect.y >= SHU + 300:
            self.kill()

    def setpos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# 爆炸类
class Boom(pygame.sprite.Sprite):  # flag代表爆炸是   1玩家2敌机3boss4子弹相撞  爆炸
    def __init__(self, flag):
        pygame.sprite.Sprite.__init__(self)
        self.flag = flag
        self.rect = None
        self.image = None
        self.last_time = pygame.time.get_ticks()
        self.frame = 0
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.images = []
        self.rate = 10
        if flag == 1:
            self.load_image('pictures/blasts/boom.xml', 658, 329, 4, 8)
        elif flag == 2:
            self.load_image('pictures/blasts/blast2.xml', 570, 112, 1, 5)
        elif flag == 3:
            self.load_image('pictures/blasts/boom.xml', 658, 329, 4, 8)
        elif flag == 4:
            self.load_image('pictures/blasts/blast0.xml', 465, 72, 1, 6)

    def load_image(self, filename, width, height, rows, columns):
        frame_width = width // columns
        frame_height = height // rows
        self.boom_picture = read_secret(filename)
        for row in range(rows):
            for col in range(columns):
                frame = self.boom_picture.subsurface([col * frame_width, row * frame_height, frame_width, frame_height])
                self.images.append(frame)
        self.image = self.images[0]
        self.last_frame = rows * columns - 1
        self.rect = self.images[0].get_rect()

    def setpos(self, center):
        self.rect.center = center

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time > self.last_time + self.rate:
            self.last_time = current_time
            self.image = self.images[self.frame]
            self.frame += 1
            if self.frame > self.last_frame:
                self.kill()


# 道具类
class Prop(pygame.sprite.Sprite):  # flag代表道具是  1加血道具还是2炮弹升级道具
    def __init__(self, flag):
        pygame.sprite.Sprite.__init__(self)
        self.flag = flag
        self.flag = flag
        self.rect = None
        self.image = None
        self.last_time = pygame.time.get_ticks()
        self.frame = 0
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.images = []
        self.rate = 300
        self.speed = 2
        self.mask = None
        if flag == 1:
            self.load_image('pictures/supplys/lifesupply.xml', 303, 98, 1, 3)
        elif flag == 2:
            self.load_image('pictures/supplys/powersupply.xml', 249, 81, 1, 3)
        elif flag == 3:
            self.load_image('pictures/supplys/mpsupply.xml', 249, 81, 1, 3)

    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y < 0 or self.rect.y > SHU:
            self.kill()
        current_time = pygame.time.get_ticks()
        if current_time > self.last_time + self.rate:
            self.last_time = current_time
            self.image = self.images[self.frame]
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = 0

    def load_image(self, filename, width, height, rows, columns):
        frame_width = width // columns
        frame_height = height // rows
        self.boom_picture = read_secret(filename)
        for row in range(rows):
            for col in range(columns):
                frame = self.boom_picture.subsurface([col * frame_width, row * frame_height, frame_width, frame_height])
                self.images.append(frame)
        self.image = self.images[0]
        self.last_frame = rows * columns - 1
        self.rect = self.images[0].get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def setpos(self, center):
        self.rect.center = center


# 子弹类
class Bullet(pygame.sprite.Sprite):  # flag代表子弹是属于   1玩家 2敌机 3BOSS
    def __init__(self, flag):
        pygame.sprite.Sprite.__init__(self)
        self.flag = flag
        self.speedx = 0
        self.rect = None
        self.image = None
        self.last_time = pygame.time.get_ticks()
        self.frame = 0
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.images = []
        self.rate = 200
        self.mask = None
        self.bounce = False
        if self.flag == 1:
            self.images = PLAYERBULLETIMG
            self.image = self.images[0]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.speedy = -10
        elif self.flag == 2:
            self.image = read_secret('pictures/enemys/enemybullet.xml')
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.speedy = 10
        elif self.flag == 3:
            self.speed = -10
        self.nowtime = self.pretime = pygame.time.get_ticks()
        self.delay = 0

    def setpos(self, x, y, bounce=False):
        self.bounce = bounce
        self.rect.x = x
        self.rect.y = y

    def load_image(self, filename, width, height, rows, columns):
        frame_width = width // columns
        frame_height = height // rows
        self.boom_picture = read_secret(filename)
        for row in range(rows):
            for col in range(columns):
                frame = self.boom_picture.subsurface([col * frame_width, row * frame_height, frame_width, frame_height])
                self.images.append(frame)
        self.image = self.images[0]
        self.last_frame = rows * columns - 1
        self.rect = self.images[0].get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.nowtime = pygame.time.get_ticks()
        if self.nowtime - self.pretime > self.delay:
            self.delay = 0
            self.rect.y = self.rect.y + self.speedy
            self.rect.x = self.rect.x + self.speedx
            self.pretime = pygame.time.get_ticks()
        if self.rect.y < 0 or self.rect.y > SHU:
            self.kill()
        if (self.bounce is True):
            if (self.rect.x < 0) or (self.rect.x > HENG - 60):
                self.speedx = -self.speedx
        if self.flag == 1:
            if player1.powerlever == 1 or player1.powerlever == 2:
                self.image = self.images[0]
            elif player1.powerlever == 3 or player1.powerlever == 4:
                self.image = self.images[1]
            elif player1.powerlever == 5 or player1.powerlever == 6 or player1.powerlever == 7:
                self.image = self.images[2]
            elif player1.powerlever == 8:
                self.image = self.images[3]
        elif self.flag == 3:
            current_time = pygame.time.get_ticks()
            if current_time > self.last_time + self.rate:
                self.last_time = current_time
                self.image = self.images[self.frame]
                self.frame += 1
                if self.frame > self.last_frame:
                    self.frame = 0

    def setspeedxy(self, speedx, speedy):
        self.speedx = speedx
        self.speedy = speedy

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def setdelay(self, delay=0):
        self.delay = delay


# 游戏初始化
bgm = read_secret_sound('sounds/bgm.xml')
menu_sound = read_secret_sound('sounds/menu.xml')
screen = pygame.display.set_mode((HENG, SHU), pygame.FULLSCREEN)  # 设定游戏区域大小,并全屏显示, pygame.FULLSCREEN
backgrounds = pygame.sprite.Group()  # 背景图片精灵组
background1 = Background()
background1.setpos(0, -1920)
backgrounds.add(background1)
background2 = Background()
background2.setpos(0, -4920)
backgrounds.add(background2)
lifebars = pygame.sprite.Group()  # 血条精灵组
enerys = pygame.sprite.Group()  # 敌机精灵组
players = pygame.sprite.Group()  # 玩家精灵组
player1 = Player()
players.add(player1)
playerbullets = pygame.sprite.Group()  # 玩家子弹精灵组
enerybullets = pygame.sprite.Group()  # 敌机子弹精灵组
skillbullets = pygame.sprite.Group()  # 技能子弹组
booms = pygame.sprite.Group()  # 爆炸精灵组
bloodupprops = pygame.sprite.Group()  # 加血道具精灵组
powerupprops = pygame.sprite.Group()  # 炮弹升级道具精灵组
mpprops = pygame.sprite.Group()  # 加蓝量道具精灵组
bosses = pygame.sprite.Group()  # Boss精灵组
bossbullets = pygame.sprite.Group()  # Boss炮弹精灵组
boss1 = Boss()
bosses.add(boss1)
menu()
