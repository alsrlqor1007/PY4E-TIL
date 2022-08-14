try:
    age = int(input('나이: '))
except:
    print('나이는 숫자로 입력해주세요.')
    quit()

pay_method = input('현금, 카드 택 1: ')

if pay_method != '현금' and pay_method != '카드':
    print('현금과 카드만 가능합니다.')
    quit()

def bus_fare(age, pay_method):
    if age < 8 or age >= 75:
        fee = '무료'
    elif age >= 8 and age < 14:
        fee = '450원'
    elif age >= 14 and age < 20:
        if pay_method == '카드':
            fee = '720원'
        else:
            fee = '1000원'
    else:
        if pay_method == '카드':
            fee = '1200원'
        else:
            fee = '1300원'

    print('나이: ', age, '세')
    print('지불유형: ', pay_method)
    print('버스요금: ', fee)

bus_fare(age, pay_method)