def check_id(id):
    front_num = id.split('-')[0]
    back_num = id.split('-')[1]
    year = front_num[:2]
    month = front_num[2:4]

    if int(year) >= 00 and int(year) <= 21:
        question = input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x:')

        if question == 'o' and (back_num[0] != '3' and back_num[0] != '4'):
            print('잘못된 번호입니다.\n올바른 번호를 넣어주세요.')
            quit()

    if back_num[0] == '1' or back_num[0] == '3':
        gender = '남자'
    elif back_num[0] == '2' or back_num[0] == '4':
        gender = '여자'
    else:
        print('잘못된 번호입니다.')
        quit()

    print(f'{year}년{month}월 {gender}')


id = input("주민등록번호('-' 포함 14자리 입력): ")
check_id(id)