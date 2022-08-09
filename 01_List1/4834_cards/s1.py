import sys
sys.stdin = open('4834.txt')

for tc in range(1, T+1):
    n = int(input())
    cards = list((map(int, input())))
    arr = [0]*10

    for j in cards:
        arr[j] += 1

    max_ = 0
    cnt = 0
    for k in range(10):
        if arr[k] == max_:
            cnt = k
        elif arr[k] > max_:
            max_ = arr[k]
            cnt = k


    print(f'#{tc} {cnt} {max_}')

