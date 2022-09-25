import sys
sys.stdin = open('input.txt')

def inorder(now):
    global num
    if now*2 <= N:
        inorder(now*2)
    tree[now] = num
    num += 1
    if now*2+1 <= N:
        inorder(now*2+1)





T = int(input())
for _ in range(T):

    num = 1
    N = int(input())
    tree = [0] * (N + 1)

    inorder(1)
    print(tree)

    print(tree[1], tree[N//2])