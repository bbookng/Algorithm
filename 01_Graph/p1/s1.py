import sys
sys.stdin = open('input.txt')

def dfs(i):
    visited[i] = 1
    print(i, end=' ')
    for j in graph[i]:
        if j and visited[j] == 0:
            dfs(j)



arr = list(map(int, input().split()))
graph = [[] for _ in range(len(arr)//2 + 1)]

for i in range(0, len(arr), 2):
    graph[arr[i]].append(arr[i+1])
    graph[arr[i+1]].append(arr[i])

visited = [0] * (len(arr) // 2 + 1)

dfs(1)
