import sys
sys.stdin = open('1234.txt')

def sol(numbers):
    check = []
    for i in numbers:
        if check and i == check[-1]:
            check.pop()
        else:
            check.append(i)
    return ''.join(check)

T = 10
for tc in range(1, T+1):
    L, numbers = map(str, input().split())
    print(f'#{tc} {sol(numbers)}')