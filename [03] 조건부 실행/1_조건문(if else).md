## 조건문(if else)

- 학습목표: 조건부 실행(Conditional Execution)에 대해서 알아보려 합니다. 조건부 실행은 우리의 코드가 무언가가 검사를 하거나 결정을 내릴 때 사용합니다. 파이썬이 명령문을 실행시키거나 넘어가는 방법을 알아보도록 하겠습니다.
- 핵심 키워드: 조건부 실행 (Conditional Execution), 들여쓰기, if, else

<br></br>

파이썬에서 조건문을 통해 두 방향으로 갈 수 있다. 

#### if 문

`if`는 예약어이며, 질문이 포함되어 있다.

```python
x = 5

if x < 10: # if는 예약어이며, 컴퓨터는 if 다음에 나오는 조건문의 True, False를 판단 
  print('Smaller') # 만약 True인 경우 :(콜론) 아래로 들여쓰기 된 부분 실행
                   # 여기서는 Smaller가 출력
```

<br/>

#### 비교연산자

조건문의 참 또는 거짓을 판별하기 위해 사용되는 비교 연산자들이 있다. 다음과 같은 비교 연산자들을 사용한다.

<div align="center">

<img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0997b5d2-82fa-4d1d-9bd8-91dab05d451e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-07-22_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.29.13.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220722T143143Z&X-Amz-Expires=86400&X-Amz-Signature=15ff4721d8e7051e60bcec66f7f9d8d6b120a36e3769a2410ede4f121b571044&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA%25202022-07-22%2520%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE%252011.29.13.png%22&x-id=GetObject"/>

</div>

<br/>

#### 들여쓰기 (indentation)

파이썬에서는 들여쓰기를 매우 엄격하게 생각한다. 들여쓰기가 제대로 되어 있지 않다면 파이썬은 문법 에러를 반환한다.
블록이 시작하고 끝나는 부분을 표시하기 위해 자주 사용한다. 들여쓰기를 하면 같은 블록에 있는 이상 들여쓰기를 하고 블록이 끝나면 내어쓰기를 한다.
내어쓰기에서 주석과 빈 줄은 모두 무시된다. 들여쓰기를 통해 내어쓰기를 하기 전까지의 코드들을 모두 포함해 블록을 만들게 된다.

```python
x = 5

if x < 10:
  print('Smaller')
```

조건문에서 x가 가진 값이 10보다 작기 때문에 Smaller가 출력된다. 하지만, 들여쓰기를 제대로 하지 않았기 때문에 파이썬은 아래와 같이 들여쓰기 에러를 나타낸다.

```python
  File "part2.py", line 4
    print('Smaller')
        ^
IndentationError: expected an indented block
```

통상 들여쓰기는 [Tab] 또는 [Space] 네 번과 같다. 컴퓨터가 탭을 잘못 인식하는 경우도 있으므로 Tab 보다는 Space 네 번 사용을 권장한다.

<br/>

#### 단일 if 문

단일 if문으로 사용하는 경우, 조건문이 참인 경우에만 미리 입력해 놓은 실행코드를 실행한다.

```python
x = 5

if x < 10:
  print('Smaller')
```

<br/>

#### if else 문

첫 번째 조건문의 조건이 거짓인 경우에 대해 처리하기 위해 else를 사용할 수 있다. 즉, 첫번째 if문의 조건이 거짓인 경우 else문 이하의 실행코드가 실행된다.

```python
x = 11

if x < 10:
  print('Smaller')
else:
  print('Bigger'))
  
# 11 < 10은 False
# 따라서 Bigger 출력
```

<br/>

#### 주의사항

조건문(if, else)을 사용할 때에는 주의할 점이 2가지가 있다.

1. 조건문 후에 :(콜론)을 찍어야 한다.
2. 조건문이 참일 경우 실행할 코드는 들여쓰기를 해야 한다.

<br/>

### 참고

- [조지 불](https://ko.wikipedia.org/wiki/%EC%A1%B0%EC%A7%80_%EB%B6%88)