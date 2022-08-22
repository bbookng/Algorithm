def f(i, N):
    global answer
    global cnt
    cnt += 1
    if i == N:
        if s == t:
            answer += 1
        return
    else:
        f(i+1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
cnt = 0
f(0, 10)
print(answer)