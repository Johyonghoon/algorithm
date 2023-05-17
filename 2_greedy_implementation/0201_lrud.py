class LRUD:

    def solution(self, n, plans):
        x, y = 1, 1
        for plan in plans:
            if plan == "U" and x > 1:
                x = x - 1
            elif plan == "D" and x <= n:
                x = x + 1
            elif plan == "L" and y > 1:
                y = y - 1
            elif plan == "R" and y <= n:
                y = y + 1
        print(x, y)

    def teacher_solution(self, n, plans):
        x, y = 1, 1
        # L, R, U, D에 따른 이동 방향
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        move_types = ['L', 'R', 'U', 'D']

        # 이동 계획을 하나씩 확인하기
        for plan in plans:
            for i in range(len(move_types)):
                if plan == move_types[i]:
                    nx = x + dx[i]
                    ny = y + dy[i]

            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            x, y = nx, ny

        print(x, y)


if __name__ == '__main__':
    n = int(input("숫자 N을 입력하세요 : "))
    plans = input("계획서를 입력하세요 : ").split()
    # LRUD().solution(n, plans)
    LRUD().teacher_solution(n, plans)
