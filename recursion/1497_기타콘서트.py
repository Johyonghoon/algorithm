# 1497번 기타콘서트
# https://www.acmicpc.net/problem/1497

N, M = map(int, input().split())
songs = [0 for _ in range(M)]
guitars = []
arr = []
result = []
maxi_song = 0
mini_guitar = N
for _ in range(N):
    name, info = input().split()
    arr.append([name, tuple(info)])

def recur(idx):
    global maxi_song, mini_guitar
    if idx == N:
        cnt_song = len(songs) - songs.count(0)
        maxi_song = max(maxi_song, cnt_song)
        if maxi_song == cnt_song:
            mini_guitar = min(mini_guitar, len(guitars))
        return
    info = arr[idx][1]
    for i, song in enumerate(info):
        if song == 'Y':
            songs[i] += 1
    guitars.append(arr[idx][0])
    recur(idx+1)
    guitars.pop()
    for i, song in enumerate(arr[idx][1]):
        if song == 'Y':
            songs[i] -= 1
    recur(idx+1)

recur(0)

if mini_guitar:
    print(mini_guitar)
else:
    print(-1)
