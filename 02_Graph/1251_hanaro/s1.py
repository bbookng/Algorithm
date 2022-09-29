import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr_x = list(map(int, input().split()))
    arr_y = list(map(int, input().split()))
    E = float(input())

    adjM = [[0] * N for _ in range(N)]

    for i in range(N):
        a, b = arr_x[i], arr_y[i]
