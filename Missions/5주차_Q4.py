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
