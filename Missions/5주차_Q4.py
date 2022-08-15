import datetime


def after_100(month, day, day_of_week):
    monthly_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ['월', '화', '수', '목', '금', '토', '일']

    start_date = datetime.datetime(datetime.datetime.now().year, month, day)
    date_after = start_date + datetime.timedelta(days=99)

    day_of_week_after = days_of_week[(days_of_week.index(day_of_week) + 1) % 7]

    print(f'{month}월 {day}일 {day_of_week}요일부터 100일 뒤는 {date_after.month}월 {date_after.day}일 {day_of_week_after}요일')


anniversary_month = int(input('몇 월:'))
anniversary_date = int(input('몇 일:'))
anniversary_day = input('무슨 요일: ')

after_100(anniversary_month, anniversary_date, anniversary_day)


# 다른 풀이
def after_100(month, day, day_of_the_week):
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_the_week_list = ["월", "화", "수", "목", "금", "토", "일"]


after_month = month
after_day = day + 99

after_day_of_the_week = day_of_the_week_list[(
    day_of_the_week_list.index(day_of_the_week) + 99) % 7]

while after_day > day_in_month[after_month - 1]:
    after_day -= day_in_month[after_month - 1]
    if after_month == 12:
        after_month = 1
    else:
        after_month += 1

print(f"{month}월 {day}일 {day_of_the_week}요일부터 100일 뒤는 {after_month}월 {after_day}일 {after_day_of_the_week}요일")


after_100(6, 21, "월")
