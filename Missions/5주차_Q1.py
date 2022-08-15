import random


def bs31():
    round = 1
    cur_last_num = 0

    while True:
        my = input("My turn - 숫자를 입력하세요: ")
        computer_turn_num = random.randint(1, 3)

        my_nums = list()
        for el in my.split():
            my_nums.append(int(el))

        if len(my_nums) > 3 or my_nums != list(range(my_nums[0], my_nums[-1] + 1)):
            print('연속된 숫자로 3개까지 입력 가능합니다.\n')
            continue
        elif my_nums[-1] != int(max(my_nums)):
            print('숫자를 순서대로 입력해 주세요.\n')
            continue
        elif round == 1 and my_nums[-1] not in [1, 2, 3]:
            print('첫 번째 순서는 1부터 시작해야 하며 3까지 가능합니다.\n')
            continue
        elif my_nums[0] != cur_last_num + 1:
            print('현재 숫자의 다음 숫자부터 입력 가능합니다.\n')
            continue
        else:
            cur_last_num = my_nums[-1]
            print(f'현재 숫자: {cur_last_num}')

            if cur_last_num == 30:
                print(f'\n사용자 승리!')
                break

            while computer_turn_num > 0:
                print(f'컴퓨터: {cur_last_num + 1}')
                cur_last_num += 1
                computer_turn_num -= 1

                if cur_last_num == 30:
                    print(f'컴퓨터 승리!')
                    quit()

            print(f'현재 숫자: {cur_last_num}\n')

            round += 1
            continue


print("베스킨라빈스 써리원 게임")
print("------------------")
bs31()


# course reference
def bs31():
    print("베스킨라빈스 써리원 게임")
    print("------------------")
    import random
    number = 0
    while True:
        # my turn
        my = input("My turn - 숫자를 입력하세요: ")
        my = my.split()
        if int(my[0]) != number + 1 or len(my) > 3:
            print("숫자를 제대로 입력하세요")
            continue
        # 숫자 2개 입력 후 연속된 숫자가 아닐 경우 제한
        if len(my) == 2:
            if int(my[1]) - int(my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue
        # 숫자 3개 입력 후 연속된 숫자가 아닐 경우 제한
        if len(my) == 3:
            if int(my[2]) - int(my[1]) != 1 or int(my[1]) - int(my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue

        number = int(my[-1])
        print(f"현재 숫자 : {number}")

        # 31을 넘겼는지 검사
        if number >= 31:
            print("패배")
            break

        # computer
        computer = []
        computer_turn_num = random.randint(1, 3)
        for i in range(computer_turn_num):
            number += 1
            # 컴퓨터가 31이 넘는 수를 외치면 31로 되돌리기
            if number > 31:
                number = number - 1
                continue
            computer.append(number)
            print(f"컴퓨터 : {computer[-1]}")
        print(f"현재 숫자 : {number}")
        print()
        # 31이 있는지 검사
        if 31 in computer:
            print("승리!")
            break
    print("게임 종료")
