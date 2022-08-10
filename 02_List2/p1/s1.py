T = int(input())

def sol(n, arr):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    total = 0                                       # 총합
    for i in range(n):
        for j in range(n):
            for k in range(4):                      # 상,하,좌,우 총 4번 반복
                ni, nj = i + dx[k], j + dy[k]       # arr[i][j]에 dx,dy의 k번째씩 더하며 상하좌우 탐색하여 좌표생성
                if 0 <= ni < n and 0 <= nj < n:     # 새 좌표가 arr을 벗어나지 않으면
                    total += abs(arr[i][j] - arr[ni][nj])   # 현재좌표 - 새 좌표 에 절댓값을 씌워 추가
    return total

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    print(f'#{tc} {sol(n, arr)}')

