import time
import xlwt
import requests
from bs4 import BeautifulSoup
import json
import random


# 存储到excel
def saveExcel(file_path, doctorInfo):
	f = xlwt.Workbook(encoding='utf-8')
	sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
	info = ['FullCompanyName', 'IncorporatedIn', 'IncorporatedOn', 'ISINCode', 'OffcTotal', 'Telephone', 'Fax', 'email',
			'Secretary',
			'LinktoInternetWebsite', 'LISTING', 'LISTINGBOARD', 'OTHERSTOCKEXCHANGELISTINGS', 'AUDITORS', 'Background']
	for col in range(0, 15):
		sheet1.write(0, col, info[col])
	# 将数据写入第 i 行，第 j 列
	row = 1
	for data in doctorInfo:
		for j in range(len(data)):
			sheet1.write(row, j, data[j])
		row = row + 1
	f.save(file_path)


headers = {
	"Accept": '*/*',
	"Accept-Encoding": 'gzip, deflate, br',
	"Accept-Language": 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
	"Connection": 'keep-alive',
	"origin": 'https://www.sgx.com',
	"referer": 'https://www.sgx.com/',
	# sec-ch-ua: "Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"
	"sec-ch-ua-mobile": '?0',
	"sec-ch-ua-platform": "Windows",
	"sec-fetch-dest": 'empty',
	"sec-fetch-mode": 'cors',
	"sec-fetch-site": 'same-site',
	"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
}
all_info = []
urlList = []
for iii in range(0, 8):
	url = 'https://api.sgx.com/corporateinformation/v1.0?pagestart=' + str(iii) + '&pagesize=100'
	response = requests.get(url, headers=headers).content.decode('utf-8')
	data = json.loads(response)['data']
	print(iii, '--------------', len(data))
	for i in data:
		url = 'https://links.sgx.com/1.0.0/corporate-information/' + str(i['id'])
		urlList.append(url)
num = 0
for singleUrl in urlList:
	num += 1
	res = requests.get(singleUrl, headers=headers).content.decode('utf-8')
	soup = BeautifulSoup(res, "lxml")
	if soup.select("#ctl07_compFullNameLabel"):
		FullCompanyName = soup.select("#ctl07_compFullNameLabel")[0].string
	else:
		FullCompanyName = ' '
	if soup.select("#ctl07_incorporatedLabel"):
		IncorporatedIn = soup.select("#ctl07_incorporatedLabel")[0].string
	else:
		IncorporatedIn = ' '
	if soup.select("#ctl07_incorpOnLabel"):
		IncorporatedOn = soup.select("#ctl07_incorpOnLabel")[0].string
	else:
		IncorporatedOn = ' '
	if soup.select("#ctl07_isinCodeLabel"):
		ISINCode = soup.select("#ctl07_isinCodeLabel")[0].string
	else:
		ISINCode = ' '
	if soup.select("#ctl07_regOffc1Label"):
		Offc1 = soup.select("#ctl07_regOffc1Label")[0].string
	else:
		Offc1 = ' '
	if soup.select("#ctl07_regOffc2Label"):
		Offc2 = soup.select("#ctl07_regOffc2Label")[0].string
	else:
		Offc2 = ' '
	if soup.select("#ctl07_regOffc3Label"):
		Offc3 = soup.select("#ctl07_regOffc3Label")[0].string
	else:
		Offc3 = ' '

	if soup.select("#ctl07_regOffc4Label"):
		Offc4 = soup.select("#ctl07_regOffc4Label")[0].string
	else:
		Offc4 = ' '
	OffcTotal = str(Offc1) + str(Offc2) + str(Offc3) + str(Offc4)

	if soup.select("#ctl07_teleLabel"):
		Telephone = soup.select("#ctl07_teleLabel")[0].string
	else:
		Telephone = ' '
	if soup.select("#ctl07_faxLabel"):
		Fax = soup.select("#ctl07_faxLabel")[0].string
	else:
		Fax = ' '

	if soup.select("#ctl07_emailLabel"):
		email = soup.select("#ctl07_emailLabel")[0].string
	else:
		email = ' '
	if soup.select("#ctl07_secretary1Label"):
		Secretary1 = soup.select("#ctl07_secretary1Label")[0].string
	else:
		Secretary1 = ' '
	if soup.select("#ctl07_secretary2Label"):
		Secretary2 = soup.select("#ctl07_secretary2Label")[0].string
	else:
		Secretary2 = ' '
	Secretary = str(Secretary1) + str(Secretary2)

	if soup.select("#ctl07_compWebHypLink"):
		LinktoInternetWebsite = soup.select("#ctl07_compWebHypLink")[0].string
	else:
		LinktoInternetWebsite = ' '

	if soup.select("#ctl07_listingDateLabel"):
		LISTING = soup.select("#ctl07_listingDateLabel")[0].string
	else:
		LISTING = ' '

	if soup.select("#ctl07_lbllistingBoard"):
		LISTINGBOARD = soup.select("#ctl07_lbllistingBoard")[0].string
	else:
		LISTINGBOARD = ' '

	if (soup.select("#ctl07_OtherStockExchangeLabel")):
		OTHERSTOCKEXCHANGELISTINGS = soup.select("#ctl07_OtherStockExchangeLabel")[0].string
	else:
		OTHERSTOCKEXCHANGELISTINGS = ' '
	if soup.select("#ctl07_auditor1Label"):
		AUDITORS0 = soup.select("#ctl07_auditor1Label")[0].string
	else:
		AUDITORS0 = ' '
	if soup.select("#ctl07_auditor1Label"):
		AUDITORS1 = soup.select("#ctl07_auditor1Label")[0].string
	else:
		AUDITORS1 = ' '

	AUDITORS = str(AUDITORS0) + str(AUDITORS1)

	if soup.select("#litIPOCompany"):
		Background = soup.select("#litIPOCompany")[0].string
	else:
		Background = ' '
	all_info.append(
		[FullCompanyName, IncorporatedIn, IncorporatedOn, ISINCode, OffcTotal, Telephone, Fax, email, Secretary,
		 LinktoInternetWebsite, LISTING, LISTINGBOARD, OTHERSTOCKEXCHANGELISTINGS, AUDITORS, Background])

	print(singleUrl)
	print(num)
	time.sleep(random.randint(1, 10))
saveExcel("731.xls", all_info)
