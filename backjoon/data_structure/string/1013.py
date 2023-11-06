# 1013번 Contact
# https://www.acmicpc.net/problem/1013

T = int(input())
left = [1, 0, 0]    # 100+1+
right = [0, 1]      # 01
for tc in range(1, T+1):
    S = list(map(int, list(input())))

    idx = len(S)-1
    isPossible = True
    while idx >= 0:
        # print(idx)
        if S[idx] == 1:
            idx -= 1
            if idx >= 0 and S[idx] == 0:
                idx -= 1
                # 종료 또는 새로운 전파 생성
                if idx < 0 or S[idx] == 1:
                    continue
                # left 만 가능
                if idx >= 0 and S[idx] == 0:
                    idx -= 1
                    while idx >= 0 and S[idx] == 0:
                        idx -= 1
                    # while문이 종료될 경우 1이어야 한다.
                    if idx < 0 or S[idx] == 0:
                        isPossible = False
                        break
                    # 1일 경우 패스
                    idx -= 1
                else:
                    isPossible = False
                    break
            # left 만 가능
            elif idx >= 0 and S[idx] == 1:
                idx -= 1
                while idx >= 0 and S[idx] == 1:
                    idx -= 1
                cnt = 0
                while idx >= 0 and S[idx] == 0:
                    cnt += 1
                    idx -= 1
                if cnt < 2:
                    isPossible = False
                    break
                # S[idx] = 1 일 경우만 넘어옴
                if idx >= 0:
                    idx -= 1
                else:
                    isPossible = False
            else:
                isPossible = False

        else:
            isPossible = False

        if not isPossible:
            break

    if isPossible:
        print("YES")
    else:
        # print(idx)
        print("NO")
