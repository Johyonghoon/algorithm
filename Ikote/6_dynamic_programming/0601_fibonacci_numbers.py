from utils import my_menu


class Fibonacci:

    def fibo_dp_topdown(self, x):
        if x == 1 or x == 2:
            return 1
        if d[x] != 0:
            return d[x]
        d[x] = self.fibo_dp_topdown(x - 1) + self.fibo_dp_topdown(x - 2)
        return d[x]

    def fibo_dp_bottomup(self, n):
        d[1] = 1
        d[2] = 1
        for i in range(3, n + 1):
            d[i] = d[i - 1] + d[i - 2]
        print(d[n])


MENUS = ["종료",  # 0
         "피보나치 탑다운 다이나믹 프로그래밍",  # 1
         "피보나치 바텀업 다이나믹 프로그래밍",  # 2
         ]


if __name__ == '__main__':
    fb = Fibonacci()
    while True:
        menu = my_menu(MENUS)
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            d = [0] * 100
            x = int(input())
            print(fb.fibo_dp_topdown(x))
        elif menu == "2":
            d = [0] * 100
            x = int(input())
            fb.fibo_dp_bottomup(x)
        else:
            print("잘못된 입력입니다.")
