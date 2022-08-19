import sys
sys.stdin = open('1220.txt')

def sol(table):
    cnt = 0

    for i in table:
        while 0 in i:
            i.remove(0)
            tmp = 0
        for j in range(len(i)):
            if tmp == 0 and i[j] == 1:
                tmp = 1
            elif tmp == 1 and i[j] == 2:
                tmp = 0
                cnt += 1

    return cnt

T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    table = list(map(list, list(zip(*table))))
    print(f'#{tc} {sol(table)}')