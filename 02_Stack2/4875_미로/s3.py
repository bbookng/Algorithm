import sys
sys.stdin = open('4875.txt')

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j):
    global answer
    # 종료 조건
    if arr[i][j] == 2:
        answer = 1
        return

    # 이미 최적이 아닐때 탐색 중지
    # if ~~:
    #     return

    # 다음에 갈 후보군 결정
    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        # 후보군 중에 조건 만족 하는지 확인
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
            visited[ni][nj] = 1
            # 만족 했을 때, 다음 함수 호출
            dfs(ni, nj)




T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                si, sj = i, j
                break

    visited = [[0] * N for _ in range(N)]
    answer = 0

    dfs(si, sj)
    print(answer)