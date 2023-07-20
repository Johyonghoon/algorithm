if __name__ == '__main__':
    n = int(input("식량창고의 개수 N 값을 입력하세요. : "))
    ls = list(map(int, input("각 식량창고에 저장된 식량의 개수를 공백을 기준으로 입력하세요. : ").split()))
    d = [0] * n
    d[0] = ls[0]
    d[1] = max(ls[0], ls[1])
    for i in range(2, n):
        d[i] = max(d[i-2] + ls[i], d[i-1])
    print(d[n-1])
