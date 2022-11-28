# pizza='|'
# def pizzaroll(pizza):
#     if pizza == '|':
#         pizza = '/'
#     elif pizza == '/':
#         pizza = '-'
#     elif pizza == '-':
#         pizza = '\\'
#     elif pizza == '\\':
#         pizza = '|'
#     print('\b'+pizza, sep='', end='')
#
# for i in range (1000):
#     for j in range(1000):
#         for k in range(1000):
#             pass
#     pizzaroll(pizza)
import math

# for a in range(1,150):
#     for b in range(a, 150):
#         for c in range(b, 150):
#             for d in range(c, 150):
#                 for e in range(d, 150):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                          print (a+ b + c + d +e)
# #         pizza

#import math
# n = 150
# for e in range (1,n):
#     for d in range (1,e):
#         for c in range(1, int(e / pow(2, 1 / 5))):
#             for c in range(1, int(e / pow(2, 1 / 5))):
#                 for b in range(1, int(e / pow(3, 1 / 5))):
#                     for a in range(1, int(e / pow(2, 1 / 4))):
#                         if (pow(a, 5) + pow(b, 5)+ pow(c, 5) + pow(d, 5)) == pow(e, 5):
#                             print(a + b + c + d + e)

# var, output = int(input("Число: ")), 1
# for i in range(1, var+1):
#     for j in range (0, i):
#         print(output, end = ' ')
#         output+=1
#     print()

#================
# for i in range(10):
#     for j in range(i+1):
#         print(j, end= ' ')
#     print()
#================
# for i in range(10):
#     for _ in range(i):
#         print(' ', end = ' ')
#     for _ in range(10-i):
#         print(_, end=' ')
#     print()
# ================
# var = int(input())
# while var > 9:
#     sum = 0
#     while var > 0:
#         sum += var % 10
#         var //= 10
#         #print(var)
#     var = sum
#     #print("--", var)
# print(var)
# ================
# var, total = int(input()), 0
# for i in range (1, var + 1):
#     fctrl = 1
#     for j in range (1, i + 1):
#         fctrl *= j
#     total +=fctrl
# print(total)
# ================
# def fctrl(x):
#     if x == 1:
#         return 1
#     return x * fctrl(x - 1)
# print(sum(fctrl(i) for i in range(1, int(input()) + 1)))
#================
# varA, varB = int(input()), int(input())
# for i in range(varA, varB + 1):
#     counter = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             counter += 1
#     if counter == 2:
#         print(i)
#============
# a, b = int(input()), int(input())
# if a == 1:
#     a = 2
# for number in range(a, b + 1):
#     for j in range(2, int(number ** 0.5) + 1):
#         if number % j == 0:
#             break
#     else:
#         print(number)
#=========
# количество цифр 3 в нем;
# сколько раз в нем встречается последняя цифра;
# количество четных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
# сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
# limiter = 50
# for a in range(limiter):
#     for b in range(limiter):
#         for c in range(limiter):
#             for d in range(limiter):
#                 if a != b and a != c and a != d and b != c and b != d and c != d and (a ** 3 + b ** 3 == c ** 3 + d ** 3):
#                     print (a ** 3 + b ** 3)
#==============
# n = 50000
# for i in range(1, n + 1):
# 	count = 0
# 	for x in range(1, int(i**(1/3)) + 1):
# 		for y in range(x, int(i**(1/3)) + 1):
# 			if x**3 + y**3 == i:
# 				count += 1
# 			elif x**3 + y**3 > i:
# 				break
# 	if count >= 2:
# 		print(i)
#========
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
#========
# string = "abcdefghijklmnop"
# #[print(string[i]) for i in range(0, len(string), 2)]
# [print(letter) for letter in string[::2]]
#==========
# var, binary = int(input()), ''
# while var > 0:
#     binary += str(var % 2)
#     var //= 2
# binary = binary[::-1]
# print(binary)
#==========
# var = input('> ')
# print(str(bin(int(var)))[2:])
#==========
# def num10to_base(strn, base=2):
#     num, res = int(strn), ''
#     while(num):
#         res, num = str(num % base) + res, num // base
#     return res
# print(num10to_base(input()))
#==========
# string = 'jazzaj'
# print('YES' if string == string[::-1] else 'NO')
#==========
# print(('1st', '2nd')[False])
#==========


# print(ord('f'))
# print(ord('r'))
# bias, string = 14, 'fsfftsfufksttskskt'
# for char in string:
#     print(chr(ord(char) - (bias % 25)), end = '')

#=========

# data = input().split()
# checked, result = [], 0
# for i in data:
#     counter = data.count(i) // 2
#     if i not in checked and counter > 0:
#         result += counter
#         checked.append(i)
# print(result)

def quick_merge(listA, listB):
    result=[]
    startA, startB = 0,0
    while(startA < len(listA) and startB < len(listB)):
        if listA[startA] <= listB[startB]:
            result.append(listA[startA])
            startA +=1
        else:
            result.append(listB[startB])
            startB += 1

    if startA == len(listA):
        result += listB[startB:]
    elif startB == len(listB):
        result += listA[startA:]
    return result

def quick_merge1(listA, listB):
    print('=', listA, listB)
    result=[]
    while (len(listA)>0 and len(listB)>0):
        if listA[0] <= listB[0]:
            result.append(listA.pop(0))
        else:
            result.append(listB.pop(0))
    print('temp', result, listA, listB)

    if len(listA) == 0:
        result += listB
    elif len(listB) == 0:
        result += listA
    return result

#columns = int(input('n>'))
#data = [[int(num) for num in input('subs>').split()] for sub in range(columns)]
data = [[1,2,9,10,20],[4,5,6,7]]
result=[]
for part in data:
    #result = quick_merge(result,part)
    result = quick_merge1(result,part)
    print('>>', result)
    input()
print(*result)



