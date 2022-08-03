fileHandler = open('mbox-short.txt')

for line in fileHandler:
    withoutBlanks = line.rstrip()
    upperedLines = withoutBlanks.upper()
    print(upperedLines)


# Lecture reference
fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())