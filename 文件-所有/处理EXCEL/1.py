file = open("1.xlsx", encoding='utf-8')
txt = []
for line in file.readlines():  #readlines获取所有行   line就是每行
    if line[0] == "#":  #过滤掉以#开头的
        continue
    txt.append(line.strip())  #将每一个添加到
print(txt, 'txt存入一个列表')