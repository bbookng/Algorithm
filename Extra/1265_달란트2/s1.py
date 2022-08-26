import sys
sys.stdin = open('1265.txt')

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    tmp1, tmp2 = N // P, N % P
    result = (tmp1 ** (P-tmp2)) * ((tmp1 + 1) ** tmp2)
    print(f'#{tc} {result}')