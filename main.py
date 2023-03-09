




# mx = 0
# for i in range(10000):
#     a = 17*(32**i+1)**2
#     b = bin(a)[2:]
#     if b.count('0')>1000:
#         s = list(b.split('1'))
#         for v in s:
#             if mx<len(v):
#                 mx=len(v)
#         break
# print(mx)



# for i in range(4, 10000):
#     N = i
#     a = []
#     for j in range(1, N+1):
#         a.append(j)
#     while len(a) > 1:
#         if a[0] % 2 != 0:
#             x = a[-1]
#             a[-1] = x - a[0]
#         else:
#             x = a[-1]
#             a[-1] = x + a[0]
#         del a[0]
#     if a[0] == 67:
#         print(N)



a = 123
print(bin(a))
print(hex(a))
print(oct(a))

