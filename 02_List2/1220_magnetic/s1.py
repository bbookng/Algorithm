import sys
sys.stdin = open('1220.txt')

def sol(table):
    cnt = 0
    for i in range(100):
        check = []
        for j in range(100):
            if not check and table[j][i] == 1:
                check.append(1)
            elif check and table[j][i] == 2 and check[-1] == 1:
                check.pop()
                cnt += 1
    return cnt



T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {sol(table)}')