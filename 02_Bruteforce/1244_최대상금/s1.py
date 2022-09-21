import sys
sys.stdin = open('input.txt')

def solution(idx, cnt):
    global result

    if cnt == N:
        if flag and numbers.count(max(numbers, key=lambda x: numbers.count(x))) == 1:
            numbers[-2], numbers[-1] = numbers[-1], numbers[-2]
        result = max(int(''.join(numbers)), result)
        return
    for i in range(idx, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                solution(idx, cnt + 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]

    if result == 0 and cnt < N:
        if not flag and numbers.count(max(numbers, key=lambda x: numbers.count(x))) == 1:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        solution(idx, cnt+1)

T = int(input())

for tc in range(1, T+1):
    numbers, N = input().split()
    N = int(N)
    numbers = list(numbers)
    flag = 0

    if N > len(numbers):
        flag = (N-len(numbers))%2
        N = len(numbers)
    result = 0

    solution(0, 0)
    print(f'#{tc} {result}')

