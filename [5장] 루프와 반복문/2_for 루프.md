## for 루프

- 학습목표: 파이썬에서의 반복작업은 어떤식으로 수행되는지 이해하고 활용할 수 있다.
- 핵심 키워드: for 루프

<br></br>

유한 루프는 4자기 키워드를 사용한다. 유한 루프의 개념은 어떤 집합의 원소들에 대해 반복문을 실행한다는 것이다.
집합이 무엇이든 루프가 실행되는 집합에 따라 유한 번 실행된다. 유한 루프는 집합의 원소를 통해 반복한다.

<br/>

#### for 루프

하나의 파일에 들어 있는 문장의 갯수와 리스트 안에 들어 있는 항목들의 수는 유한하다. 유한개의 항목들에 대해 우리가 특정 조치들을 취하고 싶을 때 for 루프를 사용한다.

```python
for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')

# 5
# 4
# 3
# 2
# 1
# Blastoff!

# 순차적으로 출력된다.
```

문자열 리스트에서도 동일한 방식으로 출력할 수 있다.

```python
friends = ['Connect', 'Korea', 'NHN']
for friend in friends:
    print('Happy New Year!! ', friend)
print('Done!')
# Happy New Year!!  Connect
# Happy New Year!!  Korea
# Happy New Year!!  NHN
# Done!
```

for 루프는 while 루프에서 개별적인 구문들이 하는 일을 한 번에 처리한다. 먼저 루프를 몇 번 실행할지 결정한다. 따라서 루프가 끝났는지 물어보는 질문에 어떤 방향으로 실행할지 결정한다.
앞의 while 루프 예시에서는 루프를 제어하기 위해 3줄의 코드가 필요했지만 for 루프에서는 그렇지 않다.