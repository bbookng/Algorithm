import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (100001)

    last = 0
    for i in arr:
        last += 1
        heap[last] = i
        c = last
        p = c // 2
        while p and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c // 2


    result = 0
    while N:
        result += heap[N//2]
        N //= 2

    print(f'#{tc} {result}')
