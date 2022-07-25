## while 루프

- 학습목표: 파이썬에서의 반복작업은 어떤식으로 수행되는지 이해하고 활용할 수 있다.
- 핵심 키워드: while 루프

<br></br>

#### while 루프

while과 :(콜론)사이에 오는 조건문이 참의 값을 가지는 경우에는 :(콜론)이하의 코드가 반복해서 작동한다.
통상적으로 while문을 자주 사용하게 된다면 작성한 코드를 되돌아볼 필요가 있다. 물론 while은 반복적으로 작업할 수 있도록 해주는 편리한 문법이지만 무한루프에 빠질 수 있는 단점도 내포하고 있기 때문이다.

```python
n = 5

while n > 0:
    print(n)
    n = n - 1

print('Blastoff!')
print(n)
```

<br/>

#### break

루프가 break를 만나게 되면 해당 루프는 실행이 종료 되고 while문 바로 뒤의 코드를 실행한다.

```python
while True:
    line = input('> ') 
    if line == 'done':
        break
    print(line)
print('Done!')

# > hello there로 입력
# hello there로 출력됨
# > finished로 입력
# finished로 출력됨
# > done로 입력
# Done!으로 출력됨
```
<br/>

#### continue

루프가 continue를 만나게 되면 해당 루프는 실행이 종료되고 루프가 시작된 지점부터 다시 루프를 실행한다.

```python
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

# > hello there 입력
# hello there로 출력
# # don't print this '#'을 입력하게 되면 continue를 만나게 되고 continue는 loop의 시작점으로 다시 돌아가서 loop를 실행하게 됩니다.
# > print this! 입력
# print this!로 출력
# > done 입력
# Done!으로 출력 done을 입력하게 되면 break를 만나게 되고 break는 loop끝나는 점 바로 다음에 오는 코드를 실행하게 됩니다.
```

<br/>