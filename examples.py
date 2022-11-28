var = int(input())

[print(i*str(i)) for i in range(1, var+1)]

#==========
import time
start = time.time()
#...
end = time.time()
print('elapsed time: ', end - start)

#============
from math import *

n = 5  # степень
max_par = 145  # верхний предел на переменную "e", можно менять
max_a = floor((max_par + 1) / pow(4, 0.2))
max_b = floor((max_par + 1) / pow(3, 0.2))
max_c = floor((max_par + 1) / pow(2, 0.2))
flag = True  # False: решение найдено; True: решение не найдено (т.е. теорема Эйлера верна для данных пределов перебираемых переменных)

for a in range(1, max_a + 1):
    if flag == False:  #далее: прерывания на случай нахождения решения на предыдущем шаге
        break
    for b in range(a + 1, max_b + 1):
        if flag == False:
            break
        for c in range(b + 1, max_c + 1):
            if flag == False:
                break
            for d in range(c + 1, max_par):
                e = pow((a ** n + b ** n + c ** n + d ** n), 0.2)
                if 1000000000 * floor(e) == floor(1000000000 * e) and e <= max_par + 1:  # сравнение до 9-го знака после запятой; + явное ограничение на e
                    print('НАЙДЕНО РЕШЕНИЕ: ', a, b, c, d, floor(e))
                    flag = False
                    break

print('Перебор завершён')

if flag == True:
    print('Решений не найдено')

#============
string = "abcdefghijklmnop"
#[print(string[i]) for i in range(0, len(string), 2)]
[print(letter) for letter in string[::2]]
#============
prod += c == '*'
prod += (1) так как c = True if c in ['*'], True = 1
#============
for bukva in text:
        p += bukva in '+'
        z += bukva in '*'
print('Символ + встречается', p, 'раз')
print('Символ * встречается', z, 'раз')
#============
str, s, count = input(), '', 0
for sb in str:
    if sb == s: count += 1
    s = sb
print(count)
#============
word = input()
print(('NO', 'YES')[word == word[::-1]])
print(('1st', '2nd')[False])
# ============
string = input()
print (string[int(len(string) / 2) + len(string) % 2:] + string[:int(len(string) / 2 + len(string) % 2)])
#=============
a = input()[::-1]
z = [a.count(i) for i in a]
print(a[z.index(max(z))])

a = input()[::-1]
z = max(a, key = a.count)
print(z)
#=============
c, s = 'f', 'abcdefgfhfabc'
b, e = s.find(c), s.rfind(c)
print('NO' if b < 0 else b, str(e) * (e > b))
#====
# put your python code here
s = input()
l = s.find('f') #первое вхождение
print(s.find('f', l+1) if l != -1 else -2)
#========
numbers = ([int(input()) for _ in range(int(input()))])
print(*[value for value in numbers  if min(numbers) < value < max(numbers)], sep = '\n')
#========
s = [input() for _ in range(int(input()))]
print(*[s[i] for i in range(len(s)) if s[:i].count(s[i]) == 0], sep="\n")
#=========
query = ['Python прекрасен', 'C# - отличный язык программирования', 'Stepik - отличная платформа', 'BEEGEEK FOREVER!', 'язык Python появился 20 февраля 1991']
search = ['язык', 'python']

for queryindex in query:
    for searchindex in search:
        if searchindex.lower() not in queryindex.lower():
            break
    else:
        print(queryindex)

for queryindex in query:
    if all(searchindex.lower() in queryindex.lower() for searchindex in search):
        print(queryindex)
#=============
print(('НЕТ', 'ДА')[sum(n.isdigit() and 0 <= int(n) <= 255 for n in input().split('.', 3)) == 4])
#=============
def convert_to_python_case3(text):
    res=''
    for char in text:
        if char.isupper():
            res += '_'
        res += char.lower()
    return(res[1:])

def convert_to_python_case4(text):
    return(''.join(['_' + char.lower() if char.isupper() else char for char in text]).lstrip('_'))
#=============
class MoneyBox:
    def __init__(self, capacity):
        self._capacity=capacity
        self._cash = 0

    def can_add(self, v):
        return self._cash + v <= self._capacity

    def add(self, v):
        if self.can_add(v):
            self._cash+=v
    def display(self):
        return self._cash
    #================
    
