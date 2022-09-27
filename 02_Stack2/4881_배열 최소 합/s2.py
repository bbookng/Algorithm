import sys
sys.stdin = open('4881.txt')

def solution(i, total):
    global _min
    # 이미 최적이 아닐때 탐색 중지
    if total >= _min:
        return

    # 종료 조건
    if i == N:
        _min = total

    # 다음에 갈 후보군 결정
    for nxt in range(N):
        # 후보군 중에 조건 만족 하는지 확인
        if candidates[nxt]:
            # 만족 했을 때, 다음 함수 호출
            candidates[nxt] = 0
            solution(i+1, total+arr[i][nxt])
            candidates[nxt] = 1

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    _min = float('inf')
    candidates = [1] * N

    solution(0, 0)
    print(_min)