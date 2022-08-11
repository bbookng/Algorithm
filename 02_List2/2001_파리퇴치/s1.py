import sys
sys.stdin = open('2001.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for c in range(n)]
    max_ = 0
    for i in range(n-m+1):
            for j in range(n-m+1):
                sum = 0
                for k in range(m):
                    for l in range(m):
                        sum += arr[i+k][j+l]
                if sum > max_:
                    max_ = sum
    print(f'#{tc} {max_}')

