def find_even_number(n, m):
    numbers = [i for i in range(n, m + 1)]
    mid = numbers[int((m - 1) / 2)]

    for num in numbers:
        if num % 2 == 0:
            print(f'{num} 짝수')
            if num == mid:
                print(f'{num} 중앙값')


try:
    n = int(input("첫 번째 수 입력: "))
    m = int(input("두 번째 수 입력: "))

    find_even_number(n, m)
except:
    print('올바른 숫자로 입력해 주세요.')
    quit()

