# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"


def good_customer(info):
    info_list = info.split(',')

    categorization = dict()
    categorization['아이디'] = list()
    categorization['나이'] = list()
    categorization['전화번호'] = list()
    categorization['성별'] = list()
    categorization['지역'] = list()
    categorization['구매횟수'] = list()

    for el in info_list:
        left_over = info_list.index(el) % 6

        if left_over == 0:
            categorization['아이디'].append(el)
        elif left_over == 1:
            categorization['나이'].append(el)
        elif left_over == 2:
            if el == 'x':
                categorization['전화번호'].append('000-0000-0000')
            else:
                categorization['전화번호'].append(el)
        elif left_over == 3:
            categorization['성별'].append(el)
        elif left_over == 4:
            categorization['지역'].append(el)
        elif left_over == 5:
            categorization['구매횟수'].append(int(el))

    print(categorization)

    for idx in range(len(categorization['구매횟수'])):
        customer_id = categorization['아이디'][idx]
        age = categorization['나이'][idx]
        phone_number = categorization['전화번호'][idx]
        gender = categorization['성별'][idx]
        region = categorization['지역'][idx]
        purchase_count = categorization['구매횟수'][idx]

        if purchase_count >= 8 and phone_number != '000-0000-0000':
            print(
                f'할인 쿠폰을 받을 회원정보 아이디:{customer_id}, 나이:{age}, 전화번호:{phone_number}, 성별:{gender}, 지역:{region}, 구매횟수:{purchase_count}')


good_customer(info)
