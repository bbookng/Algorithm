import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())

    cnt = 0
    result = ''
    while N > 0:
        tmp = N*2
        result += str(tmp)[0]
        N = tmp - int(tmp)
        cnt += 1

    if cnt > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')