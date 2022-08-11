import sys
sys.stdin = open('1210.txt')

T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    x, y = 99, arr[99].index(2)     # 도착점에서부터 시작

    while x > 0:                    # 출발선 도착하기 전까지
        arr[x][y] += 1              # 지나온 곳에 +1 (다시 되돌아갈 일 없게하기 위해)
        # y가 범위 밖으로 벗어나지 않고, 현재 좌표의 왼쪽이 1이라면
        if y - 1 > 0 and arr[x][y-1] == 1:
            y = y - 1       # 왼쪽으로 이동
        # y가 범위 밖으로 벗어나지 않고, 현재 좌표의 오른쪽이 1이라면
        elif y + 1 <= 99 and arr[x][y+1] == 1:
            y = y + 1       # 오른쪽으로 이동
        else:               # 양쪽에 1이 없으면
            x -= 1          # 위로 이동

    print(f'#{tc} {y}')

