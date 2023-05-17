class CountTime:

    def solution(self, n):
        hours = range(n+1)
        minutes = range(60)
        seconds = range(60)
        count = 0

        for hour in hours:
            for minute in minutes:
                for second in seconds:
                    time = f"{hour}:{minute}:{second}"
                    if time.find("3") != -1:
                        count += 1

        print(count)


if __name__ == '__main__':
    n = int(input("N값을 입력하세요 : "))
    CountTime().solution(n)

