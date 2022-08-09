import sys
sys.stdin = open('5789.txt')

T = int(input())
for tc in range(1, T+1):
    n, q = map(int, input().split())
    arr = [0] * n                       # 상자 생성
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):         # l부터 r idx 박스까지
            arr[j-1] = str(i)           # i로 바꿔준다.

    print(f'#{tc}', end=' ')
    print(*arr, sep=' ')
