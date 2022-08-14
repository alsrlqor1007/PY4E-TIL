import random

def rcp(my, round):
    computer = random.randint(0, 2)

    if my == '가위' or my == '0':
        myChoice = '가위'
    elif my == '바위' or my == '1':
        myChoice = "바위"
    elif my == '보' or my == '2':
        myChoice = "보"

    if computer == 0:
        computerChoice = "가위"
    elif computer == 1:
        computerChoice = "바위"
    elif computer == 2:
        computerChoice = "보"

    if myChoice == computerChoice:
        result = "무승부!"
    elif myChoice == "가위" and computerChoice == "보":
        result = "나의 승리!"
    elif myChoice == "바위" and computerChoice == "가위":
        result = "나의 승리!"
    elif myChoice == "보" and computerChoice == "바위":
        result = "나의 승리!"
    else:
        result = "컴퓨터 승리!"

    print(f'나: {myChoice}')
    print(f'컴퓨터: {computerChoice}')
    print(f'{round}번째 판 {result}\n')

    return result


def rsp_advanced(games):
    round = games
    my_win = 0
    my_lose = 0
    draw = 0

    while round > 0:
        my = input("가위 바위 보: ")

        while my not in ['가위', '바위', '보', '0', '1', '2']:
            print('가위(0), 바위(1), 보(2)만 입력이 가능합니다.\n')
            my = input("가위 바위 보: ")

        result = rcp(my, round)
        if result == '무승부!':
            draw += 1
        elif result == '나의 승리!':
            my_win += 1
        else:
            my_lose += 1

        round -= 1

    print(f'나의 전적: {my_win}승 {draw}무 {my_lose}패')
    print(f'컴퓨터의 전적: {my_lose}승 {draw}무 {my_win}패')

try:
    games = int(input("몇 판을 진행하시겠습니끼?: "))
    rsp_advanced(games)
except:
    print('올바른 숫자를 입력해 주세요.')
    quit()

