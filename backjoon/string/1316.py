# 1316번 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

N = int(input())

# 그룹 단어의 개수 초기화
result = 0

for _ in range(N):
    string = input()
    L = 0  # string length
    for _ in string:
        L += 1

    # 모든 문자 검색을 위한 idx 초기화
    idx = 0
    # 문자 등장 여부 확인을 위한 딕셔너리
    d = {}
    while idx < L:
        # 만약 문자가 등장하지 않았다면? 딕셔너리 추가
        if string[idx] not in d:
            d[string[idx]] = True
            if idx:
                # 다음 문자열이 나타났으므로 다시 나타났을 때 틀림을 알림
                d[string[idx-1]] = False
            idx += 1
        else:
            # 이미 등장한 문자가 직전에 존재한다면 다음 인덱스로!
            if d[string[idx]]:
                idx += 1
            # 이미 등장했었는데 직전의 문자가 아니라면 종료!
            else:
                break
        # 전체 문자열을 탐색했을 때 중단되지 않았다면 그룹 단어!
        if idx == L:
            result += 1

print(result)
