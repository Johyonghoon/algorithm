class KnightOfRoyal:

    def solution(self, position):
        number_of_case = 0
        x = ord(position[0]) - 96
        y = int(position[1])
        # print(x, y)

        dx = [-2, -2, 2, 2, -1, 1, -1, 1]
        dy = [-1, 1, -1, 1, -2, -2, 2, 2]
        move_types = ["L1", "L2", "R1", "R2", "U1", "U2", "D1", "D2"]

        for i in range(len(move_types)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or nx > 8 or ny < 1 or ny > 8:
                continue
            number_of_case += 1

        print(number_of_case)

    def teacher_solution(self, position):
        row = int(position[1])
        column = int(ord(position[0]) - int(ord("a")) + 1)
        steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

        result = 0
        for step in steps:
            next_row = row + step[0]
            next_column = column + step[1]
            if 1 <= next_row <= 8 and 1 <= next_column <= 8:
                result += 1

        print(result)


if __name__ == '__main__':
    while True:
        position = input("나이트의 위치를 입력하세요 : ")
        # KnightOfRoyal().solution(position)
        KnightOfRoyal().teacher_solution(position)

