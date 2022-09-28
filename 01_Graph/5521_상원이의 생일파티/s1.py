import sys
sys.stdin = open('input.txt')

def bfs(N):
    q = [1]
    visited = [0] * (N+1)
    visited[1] = 1
    cnt = 0
    while q:
        t = q.pop(0)
        cnt += 1
        if visited[t] < 3:
            for i in graph[t]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = visited[t] + 1
    return cnt-1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = bfs(N)
    print(f'#{tc} {ans}')

