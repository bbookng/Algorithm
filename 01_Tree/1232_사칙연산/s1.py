import sys
sys.stdin = open('input.txt')

def solution(idx):
    if value[idx].isnumeric():
        return int(value[idx])

    else:
        if value[idx] == '+':
            return solution(child[idx][0]) + solution(child[idx][1])
        elif value[idx] == '-':
            return solution(child[idx][0]) - solution(child[idx][1])
        elif value[idx] == '*':
            return solution(child[idx][0]) * solution(child[idx][1])
        elif value[idx] == '/':
            return solution(child[idx][0]) / solution(child[idx][1])


T = 10
for tc in range(1, T+1):
    N = int(input())
    value = [0] * (N+1)
    child = [(0, 0) for _ in range(N+1)]

    for _ in range(N):
        index, *arr = input().split()
        value[int(index)] = arr[0]
        if not arr[0].isnumeric():
            child[int(index)] = (int(arr[1]), int(arr[2]))

    print(f'#{tc} {int(solution(1))}')


