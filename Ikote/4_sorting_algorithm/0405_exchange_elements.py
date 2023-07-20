def solution(n, k):
    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] > b[i]:
            break
        a[i], b[i] = b[i], a[i]
    print(sum(a))


if __name__ == '__main__':
    n, k = map(int, input("N K 값을 공백을 기준으로 구분하여 입력하세요. : ").split(" "))
    a = list(map(int, input("배열 A의 원소들을 공백을 기준으로 구분하여 입력하세요. : ").split(" ")))
    b = list(map(int, input("배열 B의 원소들을 공백을 기준으로 구분하여 입력하세요. : ").split(" ")))
    solution(n, k)
