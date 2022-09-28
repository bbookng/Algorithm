import sys
sys.stdin = open('input.txt')

def solution(i, visited):
    # 모두 끝난 상태에서 모든 일이 끝날 때까지 확률은 100%이므로 1을 리턴
    if visited == (1 << N) - 1:
        return 1

    # 만약 이미 계산된 값이 요청되었다면 바로 리턴
    if dp[visited]:
        return dp[visited]

    # 만약 이미 계산된 값이 없다면 해당 상태의 최대 확률값을 계산
    for j in range(N):
        # candidates 결정
        # arr[i][j]가 0이 아니고 j번째 일이 아직 수행 되지 않았을 때 가능
        if arr[i][j] and not visited & 1 << j:
            # arr[i][j] * solution(i + 1, visited|1 << j) = 현재 visited와 j번째 일이 되었을 때의 최대 확률 * i번째 employee한테 j번째 일을 시킬 때의 확률
            # for문을 돌며 max를 해서 최대값으로 계속해서 갱신한다.
            dp[visited] = max(dp[visited], arr[i][j] * solution(i + 1, visited|1 << j))

    # 갱신이 완료 되었을 때, 해당 상태의 최대 확률값을 리턴한다.
    return dp[visited]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]

    # dp의 index가 의미하는 것은 지금까지 수행한 일들을 비트로 나타낸 것
    # index 10이면 1번 3번이 수행된 상태
    # 예를 들어서 001010이라면 [False, True, False, True, False, False]
    # dp는 해당 상태(어느 어느 일들이 수행되어 있는 상태)에서 모든 일이 수행되기까지의 최대 확률을 저장할 테이블
    # 001010 -> 111111이 되기 위한 최대 확률
    # 001011 * 2번 employee한테 0번 일을 시킬 확률
    # 001110 * 2번 employee한테 2번 일을 시킬 확률
    # 011010 * 2번 employee한테 4번 일을 시킬 확률
    # 101010 * 2번 employee한테 5번 일을 시킬 확률
    # 이렇게 네가지 경우의 수 중 최대 값을 001010에 저장
    dp = [0] * (1 << N)
    result = solution(0, 0) * 100
    print(f'#{tc}', '{:.6f}'.format(result))