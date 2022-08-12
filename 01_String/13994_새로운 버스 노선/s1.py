import sys
sys.stdin = open('13994.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    check = [0] * 1001
    result = 0
    for i in range(N):
        arr = list(map(int, input().split()))
        if arr[0] == 1:
            for j in range(arr[1], arr[2]+1):
                check[j] += 1
        if arr[0] == 2:
            for j in range(arr[1], arr[2]+1, 2):
                check[j] += 1
        if arr[0] == 3:
            for j in range(arr[1], arr[2]+1):
                if arr[1] % 2 == 0:
                    if j % 4 == 0:
                        check[j] += 1
                else:
                    if j % 3 == 0 and j % 10 != 0:
                        check[j] += 1
    result = 0
    for i in check:
        if result < i:
            result = i

    print(f'#{tc} {result}')






