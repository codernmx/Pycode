import bs4
import re
import urllib.request, urllib.error
import csv

findLink = re.compile(r'href="(.*?)"')
findTitle = re.compile('title="(.*?)"')
findRatingInteger = re.compile('class="integer">([0-9].)')
findRatingFraction = re.compile('</i><i class="fraction">([0-9])<')
findActors = re.compile('主演：(.*)')
findDirector = re.compile(
    '< img .*="[\u4e00-\u9fa5]{0,30}[0-9]?.?[\u4e00-\u9fa5]{0,30}? ([\u4e00-\u9fa5]{0,40}·?[\u4e00-\u9fa5]{0,40})')
findIncome = re.compile('>(.*)<')
findType = re.compile('> (.*) <')
findDuration = re.compile('(...分钟)')
findRegion = re.compile('([\u4e00-\u9fa5]{0,20})\n.*\/')


def main():
    baseurl = "https://maoyan.com/board/4?offset=0"
    datalist = getData(baseurl)
    savepath = "./Data.csv"
    saveData(savepath, datalist)


def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 10)
        html = askURL(url)
        soup = bs4.BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="board-item-main"):
            data = []
            item = str(item)
            tempLink = "".join(re.findall(findLink, item))
            link = "https://maoyan.com" + tempLink
            subHtml = askURL(link)

            # 1. Title
            name = re.findall(findTitle, item)[0]
            data.append(name)
            # 2. Name of director
            director = getDirector(subHtml)
            data.append(director)
            # 3. Name of actors
            actors = re.findall(findActors, item)[0]
            data.append(actors)
            # 4. Rating
            RatingInteger = re.findall(findRatingInteger, item)[0]
            RatingFraction = re.findall(findRatingFraction, item)[0]
            Rating = RatingInteger + RatingFraction
            data.append(Rating)
            # 5. Cumulative income
            income = getIncome(subHtml)[0]
            data.append(income)
            # 6. Type
            type = getType(subHtml)
            data.append(type)
            # 7. Duration
            duration = getDuration(subHtml)[0]
            data.append(duration)
            # 8. Region
            region = getRegion(subHtml)[0]
            data.append(region)
            print(data)
            datalist.append(data)

    return datalist


def getDirector(subHtml):
    soup = bs4.BeautifulSoup(subHtml, "html.parser")
    soup1 = str(soup.find_all(class_="celebrity-group")[0])
    director = re.findall(findDirector, soup1)
    return director[0]


def getIncome(subHtml):
    try:
        soup = bs4.BeautifulSoup(subHtml, "html.parser")
        soup1 = str(soup.find_all(class_="mbox-name")[2])
        income = re.findall(findIncome, soup1)
    except:
        return ['暂无']
    return income


def getType(subHtml):
    soup = bs4.BeautifulSoup(subHtml, "html.parser")
    soup1 = str(soup.find_all(class_="ellipsis")[1])
    type = re.findall(findType, soup1)
    b = ""
    for i in type:
        b = b + i + ","

    return b[:-1]


def getDuration(subHtml):
    soup = bs4.BeautifulSoup(subHtml, "html.parser")
    soup1 = str(soup.find_all(class_="ellipsis")[2])
    duration = re.findall(findDuration, soup1)
    return duration

def getRegion(subHtml):
    soup = bs4.BeautifulSoup(subHtml, "html.parser")
    soup1 = str(soup.find_all(class_="ellipsis")[2])
    region = re.findall(findRegion, soup1)
    return region

def askURL(url):
    head = {}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print("a")
    return html


def saveData(savepath, data):
    headers = ['电影名称', '导演', '演员', '评分', '收入', '类型', '时长', '国家']

    with open(savepath, 'w')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(data)


if __name__ == "__main__":
    main()