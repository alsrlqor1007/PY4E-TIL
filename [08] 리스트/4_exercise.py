fileHandler = open('mbox-short.txt')

for line in fileHandler:
    words = line.rstrip().split()

    # 조건 순서 중요
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])


# Lecture reference
han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()

    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[2])