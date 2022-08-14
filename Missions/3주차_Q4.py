def isPrime(num):
    if num == 1:
        return False

    square_root = round(num ** 0.5)
    for i in range(2, square_root + 1):
        if num % i == 0:
            return False
    return True

def count_prime_number(n, m):
    count = 0

    for num in range(n, m + 1):
        if isPrime(num) == True:
            count += 1

    return count


try:
    n = int(input("첫 번째 수 입력: "))
    m = int(input("두 번째 수 입력: "))

    result = count_prime_number(n, m)
    print(f'소수개수 {result}')
except:
    print('올바른 숫자로 입력해 주세요.')
    quit()