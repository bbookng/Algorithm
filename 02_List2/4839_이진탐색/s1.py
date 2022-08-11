import sys
sys.stdin = open('4839.txt')

def sol(start, end, target):
    count = 0
    while True:
        count += 1
        mid = (start + end) // 2    # 중간값부터 탐색
        if mid == target:           # 찾았다
            return count            # 횟수 반환
        elif mid < target:          # 중간값이 target보다 크면
            start = mid             # start지점을 중간값부터
        else:                       # target이 중간값보다 작으면
            end = mid               # end지점을 중간값으로

def findWinner(A, B):
    if A < B:
        return 'A'
    elif A == B:
        return 0
    else:
        return 'B'

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    A = sol(1, P, A)
    B = sol(1, P, B)

    print(f'#{tc} {findWinner(A, B)}')