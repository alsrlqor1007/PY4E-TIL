count = 0
sum = 0

while True:
    number = input('Enter a number: ')

    if number == 'done':
        break

    try:
        number = float(number)
    except:
        print('Invalid input')
        continue

    count += 1
    sum += number
    avg = sum / count

print(sum, count, avg)


# Lecture reference
num = 0
tot = 0.0
while True :
    sval = input('Enter a number:')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    num = num + 1
    tot = tot + fval

print(tot,num,tot/num)