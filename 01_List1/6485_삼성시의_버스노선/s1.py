import sys
sys.stdin = open('6485.txt')

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    cnt = [0] * 5001                    # 버스 번호 범위
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
        for j in range(a, b+1):         # a~b 범위에 포함되는 수들을
            cnt[j] += 1                 # cnt의 index 에 +1
    p = int(input())
    stop = [int(input()) for i in range(p)]     # 버스정류장
    for k in stop:                      # k 정류장을 다니는 버스는
        print(cnt[k], end=' ')          # cnt에서 k번재 항목에 추가되어 있음
    print()



