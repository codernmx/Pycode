def func1(x):
  if(x<0):
    x= abs(x)
  elif(x >= 0 and x < 3):
    x = x +1
  elif(x >= 3 and x < 8):
    x = 3 * x **2
  elif (x >= 8 and x < 10):
    x = 8 * x**3
  else:
    x = 10
  return x

def func2(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

def func3():
  return 0

def func4(m,n):
  if(m<n):
    num = 0
    for i in range(m+1,n):
      if(i%2==1):
        num+=i
    return num
  else:
    return 0

def func5(n):
  num = 0
  for i in range(1,n+1):
    if(n%i==0):
      num+=1
  return num

def func6(n):
  list_result = []
  n = str(n)
  for i in range(0,len(n)):
    a= n[i:i+1]
    list_result.append(a)
  return list_result

def func7(n):
  x = int('9'*n)
  list_result = []
  for i in range(2, x):
    list_i = func6(i)
    num = 0
    for ite in list_i:
      num += int(ite) ** n
    if i == num:
      list_result.append(i)
  return list_result

if __name__ == "__main__":
  # print(func1(-3))
  # print(func1(0))
  # print(func1(3))
  # print(func2(1900))
  # print(func2(2000))
  # print(func2(2020))
  # print(func4(3,12))
  # print(func4(12, 3))
  # print(func4(-4, 7))
  print(func5(12))
  # print(func6(123))
  # print(func7(7))