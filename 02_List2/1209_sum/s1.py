import sys
sys.stdin = open('1209.txt')

T = 10

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max = 0     # 최댓값

    for i in range(100):
        row = 0             # 각 행의 합
        col = 0             # 각 열의 합
        cross = 0           # 각 대각선 합
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
            if row > max:   # max보다 크면 갱신
                max = row
            if col > max:   # max보다 크면 갱신
                max = col
        for k in range(100):
            cross += arr[k][k]
            if cross > max: # max보다 크면 갱신
                max = cross

    print(f'#{tc} {max}')
