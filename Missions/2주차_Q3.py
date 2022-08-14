try:
    name = str(input('학생 이름: '))
    score = int(input('점수: '))
except:
    print('이름은 문자로, 점수는 정수로 입력해주세요.')
    quit()

def grader(name, score):
    if score < 60:
        grade = 'F'
    elif score <= 64:
        grade = 'D'
    elif score <= 69:
        grade = 'D+'
    elif score <= 74:
        grade = 'C'
    elif score <= 79:
        grade = 'C+'
    elif score <= 84:
        grade = 'B'
    elif score <= 89:
        grade = 'B+'
    elif score <= 94:
        grade = 'A'
    else:
        grade = 'A+'

    print('학생이름: ', name)
    print('점수: ', score, '점')
    print('학점: ', grade)

grader(name, score)