import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs():
    q = deque()
    q.append(S)
    visited[S] = 1
    while q:
        tmp = q.popleft()
        for i in graph[tmp]:
            if visited[i] == 0:
                visited[i] = visited[tmp] + 1
                q.append(i)




T = 10
for tc in range(1, T+1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [set() for _ in range(101)]
    for i in range(0, N, 2):
        graph[arr[i]].add(arr[i+1])

    visited = [0] * 101
    bfs()
    result = 0
    for i in range(101):
        if visited[i] >= visited[result]:
            result = i

    print(f'#{tc} {result}')


