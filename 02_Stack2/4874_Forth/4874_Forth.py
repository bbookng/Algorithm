import sys
sys.stdin = open('4874.txt')

def sol(arr):
    stack = []
    for i in arr:
        if i == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        if i not in '+-*/' and i.isdigit():
            stack.append(int(i))
        else:
            if len(stack) < 2:
                return 'error'
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            if i == '+':
                stack.append(tmp2+tmp1)
            elif i == '-':
                stack.append(tmp2-tmp1)
            elif i == '*':
                stack.append(tmp2*tmp1)
            elif i == '/':
                stack.append(tmp2//tmp1)


T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    print(f'#{tc} {sol(arr)}')