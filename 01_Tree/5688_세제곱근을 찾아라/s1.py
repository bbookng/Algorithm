import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = -1
    tmp = N ** (1/3)
    if round(tmp) ** 3 == N:
        result = round(tmp)
    print(f'#{tc} {result}')