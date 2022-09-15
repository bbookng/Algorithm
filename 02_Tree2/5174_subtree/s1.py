import sys
sys.stdin = open('input.txt')

def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    par = [0] * (E + 2)
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p

    preorder(N)

    print(f'#{tc} {cnt}')
