## 조건문(elif)과 예외처리(try, except)

- 학습목표: 다중 분기(Multi-way Decision) 조건문을 이해하고 사용할 수 있다. try / except 문을 이용하여 오류를 처리 할 수 있다.
- 핵심 키워드: 다중 분기 (Multi-way Decision), try / except

<br></br>

#### 다중 분기(Multi-way decisions)

하나의 조건문 블럭에 조건문들을 추가할 수 있다. `elif`라는 예약어를 통해서 가능하다.
elif 예약어는 2개 이상 사용할 수 있으며, 조건삭에 해당되면 조건문은 종료되기 때문에 순서가 중요하다.

```python
x = 21

if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
elif x < 20 :
    print('Big')
elif x < 40 :
    print('Large')
elif x < 100 :
    print('Huge')
else :
    print('Ginormous')

# Large 출력
```

<br/>

#### try / except

`try/except`로 발생할 수 있는 error에 대해 미리 대처를 할 수 있다.
try문의 코드를 수행하고 error일 경우 except문의 코드를 싫행한다. 즉, except문은 에러가 떴을 때 진행해야 할 일을 한다.

```python
rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
excpet:
    ival = -1
    
if ival > 0:
    print('Nice Work')
else:
    print('Not a number')

$ python3 trynum.py
Enter a number: 42
Nice Work
$ python3 trynum.py
Enter a number: forty-two
Not a number
```

```python
astr = "123"

try:
    print("Hello")
    isInt = int(astr)
    print("World")
except:
    isInt = "Integer로 변환할 수 없습니다."

print('Done', isInt)
# Hello
# World
# Done 123이 순서대로 출력
```