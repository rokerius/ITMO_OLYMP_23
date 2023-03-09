a = '123456'
for i in range(1000):
    l = len(a)
    n = a[l // 2 - 1 : l // 2 + 1]
    a = n + a
    print(i + 1 , a)
