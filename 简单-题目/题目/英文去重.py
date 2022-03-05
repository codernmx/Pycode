# Python for data anlysis


"""
 Week 6 Assignment



题目： 写程序计算下面这段字符串中所包含的单词个数、其中重复出现的单词的个数（单词不区分大小写）
"""

str = """
Deep Learning

AlphaGo relies on deep neural networks—networks of hardware and software that mimic the web of neurons in the human brain. With these neural nets, it can learn tasks by analyzing massive amounts of digital data. If you feed enough photos of cow in the neural net, it can learn to recognize a cow. And if you feed it enough Go moves from human players, it can learn the game of Go. But Hassabis and team have also used these techniques to teach AlphaGo how to manage time. And the machine certainly seemed to manage it better than the Korean grandmaster. Its clock still carried sixteen minutes.

The Google machine repeatedly made rather unorthodox moves that the commentators could quite understand. But that too is expected. After training on real human moves, AlphaGo continues its education by playing game after game after game against itself. It learns from a vast trove of moves that it generates on it own—not just from human moves. That means it is sometimes makes moves no human would. This is what allows it to beat a top human like Lee Sedol. But over the course of an individual game, it can also leave humans scratching their heads.

Then AlphaGo's clock ran out. Both players were down to 60 seconds for each move, and Lee Sedol had exceeded his 60 seconds twice. One more, and he would forfeit the game. Soon, the game crossed the four-and-a-half-hour mark, and it looked, for the first time in the match, like the two players would play the game out to the very end without either player resigning. It was that close.

Eyeing the board, Redmond started to count up the points that seemed available to each player, and it appeared that one had an edge. "Unfortunately for Lee Sedol," he said, "I think white might have a slight advantage here." And as the game stretched to five hours, Redmond began to concede victory to AlphaGo. But it was hard to tell, he said, where Lee Sedol had gone wrong. Seconds later, the Korean resigned.

The game showed that AlphaGo is far from infallible. Early in the contest, it made a mistake that even a decent human player would not make. There are holes in its education. But, able to draw on months of play with itself—on a corpus of moves that no human has even seen—it also has the ability to climb out of such a deep hole, even against one of the world's best players. AI is flawed. But it is here.
"""


def changeStr(str):
  str = str.strip()
  str = str.replace('\n', ' ')  # 转换Learning之后
  str = str.replace('  ', ' ')  # 两个空格
  oneList = str.split(',')
  twoList =[]
  for i in oneList:
    if (len(i.split('.')) > 0):
      a = i.split('.')
      for j in a:
        twoList.append(j)
    else:
      twoList.append(i)
  threeList = []
  for k in twoList:
    if (len(k.split(' ')) > 0):
      b = k.split(' ')
      for l in b:
        threeList.append(l)
    else:
      threeList.append(k)
  #过滤掉"
  fourList = []
  for u in threeList:
    if (len(k.split('"')) > 0):
      c = k.split(' ')
      for y in c:
        fourList.append(y)
    else:
      fourList.append(u)
  fiveList = []
  #去掉 ' 空格'
  for o in threeList:
    if o!='' and o!='"':
      fiveList.append(o)
  print('单词个数为:',len(fiveList))

  #计算重复个数
  num = 0
  count = 0
  for t in fiveList:
    num+=1
    for r in range(num,len(fiveList)):
      # print(r)
      if t == fiveList[r]:
        # print(t,'-----------',fiveList[r])
        count+=1
        break
  print('重复出现的单词的个数',count)
  return 0
changeStr(str)
