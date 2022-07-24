# 함수 선언
def computepay(hours, rate):
    if hours > 40:
        overHours = hours - 40
        pay = (40 + (overHours * 1.5)) * rate
    else:
        pay = hours * rate
    return pay

hours = float(input('Hours: '))
rate = float(input('Rate per hour: '))

result = computepay(hours, rate)

print('Earned: ', result)


# Lecture reference
def computepay(hours, rate):
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh, fr)

print("Pay: ", xp)
