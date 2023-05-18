# 1157번 단어 공부
# https://www.acmicpc.net/problem/1157

text = input().upper()
dic = {}
for i in text:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
sorted_by_value = sorted(dic.items(), key=lambda x: x[1], reverse=True)
if len(sorted_by_value) == 1:
    print(sorted_by_value[0][0])
else:
    if sorted_by_value[0][1] == sorted_by_value[1][1]:
        print("?")
    else:
        print(sorted_by_value[0][0])
