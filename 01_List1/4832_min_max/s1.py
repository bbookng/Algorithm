import sys
sys.stdin = open('4832.txt')

'''
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
'''

def sol(num, arr):
    max_ = 0
    min_ = 1000000
    for i in arr:           # arr 탐색
        if i > max_:        # i가 max_보다 크면 max 갱신
            max_ = i
        if i < min_:        # i가 min_보다 작으면 min 갱신
            min_ = i
    return max_ - min_

n = int(input())
for tc in range(1, n+1):
    num = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {sol(num, arr)}')
