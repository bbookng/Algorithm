import sys
sys.stdin = open('4866.txt')

def sol(N):
    check = []
    for i in N:
        if i in '{(':
            check.append(i)
        elif i in '})':
            if check and check[-1] == '{' and i == '}':
                check.pop()
            elif check and check[-1] == '(' and i == ')':
                check.pop()
            else:
                return 0
    else:
        if check:
            return 0
        else:
            return 1

T = int(input())
for tc in range(1, T+1):
    N = input()
    print(f'#{tc} {sol(N)}')