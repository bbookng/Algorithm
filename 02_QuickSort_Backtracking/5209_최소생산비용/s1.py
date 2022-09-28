import sys
sys.stdin = open('input.txt')

def solution(i, total):
    global result
    if total > result:
        return

    if i == N:
        result = total
        return

    for idx in range(N):
        if not visited[idx]:
            visited[idx] = 1
            solution(i + 1, total + arr[i][idx])
            visited[idx] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    visited = [0] * N
    solution(0, 0)

    print(f'#{tc} {result}')