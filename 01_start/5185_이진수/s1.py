import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, num = input().split()
    result = ''
    for i in num:
        i = bin(int(i, 16))
        i = i[2:].zfill(4)
        result += i

    print(f'#{tc} {result}')