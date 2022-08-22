import sys
sys.stdin = open('1223.txt')

def sol(counts):
    stack = []
    result = []
    for i in counts:
        if i == '+':
            while stack:
                result.append(stack.pop())
            stack.append(i)
        elif i == '*':
            while stack and stack[-1] == '*':
                result.append((stack.pop()))
            stack.append(i)
        else:
            result.append(i)
    while stack:
        result.append(stack.pop())

    stack = []
    for i in result:
        if i not in '+*' and i.isdigit():
            stack.append(int(i))
        else:
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            if i == '+':
                stack.append(tmp2+tmp1)
            elif i == '*':
                stack.append(tmp2*tmp1)
    return stack.pop()


T = 10
for tc in range(1, T+1):
    n = int(input())
    counts = input()
    print(f'#{tc} {sol(counts)}')