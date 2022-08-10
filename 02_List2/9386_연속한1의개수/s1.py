T = int(input())

def sol(n, arr):
    cnt = 0
    max_ = 0
    for i in range(n):
        if int(arr[i]) == 1:
            cnt += 1
            if max_ < cnt:
                max_ = cnt
        else:
            cnt = 0
    return max_


for tc in range(1, T+1):
    n = int(input())
    arr = list(input())
    print(f'#{tc} {sol(n, arr)}')
