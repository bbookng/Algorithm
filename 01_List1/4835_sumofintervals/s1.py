import sys
sys.stdin = open('4835.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    max_ = 0
    min_ = 99999999
    for i in range(n-m+1):              # m만큼 더하니까 n-m+1까지
        tmp = 0                         # 임시 값 생성
        for j in range(m):              # m 범위씩 더하기
            tmp += arr[i+j]

        if tmp > max_:
            max_ = tmp
        if tmp < min_:
            min_ = tmp


    print(f'#{tc} {max_ - min_}')