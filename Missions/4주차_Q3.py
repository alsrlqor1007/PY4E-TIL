def wrong_guest_book(guest_book):
    guest_book_handler = open('guest_book.txt', 'w')
    guest_book_handler.write(guest_book)
    guest_book_handler.close()

    guest_book_list = open('guest_book.txt', 'r')
    for line in guest_book_list:
        name = line.split(',')[0]
        phone_number = line.split(',')[1]

        if len(phone_number) != 13 or not phone_number.startswith('010-') or phone_number[8] != '-':
            print(f'잘못 쓴 사람: {name}')
            print(f'잘못 쓴 번호: {phone_number}')


guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""

wrong_guest_book(guest_book)