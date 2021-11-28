n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
    print(counter)
print('Sum of 1 until %d: %d' % (n, sum))
