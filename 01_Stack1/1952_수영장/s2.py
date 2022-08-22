import sys
sys.stdin = open('1952.txt')

T = int(input())
for tc in range(1, T+1):
    D, M, Q, Y = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    dp = [0] * 13
    dp[1] = min(arr[1] * D, M)
    dp[2] = arr[1] + min(arr[2]*D, M)
    for i in range(3, 13):
        dp[i] = min(dp[i-1] + arr[i] * D, dp[i-1] + M, dp[i-3] + Q)

    print(f'#{tc} {min(dp[12], Y)}')
