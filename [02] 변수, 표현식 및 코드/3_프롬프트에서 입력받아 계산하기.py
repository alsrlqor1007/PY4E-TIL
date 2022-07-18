# ** 실습 문제 **
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.
# 사용자가 일한 시간(hours)과 시급(rate per hour)을 프름프트에서 입력하면, 임금 총액을 계산해 주는 프로그램을 만들어 보세요.
# 35시간을 일 하고, 시간당 2.75 만큼을 벌었다고 가정하겠습니다. (그러면, 임금 총액은 96.25가 됩니다). 여러분은 input 함수를 써서 문자열(string)타입을 읽어오게 되지만, float()을 통해 변환을 해주어야 합니다.

hours = input('Hours: ')
ratePerHour = input('Rate per hour: ')
pay = float(hours) * float(ratePerHour)
print('Earned ', pay)