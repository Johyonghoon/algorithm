# 2621번 카드게임
# https://www.acmicpc.net/problem/2621

"""
0. R, B, Y, G 4가지 색의 1~9의 숫자가 쓰여진 카드가 각각 9장씩 있다.
   36장의 카드에서 5장을 뽑고, 아래와 같은 규칙으로 정수를 계산
1. 5장이 모두 '같은 색' 이면서 숫자가 연속적일 때, 가장 높은 수에 900을 더한다.
2. 5장 중에 4장의 '숫자가 같을 때' 점수는 같은 숫자에 800을 더한다.
3. 5장 중에 3장의 '숫자가 같고' 나머지 2장의 '숫자가 같을 때'
   3장이 같은 숫자에 10을 곱하고, 2장이 같은 숫자를 더한 다음 700을 더한다.
4. 5장의 카드가 모두 "같은 색일 때" 가장 높은 숫자에 600을 더한다.
5. 5장의 "숫자가 연속적"일 때, 가장 높은 숫자에 500을 더한다.
6. 5장 중 3장의 "숫자가 같을 때" 같은 숫자에 400을 더한다.
7. 5장 중 2장의 "숫자가 같고" 다른 2장의 "숫자가 같을 때"
   같은 숫자 중 큰 숫자에 10을 곱하고, 작은 숫자를 더한 뒤 300을 더한다.
8. 5장 중 2장의 "숫자가 같을 때" 점수가 같은 숫자에 200을 더한다.
9. 어떤 경우에도 해당하지 않을 때 가장 큰 숫자에 100을 더한다.
"""
from collections import defaultdict

# 입력 정보 받기
dict_color = defaultdict(int)
dict_number = defaultdict(int)
numbers = set()
cards = []
for _ in range(5):
    c, n = list(input().split())
    cards.append([c, int(n)])
    dict_color[c] += 1
    dict_number[int(n)] += 1
    numbers.add(int(n))

cards.sort()

breaky = False
score = 100 + max(numbers)

# 카드 5장이 모두 같은 색인 1번과 4번 경우를 처리
for color, cnt in dict_color.items():
    if cnt == 5:
        for idx in range(4):
            if cards[idx][1] + 1 != cards[idx+1][1]:
                breaky = True
                break
        else:
            score = max(score, 900 + cards[-1][1])

        if breaky:
            score = max(score, 600 + cards[-1][1])

for number, cnt in dict_number.items():
    # 2. 카드 5장 중 4장의 숫자가 같을 때
    if cnt == 4:
        score = max(score, 800 + number)
        break
    # 카드 5장 중 3장의 숫자가 같을 때
    elif cnt == 3:
        # 3. 다른 두 장의 숫자가 같은 경우
        if 2 in dict_number.values():
            number2 = 0
            for num in numbers:
                if num != number:
                    number2 = num
                    break
            score = max(score, 700 + number * 10 + number2)
            break
        # 6. 다른 두 장의 숫자가 같지 않고, 3장의 숫자만 캍을 때
        else:
            score = max(score, 400 + number)
            break
    elif cnt == 2:
        # 7. 5장 중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때
        if list(dict_number.values()).count(2) == 2:
            n2 = []
            for k, v in dict_number.items():
                if v == 2:
                    n2.append(k)
            n2.sort()

            score = max(score, 300 + n2[1] * 10 + n2[0])
            break
        # 8. 5장 중 2장의 숫자만 같을 때
        else:
            score = max(score, 200 + number)

# 5. 카드 5장의 숫자가 연속적일 때
numbers = sorted(list(numbers))
# 모든 숫자가 달라야 하니까 set에서는 같은 숫자가 생기면 5보다 작아진다.
if len(numbers) == 5:
    for idx in range(4):
        if numbers[idx] + 1 != numbers[idx + 1]:
            break
    else:
        score = max(score, 500 + numbers[-1])

print(score)


"""
1.
B 1
B 2
B 3
B 4
B 5
905

2.
B 4
Y 4
G 4
R 4
B 1
804

3.
B 4
Y 4
G 4
R 2
B 2
742

4.
B 1
B 2
B 3
B 4
B 6
606

5.
B 1
B 2
B 3
B 4
G 5
505

6.
G 3
B 4
Y 5
G 6
B 7
507

7.
G 3
G 7
B 3
B 7
Y 1
373

8. 
G 3
G 7
B 3
B 6
Y 1
203

9. 
G 9
G 7
B 3
B 6
Y 1
109

Y 4 
Y 3 
Y 2 
Y 5 
Y 6
906


"""