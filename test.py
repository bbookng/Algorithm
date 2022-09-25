a = [1, 3, 5]

N = 2 ** len(a)
result = []
for i in range(N):
    tmp = []
    for j in range(len(a)):
        if i & 1 << j:
            tmp.append(a[j])

    result.append(tmp)

print(result)

