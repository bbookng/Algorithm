import sys
sys.stdin = open('4881.txt')

def backtracking(N, idx, tmp):
    global total
    if tmp > total:                     # tmp가 total보다 커지면 의미 X
        return                          # 가지치기

    if idx == N:                        # 모든 행이 다 더해지면
        total = min(total, tmp)         # 작은값 찾기


    for i in range(N):                  # 열의 갯수만큼
        if visited[i] == 0:             # 방문 안한 열 체크
            print(board[idx][i], tmp)
            # tmp += board[idx][i]        # tmp에 추가
            visited[i] = 1              # 표시
            backtracking(N, idx+1, tmp+board[idx][i]) # 재귀. 다음 행으로 내려가서
            visited[i] = 0              # 다시 돌려주고
            # tmp -= board[idx][i]        # 0으로 만들어주기


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    total = 10000000
    backtracking(N, 0, 0)
    print(f'#{tc} {total}')
