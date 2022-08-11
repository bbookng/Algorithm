import sys
sys.stdin = open('4836.txt')

T = int(input())
for tc in range(1, T+1):
    board = list([0] * 10 for _ in range(10))       # 빈 도화지
    n = int(input())
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(arr[0], arr[2]+1):           # 가로 범위
            for k in range(arr[1], arr[3]+1):       # 세로 범위
                board[j][k] += arr[4]               # 색칠하기
    result = 0
    for s in board:
        result += s.count(3)                        # 보라색 찾기


    print(f'#{tc} {result}')

