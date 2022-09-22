import sys
sys.stdin = open('input.txt')

def solution(S, i, tmp):
    global result

    if result < tmp:                                    # 가지치기
        return

    if S == N:                                          # N 만큼 더해지면
        tmp += arr[i][0]                                # 마지막 사무실 더하고
        result = min(tmp, result)                       # 최솟값 갱신
        return

    else:
        for j in range(1, N):                           # 1열 빼고
            if arr[i][j] != 0 and not visited[j]:       # 0이 아니고 방문한 곳이 아니면
                visited[j] = 1                          # 방문 표시
                solution(S+1, j, tmp + arr[i][j])       # 횟수 카운트, 연결된 좌표로, 배터리 더하기
                visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 999999
    visited = [0] * N

    solution(1, 0, 0)

    print(f'#{tc} {result}')

