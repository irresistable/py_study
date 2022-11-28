import sys

def open_file():
    try:
        sys.stdin = open("input1.txt", "r")
        return True
    except Exception as e:
        print(e)
        print("HALT")
        return False



def prn(start, end):


    data = {}
    for line in sys.stdin:
        temp = line.split()
        data[temp[0]] = temp[2:]

    print(data)
    print()

    def wayAB (data, start, end, nodes=[]):

        nodes = nodes + [start]
        print(f'{nodes} - {start} - {end} - {data[start]}')

        if start == end:
            return nodes

        if start not in data or end not in data:
            return None

        for node in data[start]:
            if node not in nodes:
                newway = wayAB(data, node, end, nodes)
                if newway:
                    return newway
        return None

    return wayAB(data, start, end)

def parenthood(data, start, end):

    def wayAB (data, start, end, nodes=[]):

        nodes = nodes + [start]
        #print(f'{nodes} - {start} - {end} - {data[start]}')

        if start == end:
            return nodes

        if start not in data or end not in data:
            return None

        for node in data[start]:
            if node not in nodes:
                newway = wayAB(data, node, end, nodes)
                if newway:
                    return newway
        return None

    if wayAB(data, start, end):
        return True
    else:
        return False

try:
    sys.stdin = open("input2.txt", "r")
except Exception as e:
    print(e)
    print("HALT")

query=[]
for str in sys.stdin:
    query+=str.rstrip()
try:
    sys.stdin = open("input1.txt", "r")
except Exception as e:
    print(e)
    print("HALT")
data = {}
for line in sys.stdin:
    temp = line.split()
    data[temp[0]] = temp[2:]
print(data)
print(query)

checklist=[]

for i in range(len(query)):
    if i==0:
        checklist+=query[i]
        continue
    if parenthood(data, query[i], query[i-1]):
        print(f"{query[i]}")











