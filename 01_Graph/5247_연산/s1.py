import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs():
    visited = set()
    q = deque([])
    q.append((N, 0))
    while q:
        x, cnt = q.popleft()
        if x == M:
            return cnt
        if x + 1 not in visited and 0 < x + 1 <= 1000000:
            q.append((x+1, cnt+1))
            visited.add(x+1)
        if x - 1 not in visited and 0 < x - 1 <= 1000000:
            q.append((x - 1, cnt + 1))
            visited.add(x-1)
        if x * 2 not in visited and 0 < x * 2 <= 1000000:
            q.append((x*2, cnt+1))
            visited.add(x*2)
        if x - 10 not in visited and 0 < x - 10 <= 1000000:
            q.append((x-10, cnt+1))
            visited.add(x-10)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs()}')
