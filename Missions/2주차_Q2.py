monthly_payment = input('월급(만원): ')

try:
    monthly_payment = int(monthly_payment)
except:
    print('숫자로 입력해주세요.')
    quit()

def yearly_payment(monthly_payment):
    before_tax = monthly_payment * 12

    if before_tax <= 1200:
        tax = 0.06
    elif before_tax <= 4600:
        tax = 0.15
    elif before_tax <= 8800:
        tax = 0.24
    elif before_tax <= 15000:
        tax = 0.35
    elif before_tax <= 30000:
        tax = 0.38
    elif before_tax <= 50000:
        tax = 0.40
    else:
        tax = 0.42

    return before_tax * (1 - tax)

before_tax = monthly_payment * 12
result = yearly_payment(monthly_payment)

print('세전 연봉: ', before_tax, '만원')
print('세후 연봉: ', result, '만원')