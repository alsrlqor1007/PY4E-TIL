import random

userChoice = input('가위, 바위, 보 선택: ')

if (userChoice != '가위') and (userChoice != '바위') and (userChoice != '보'):
    print('가위, 바위, 보만 입력이 가능합니다.')
    quit()

def computerChoice():
    computer = random.randint(0, 2)

    if computer == 0:
        return '가위'
    elif computer == 1:
        return '바위'
    else:
        return '보'

def myChoice(userChoice):
    my = userChoice
    computer = computerChoice()

    if my == computer:
        result = '무승부!'
    elif my == '가위':
        if computer == '바위':
            result = '컴퓨터 승리!'
        elif computer == '보':
            result = '내가 승리!'
    elif my == '바위':
        if computer == '보':
            result = '컴퓨터 승리!'
        elif computer == '가위':
            result = '내가 승리!'
    elif my == '보':
        if computer == '가위':
            result = '컴퓨터 승리!'
        elif computer == '바위':
            result = '내가 승리!'

    print('나: ', my)
    print('컴퓨터: ', computer)
    print(result)

myChoice(userChoice)