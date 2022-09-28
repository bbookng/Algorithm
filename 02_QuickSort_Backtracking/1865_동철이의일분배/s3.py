import sys
sys.stdin = open('input.txt')

def solution(i, visited):
    if visited == (1 << N) - 1:
        return 1

    if dp[visited]:
        return dp[visited]

    for j in range(N):
        if arr[i][j] and not visited & 1 << j:
            dp[visited] = max(dp[visited], arr[i][j] * solution(i + 1, visited | 1 << j))

    return dp[visited]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]

    dp = [0] * (1 << N)
    result = solution(0, 0) * 100
    print(dp)
    print(f'#{tc}', '{:.6f}'.format(result))