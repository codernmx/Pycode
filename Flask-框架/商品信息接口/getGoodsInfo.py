import pymysql
import requests
import json

# 连接数据库
db = pymysql.connect(host="localhost",user="root",password="137928",database="db",port=3306)# (需要改成ORACLE版本)
# 使用cursor()方法获取操作游标
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)# (需要改成ORACLE版本)


headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
}

def getDetail(singurl):
    print('正在获取-------------->>>>>>>', singurl)
    req = requests.get(singurl, headers=headers).content.decode('utf-8')

    item_info = json.loads(req)['item_info']
    print('当前页面数据条数为------->{}'.format(len(item_info)))
    for i in item_info:
        itemshorttitle = i['itemshorttitle']# 短标题
        itemshorttitle = itemshorttitle.replace('【','')
        itemshorttitle = itemshorttitle.replace('】','')
        itemdesc = i['itemdesc']# 详情
        itempic = i['itempic']# 图片
        itemendprice = i['itemendprice']# 券后价

        # (需要改成ORACLE版本)
        sql = f"insert into info (title,des,picture,price) values ('{itemshorttitle}','{itemdesc}','{itempic}','{itemendprice}')"
        try:
            cursor.execute(sql)  # 执行SQL语句# (需要改成ORACLE版本)
        except:
            print('当前错误页面链接为{}'.format(singurl))

# 获取20页也就是2000条数据

for i in range(1,20):
    url ='https://www.haodanku.com/allitem/hdk_allitem_list?p={}'.format(i)
    getDetail(url)