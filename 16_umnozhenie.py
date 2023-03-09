from collections import deque


def sum_hex(x, y):
    HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)

    while x:

        if y:
            res = HEX_NUM[x.pop()] + HEX_NUM[y.pop()] + transfer

        else:
            res = HEX_NUM[x.pop()] + transfer

        transfer = 0

        if res < 16:
            result.appendleft(HEX_NUM[res])

        else:
            result.appendleft(HEX_NUM[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    return list(result)


def mult_hex(x, y):
    HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = HEX_NUM[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * HEX_NUM[x[j]])

        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(HEX_NUM[res])

        else:
            result.appendleft(HEX_NUM[res % 16])
            transfer = res // 16

    if transfer:
            result.appendleft(HEX_NUM[transfer])

    return list(result)


def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


def conver_to_ten(number, base):
    return int(number, base)

# Перевод шестнадцатиричной в десятичную
# number = '123f'
# result = int(number, 16)
# print(result)


# a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
# b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

# print(*a, '+', *b, '=', *sum_hex(a, b))
#
# print(*a, '*', *b, '=', *mult_hex(a, b))

print(convert_to(123, 16))