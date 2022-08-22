import sys
sys.stdin = open('1220.txt')

def sol(table):
    cnt = 0
    for i in range(N):
        stack = []
        for j in range(N):
            if not stack and table[j][i] == 1:
                stack.append(1)
            else:
                if stack and table[j][i] == 2 and stack[-1] == 1:
                    stack.pop()
                    cnt += 1


    return cnt

T = 10
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {sol(table)}')