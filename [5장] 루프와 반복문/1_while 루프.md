## while 루프

- 학습목표: 파이썬에서의 반복작업은 어떤식으로 수행되는지 이해하고 활용할 수 있다.
- 핵심 키워드: while 루프

<br></br>

#### while 루프

`while`과 `:(콜론)`사이에 오는 `조건문`이 참의 값을 가지는 경우에는 :(콜론)이하의 코드가 반복해서 작동한다.
통상적으로 while문을 자주 사용하게 된다면 작성한 코드를 되돌아볼 필요가 있다. 물론 while은 반복적으로 작업할 수 있도록 해주는 편리한 문법이지만 무한루프에 빠질 수 있는 단점도 내포하고 있기 때문이다.

루프를 제어하기 위해 설계한 이 변수를 `반복 변수`라고 한다. 루프가 몇 번 실행될지 또는 몇 번 반복할지 알려주기 때문이다.
```python
n = 5

while n > 0:
    print(n)
    n = n - 1

print('Blastoff!')
print(n)

# 5
# 4
# 3
# 2
# 1
# Blastoff!
# 0
```

조건문에 따라 한 번도 실행되지 않는 반복문은 `제로 트립`이라고 한다. 단 한 번의 실행도 보장하지 않는다. 이런 관점에서 if 구문과 동일하다. 처음으로 루프를 지날 때 참이 아니라면 바로 건너뛴다.
그리고는 다시 돌아가지 않는다. 따라서 한 번 break하면 해당 루프는 끝난다.

<br/>

#### break

루프가 `break`를 만나게 되면 해당 루프는 실행이 종료되고 while문 바로 뒤의 코드를 실행한다. 가장 안 쪽의 루프에서 루프의 마지막 줄 다음으로 빠져나온다.


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

루프가 `continue`를 만나게 되면 해당 루프는 실행이 종료되고 루프가 시작된 지점부터 다시 루프를 실행한다.
continue는 break와 다르게 이번 회차의 실행을 멈추고 루프의 최상단으로 다시 올라가서 수행한다.

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

while문으로 만들어 온 반복문을 `불확정 루프`라고 한다. break를 만나거나 이떤 값이 참일 동안 계속해서 실행되기 때문이다. 
하지만 코드가 길어지고 복잡해질 경우 해당 로직이 종료될 수 있는지 불분명하다. 따라서 대부분의 반복문을 만들기 위해서는 `유한 루프`라고 하는 것을 사용한다.
<br/>