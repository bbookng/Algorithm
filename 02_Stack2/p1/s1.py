T = int(input())
for tc in range(1, T+1):
    N = input()
    stack = []
    print(f'#{tc}', end=' ')
    for i in N:
        if i.isdigit():
            print(i, end='')
        else:
            stack.append(i)
    while stack:
        print(stack.pop(), end='')
    print()
