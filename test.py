<<<<<<< HEAD
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()) for _ in range(N))
=======
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
>>>>>>> 66efae3ddc2ccf56cab591428db810fa27ffe9eb

