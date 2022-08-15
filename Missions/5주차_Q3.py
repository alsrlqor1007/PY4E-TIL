import random


def guess_numbers():
    computer_nums = list()
    while len(computer_nums) < 3:
        number = random.randint(0, 100)
        if number not in computer_nums:
            computer_nums.append(number)
    computer_nums.sort()

    chance = 1
    count = 3
    check = [False, False, False]
    submits = list()

    while count > 0:
        try:
            print(f'{chance}차 시도')
            guess = int(input('숫자를 예측해 보세요: '))

            if guess not in list(range(0, 101)):
                print('0부터 100 사이의 숫자만 입력해 주세요.\n')
                continue
            elif guess in submits:
                print('이미 예측에 사용한 숫자입니다.\n')
                continue

            if guess in computer_nums:
                if guess == computer_nums[0]:
                    check[0] = True
                    print(f'숫자를 맞추셨습니다! {guess}는 최솟값입니다.\n')
                elif guess == computer_nums[1]:
                    check[1] = True
                    print(f'숫자를 맞추셨습니다! {guess}는 중간값입니다.\n')
                else:
                    check[2] = True
                    print(f'숫자를 맞추셨습니다! {guess}는 최댓값입니다.\n')

                if count - 1 == 0:
                    print(f'게임종료\n{chance}번 시도만에 예측 성공')

                submits.append(guess)
                chance += 1
                count -= 1
            else:
                print(f'{guess}은(는) 없습니다.')

                if chance <= 5 and check[0] == False:
                    if guess < computer_nums[0]:
                        print(f'최솟값은 {guess}보다 큽니다.\n')
                    else:
                        print(f'최솟값은 {guess}보다 작습니다.\n')
                elif chance <= 10 and check[2] == False:
                    if guess < computer_nums[2]:
                        print(f'최댓값은 {guess}보다 큽니다.\n')
                    else:
                        print(f'최댓값은 {guess}보다 작습니다.\n')
                else:
                    if guess < computer_nums[1]:
                        print(f'중간값은 {guess}보다 큽니다.\n')
                    else:
                        print(f'중간값은 {guess}보다 작습니다.\n')

                submits.append(guess)
                chance += 1

        except:
            print('올바른 숫자로 입력해 주세요.\n')
            continue


guess_numbers()
