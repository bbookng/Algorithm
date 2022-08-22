def itoa(N):
    flag = 0
    if N < 0:
        flag = 1
        N *= -1
    result = ""
    while N:
        result = chr((N % 10) + 48) + result
        N //= 10
    if flag:
        result = '-' + result
    print(result, type(result))
    return

T = 6
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}', end=' ')
    itoa(N)