import sys
sys.stdin = open('input.txt')

def inorder(num):
    if num <= N:                            # N 이하일 때 까지
        inorder(num * 2)                    # 왼쪽 자식
        print(node[num], end='')
        inorder(num * 2 + 1)                # 오른쪽 자식

T = 10
for tc in range(1, T+1):
    N = int(input())
    node = [0] * (N+1)
    for i in range(N):
        tmp = list(input().split())
        node[i+1] = tmp[1]                   # 완전 이진트리 형식. 순서대로 주어짐.
    print(f'#{tc}', end=' ')
    inorder(1)
    print()