import sys
sys.stdin = open('1952.txt')


T = int(input())

for tc in range(1, T+1):
    dx = [0, 1, 0, -1]          # 오른쪽, 아래, 왼쪽, 위 순으로 움직이기 때문에
    dy = [1, 0, -1, 0]          # 인덱스 0부터 오른쪽, 아래, 왼쪽, 위 움직이게 해줌

    n = int(input())
    arr = [[0]*n for i in range(n)]
    cnt = 0
    x, y = 0, 0

    for j in range(1, n*n+1):
        arr[x][y] = j
        x, y = x + dx[cnt], y + dy[cnt]             #

        # x 또는 y가 범위를 벗어나거나 이미 0이 아닌 수가 입력되어 있으면
        if x < 0 or x >= n or y < 0 or y >= n or arr[x][y] != 0:
            x, y = x - dx[cnt], y - dy[cnt]         # x, y 원위치
            cnt = (cnt+1)%4                         # 계속 더해지면 cnt가 dx,dy범위 넘어가므로 나머지로 cnt만들기
            x, y = x + dx[cnt], y + dy[cnt]         # 바뀐 cnt로 다시 좌표 계산

    print(f'#{tc}')
    for i in arr:
        print(*i)







