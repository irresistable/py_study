# объявление функции
def is_one_away(word1, word2):
    if len([i for i in range(len(word1)) if word1[i] != word2[i] ]) ==1 and len(word1)==len(word2):
        print([c for c in word1 if c not in word2])
        return True
    else:
        print([c for c in word1 if c not in word2])
        return False

# считываем данные
txt1 = 'aab'
txt2 = 'abb'

# вызываем функцию
#print(is_one_away(txt1, txt2))


# объявление функции


def is_palindrome(text):
    begin, end = 0, len(text)-1
    while(begin < end):
        while (not text[begin].lower().isalpha()):
            begin +=1
        while(not text[end].lower().isalpha()):
            end -= 1
        print(text[begin].lower() + '-' + str(begin) + '-' + text[end].lower()+ '-' + str(end))
        if text[begin].lower() != text[end].lower():
            print('here')
            return False
        begin +=1
        end -= 1
    return True

def is_palindrome1(text):
    temp = [c.lower() for c in text if c.isalpha()]
    print(*temp, sep ='')
    print(*temp[::-1], sep ='')
    if temp==temp[::-1]:
        return True
    else:
        return False

def is_correct_bracket(text):
    l = []
    r = []
    for i in range(len(text)):
        if text[i] == '(':
            l.append(i)
        elif text[i] == ')':
            r.append(i)
    if len(l) != len(r):
        return False
    else:
        for i in range(len(l)):
            if l[i] > r[i]:
                return False
        return True
def is_correct_bracket2(text):
    while '()' in text:
        text = text.replace('()', '')
        print(text)

    if not text:
        return True
    else:
        return False

# объявление функции
import re
def convert_to_python_case(text):
    data = [c.lower() for c in re.findall('[A-Z][^A-Z]*', text)]
    res = '_'.join(data)
    print(data)
    print(res)

def convert_to_python_case2(text):
    data = []
    data.extend(text)
    print(data)
    for i in range (len(data)):
        if data[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            data[i]=data[i].lower()
            data.insert(i,'_')
    del data[0]
    return ( ''.join(data))

def convert_to_python_case3(text):
    res=''
    for char in text:
        if char.isupper():
            res += '_'
        res += char.lower()
    return(res[1:])

def convert_to_python_case4(text):
    return(''.join(['_' + char.lower() if char.isupper() else char for char in text]).lstrip('_'))

# считываем данные

txt = 'ThisIsCamelCased'

# вызываем функцию
print(convert_to_python_case4(txt))