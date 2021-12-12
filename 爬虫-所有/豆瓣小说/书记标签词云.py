import pymysql.cursors
import pyecharts.options as opts
from pyecharts.charts import WordCloud


# 以空格为间隔，将标签连接成一个string
def get_tags_str():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='137928',  # 数据库密码
        db='douban_novels',
        charset='utf8mb4'
    )
    cursor = conn.cursor()

    sql_select = 'select tag from douban_novels.novel_tags'
    cursor.execute(sql_select)
    tags = cursor.fetchall()
    tags_str = ''
    for tag in tags:
        tags_str += tag[0]
        tags_str += ' '

    cursor.close()
    conn.close()

    return tags_str


# 以空格为间隔，将出版社连接成一个string
def get_publishers_str():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='137928',  # 数据库密码
        db='douban_novels',
        charset='utf8mb4'
    )
    cursor = conn.cursor()

    sql_select = 'select publisher from douban_novels.novels'
    cursor.execute(sql_select)
    publishers = cursor.fetchall()
    publishers_str = ''
    for publisher in publishers:
        publishers_str += publisher[0]
        publishers_str += ' '

    cursor.close()
    conn.close()
    return publishers_str


def drawTag(data, name):
    c = (
        WordCloud()
            .add(series_name=name, data_pair=data, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title=name, title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            .render(name + ".html")
    )
    return c


# 生成词云
if __name__ == '__main__':
    # 生成标签词云
    tags_str = get_tags_str()
    tag_list = tags_str.split(' ')
    count_tag = {}
    for i in tag_list:
        if i in count_tag:
            count_tag[i] += 1
        else:
            count_tag[i] = 0

    key_tag_list = count_tag.keys()  #获取对象的关键字
    data_tag = []
    for i in key_tag_list:
        print(count_tag[i])
        data_tag.append((i,count_tag[i]))
    # print()
    drawTag(data_tag,'标签词云图')

    # 生成出版社词云
    publishers_str = get_publishers_str()
    publishers_list = publishers_str.split(' ')
    count_publishers = {}
    for i in publishers_list:
        if i in count_publishers:
            count_publishers[i] += 1
        else:
            count_publishers[i] = 0
    print(count_publishers)

    key_count_publishers_list = count_publishers.keys()  # 获取对象的关键字
    data_publishers = []
    for i in key_count_publishers_list:
        data_publishers.append((i, count_publishers[i]))
    # print()
    drawTag(data_publishers, '出版社词云图')
