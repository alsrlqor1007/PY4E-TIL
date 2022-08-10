# Lecture reference
fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt' # 아무 값 없이 엔터만 입력해도 clown.txt로 처리한다.
hand = open(fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()
    wds = lin.split()

    for w in wds :
        di[w] = di.get(w, 0) + 1
#         if w in di :
#             di[w] = di[v] + 1
#         else :
#             di[w] = 1

# print(di)

largest = -1
theword = None
for k, v in di.items() :
    print(k,v)

    if v > largest :
        largest = v
        theword = k

print('Done', theword, largest)