import sys
sys.stdin = open('4837.txt')

def sol(N, K):
    cnt = 0
    arr = list(range(1, 13))
    check = []
    for i in range(1 << 12):
        tmp = []                # 임시 부분집합
        for j in range(12):
            if i & (1 << j):    # 비트합으로
                tmp.append(arr[j])  # 부분집합 만들기
        if len(tmp) == N and sum(tmp) == K: # 원소갯수가N이고 합이 K면
            cnt += 1    # 카운팅
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    print(f'#{tc} {sol(N, K)}')

