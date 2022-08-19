import sys
sys.stdin = open('1952.txt')

T = int(input())
for tc in range(1, T+1):
    D, M, Q, Y = map(int, input().split())
    schedule = list(map(int, input().split()))

    dp = [0] * 13
    dp[1] = min(D * schedule[1], M)
    dp[2] = dp[1] + min(D * schedule[2], M)
    for month in range(3, 13):
        dp[month] = min(dp[month - 1] + D * schedule[month], dp[month - 1] + M, dp[month - 3] + Q)

    print(f'#{tc} {min(dp[12], Y}')