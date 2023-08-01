from collections import Counter

arr = []
for _ in range(10):
    arr.append(int(input()))

print(sum(arr) // 10)
ans = Counter(arr).most_common(1)
print(ans[0][0])
