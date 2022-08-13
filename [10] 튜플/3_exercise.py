file_name = input('Enter file: ')
if len(file_name) < 1:
    file_name = 'clown.txt'
handler = open(file_name)

dic = dict()
for line in handler:
    words = line.rstrip().split()

    for word in words:
        dic[word] = dic.get(word, 0) + 1

list = list()
for k, v in dic.items():
    reversed = (v, k)
    list.append(reversed)

list = sorted(list, reverse = True)

# list comprehension 방식
list_comprehension_ver = sorted([ (v, k) for k, v in dic.items() ], reverse = True)

for v, k in list_comprehension_ver[:5]:
    print(k, v)


#Lecture reference
fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds :
        di[w] = di.get(w,0) + 1

tmp = list()
for k, v in di.items() :
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse = True)

for v,k in tmp[:5] :
    print(k,v)