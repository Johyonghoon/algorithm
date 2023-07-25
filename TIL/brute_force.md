# 완전 탐색 (Brute Force)

### Brute Force : 무식한 힘

즉, 가능한 **모든 경우의 수를 모두 탐색**하며 요구조건에 충족되는 결과를 찾는 과정

#### Q1. 비밀번호 [BOJ 1816](https://www.acmicpc.net/problem/1816)

>확인하고자 하는 수가 주어진다.
>
>확인하고자 하는 수가 적절한 비밀번호인지 아닌지를 구하는 프로그램을 작성하라.
>
>적절하다면 YES, 적절하지 않다면 NO 를 출력한다.
>
>적절한 비밀번호
>
>- 모든 소인수가 1,000,000 보다 크다면 적절한 비밀번호
>- 소인수? 1을 제외한 약수

>```
># input
>3
>1000036000099
>1500035500153
>20000000000002
># output
>
>```

#### A1. 수업을 듣지 않았을 때 풀이 방법

```py
def prime_number(x):
    for i in range(2, int(1e6)):
        if x % i == 0:
            return False
    return True


n = int(input())
for _ in range(n):
    x = int(input())
    if prime_number(x) is True:
        print("YES")
    else:
        print("NO")
```

* 1,000,000 까지의 수를 모두 나누어 본다면 2의 배수 등 중복되게 계산해보는 것이 존재
* 이에 따라, 소수를 구하여 1,000,000 까지의 소수를 모두 나누어보는 과정을 수행하여 효율적으로 계산

#### A2. 수업의 풀이 방법

```py
TC = int(input())

for _ in range(TC):
    pw = int(input())

    for i in range(2, 1_000_001):
        if pw % i == 0:
            print("NO")
            break
        if i == 1_000_000:
            print("YES")
```

* 모든 경우의 수를 연산
* 가능한 **모든 경우의 수**를 계산해보는 것!
* 어떤 문제든지, 경우의 수가 보인다면
* 시간과 메모리가 충분히 주어진다면
* 완전 탐색으로 문제를 해결할 수 있다!



#### Q2. 사탕 [BOJ 14568](https://www.acmicpc.net/problem/14568)

> 친구 A B C 에게 사탕을 나누어주려고 한다.
>
> 조건은 다음과 같다.
>
> 1. 남는 사탕이 없어야 한다.
> 2. A 는 B 보다 2개 이상 많은 사탕을 가져야 한다.
> 3. 셋 중 사탕을 하나도 받지 못하는 친구는 없다.
> 4. C가 받는 사탕의 수는 짝수이다.

> input / output
>
> ```
> # input
> 6
> # output
> 1
> ```

#### A1. 수업을 듣지 않았을 때 풀이 방법

```py 
n = int(input())
cnt = 0
for i in range(1, n):
    for j in range(i+2, n):
        x = n - i - j
        if x <= 0:
            break
        if x % 2 == 0:
            cnt += 1

print(cnt)
```

#### A2. 수업의 풀이 방법

```py
candy = int(input())
cnt = 0

for A in range(0, candy+1):
    for B in range(0, candy+1):
        for C in range(0, candy+1):
            if A + B + C == candy:
                if A >= B + 2:
                    if A != 0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            cnt += 1
```

* 굳이 미리 조건의 식을 코드에 반영할 필요가 없다.
* 모든 경우의 탐색하고, 조건에 해당하지 않는다면 다음 경우의 수로 넘어가는 것!



#### Q3. 연립방정식 [BOJ 19532](https://www.acmicpc.net/problem/19532)

>숫자 A B C D E F 가 주어진다.
>
>다음 연립방정식에서 x와 y 값을 계산하는 프로그램을 작성
>
>```
>Ax + By = C
>Dx + Ey = F
>```
>
>범위
>
>* X와 Y는 -999 이상 999 이하인 정수이다

#### A1. 수업을 듣지 않았을 때 풀이방법

```py
a, b, c, d, e, f = map(int, input().split())
print((c * e - b * f) // (a * e - b * d), (c * d - a * f) // (b * d - a * e))
"""
y = (cd - af) / (bd - ae)
x = (ce - bf) / (ae - bd)
"""
```

#### A2. 수업의 풀이방법

```py
A, B, C, D, E, F = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if A * x + B * y == C:
            if D * x + E * y == F:
                print(x, y)
                break
```

* 파이썬 1초 약 1억번의 연산 가능!



#### Q4. 숫자야구 [BOJ 2503](https://www.acmicpc.net/problem/2503)

> A는 3자리 숫자로 된 정답을 하나 정한다.
>
> B는 3자리 숫자를 제시해서 A가 생각하고 있는 정답을 맞히려고 한다.
>
> B가 말한 숫자가 정답에 포함되어 있다면 1 Ball 
>
> B가 말한 숫자가 정답에 포함되어 있고, 자리도 동일하다면 1 Strike
>
> 다른 숫자로 이루어진 세 자리 수
>
> Strike 와 Ball 의 결과를 보고, 가능한 숫자를 계산하는 프로그램을 작성

> ```py
> # input
> 4
> 123 1 1
> 356 1 0
> 327 2 0
> 489 0 1
> ```

#### A1. 내 풀이

```py
n = int(input())
arr = []
result = 0
for i in range(n):
    ans, strike, ball = map(int, input().split())
    arr.append([ans, strike, ball])

# 완전 탐색
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a != b and a != c and b != c:
                cnt_case = 0
                for i in range(n):
                    ans, strike, ball = arr[i]
                    cnt_strike, cnt_ball = 0, 0
                    x = ans // 100
                    y = ans // 10 % 10
                    z = ans % 10
                    if a == x: cnt_strike += 1
                    if a == y or a == z: cnt_ball += 1
                    if b == y: cnt_strike += 1
                    if b == x or b == z: cnt_ball += 1
                    if c == z: cnt_strike += 1
                    if c == x or c == y: cnt_ball += 1
                    if cnt_strike == strike and cnt_ball == ball: cnt_case += 1
                    if cnt_case == n: result += 1

print(result)
```

#### A2. 수업의 풀이방법

```py
n = int(input())  # 4

# [[123, 1, 1], [356, 1, 0], ...]
hint = [list(map(int, input().split())) for _ in range(4)]

answer = 0
# 100 ~ 999
for a in range(1, 10):  # 100의 자리 수
    for b in range(10):  # 10의 자리 수
        for c in range(10):  # 1의 자리 수
            
            if (a == b or b == c or c == a):
                continue
            
            # 숫자가 정해졌다면
            cnt = 0
            for arr in hint:
                number = hint[0]
                ball = hint[1]
                strike = hint[2]
                
                # a, b, c 라는 숫자를
                # number과 비교해서
                # 자릿수를 나눠서, strike ball 을 판단하는 부분
                
                ball_count = 0
                strike_count = 0
                
                if ball == ball_count and strike == strike_count:
                    cnt += 1
            
            if cnt == n:
                answer += 1
                
print(answer)
```

