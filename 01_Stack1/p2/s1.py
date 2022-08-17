import sys
sys.stdin = open('p2.txt')

def sol(data):
    tmp = []
    for i in data:
        if i == '(':
            tmp.append(i)
        else:
            if not tmp:
                return -1
            else:
                check = tmp.pop()
                if check != '(':
                    return -1
    if not tmp:
        return 1
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    data = list(input())
    print(f'#{tc} {sol(data)}')

