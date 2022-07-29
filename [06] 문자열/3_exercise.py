str = 'X-DSPM-Confidence: 0.8475'

colonIndex = str.find(':')
num = str[colonIndex + 2:]
value = float(num)
print(value)


# Lecture reference
str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
piece = str[ipos+2:]
value = float(piece)
print(value)