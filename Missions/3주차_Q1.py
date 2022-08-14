def gugudan(number):
    print(number, '단')

    count = 1
    while True:
        result = number * count

        if result <= 50:
            print(number, 'X', count, '=', result)
        else:
            break

        count += 2

try:
    number = int(input("몇 단?: "))
    gugudan(number)
except:
    print('올바른 숫자를 입력해 주세요.')
    quit()