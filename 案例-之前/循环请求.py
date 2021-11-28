import urllib.request
url = 'https://api.day.app/ETH6H7jpx6yLfwUKzMUqzV/english/thisistest'
count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    data = resp.read().decode('utf-8')
    print("当前访问" + url)
print("Good bye!")
