import sys
sys.stdin = open('input.txt')

dx = [1, 1, -1, -1]                                                 # 대각선 시계방향으로 도는
dy = [1, -1, -1, 1]                                                 # 델타

def dfs(x, y, d, tmp):
    global result, i, j

    nx = x + dx[d]
    ny = y + dy[d]

    if d == 3 and nx == i and ny == j:                              # 방향을 세 번 바꿨고 다시 출발점으로 돌아왔으면
        result = max(result, len(tmp))                              # 최댓값 갱신
        return

    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] not in tmp:      # 범위 안에 있고 같은 숫자 디저트 없으면
        dfs(nx, ny, d, tmp + [arr[nx][ny]])                         # 같은 방향으로 계속 가고, tmp에 값 더해주기

        if d != 3:                                                  # 위 if 문에서 막혀서 재귀를 빠져 나왔을 경우에
            dfs(nx, ny, d+1, tmp + [arr[nx][ny]])                   # d가 3이 아니라면 방향 바꿔서 다시 돌기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1


    for i in range(N):                                              # 좌표별로 실행
        for j in range(N):
            dfs(i, j, 0, [arr[i][j]])

    print(f'#{tc} {result}')
