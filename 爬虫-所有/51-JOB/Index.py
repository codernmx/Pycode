# @Time : 2021/11/2 22:24
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm
# 发送请求
import requests
import re  # 正则表达式模块
import json
import pprint
import csv

f = open('招聘4.csv', mode='a', encoding='ANSI', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['职位名称', '基本信息', '公司名称', '公司类型', '公司规模',
                                           '公司性质', '公司福利', '薪资', '发布日期', '职位详情页'])
csv_writer.writeheader()  # 写入表头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

}
for i in range(1,100):
    url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,'+ str(i) +'.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    # 解析数据
    html_data = re.findall('window\.__SEARCH_RESULT__ = (.*?)</script>', response.text)[0]
    json_data = json.loads(html_data)
    # 格式化输出
    # pprint.pprint(json_data)
    # 解析json数据
    search_result = json_data['engine_jds']
    for index in search_result:
        # pprint.pprint(index)
        title = index['job_name']  # 职位名称
        attribute_text = index['attribute_text']  # 基本信息
        # 列表转成字符串 ['深圳-福田区', '3-4年经验', '大专', '招3人']
        iob_info = '|'.join(attribute_text)
        company_name = index['company_name']  # 公司名称
        companyind_text = index.get('companyind_text')  # 公司类型
        companyind_size_text = index['companysize_text']  # 公司规模
        companytype_text = index['companytype_text']  # 公司性质
        job_w = index['jobwelf']  # 公司福利
        money = index['providesalary_text']  # 薪资
        date = index['updatedate']  # 发布日期
        job_href = index['job_href']  # 职位详情页
        dit = {
            '职位名称': title,
            '基本信息': iob_info,
            '公司名称': company_name,
            '公司类型': companyind_text,
            '公司规模': companyind_size_text,
            '公司性质': companytype_text,
            '公司福利': job_w,
            '薪资': money,
            '发布日期': date,
            '职位详情页': job_href,
        }
        csv_writer.writerow(dit)
        print(dit)
