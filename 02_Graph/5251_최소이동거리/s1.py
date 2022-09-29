import sys, heapq
sys.stdin = open('input.txt')

def solution():
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        length, node = heapq.heappop(q)
        for x, y in graph[node]:
            tmp = length + y
            if visited[x] > tmp:
                visited[x] = tmp
                heapq.heappush(q, (tmp, x))

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    visited = [float('inf')] * (N+1)

    solution()
    print(f'#{tc} {visited[N]}')

