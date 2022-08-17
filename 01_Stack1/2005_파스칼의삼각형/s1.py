def solution(i, arr):
    if i > N:
        return
    if i == 1:
        print("1")
        solution(i+1, [1])
    else:
        result = [0] * (i - 2)
        for k in range(0, len(arr)-1):
            result[k] = arr[k] + arr[k+1]
        result = [1] + result + [1]
        print(*result)
        solution(i+1, result)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    solution(1, [])



