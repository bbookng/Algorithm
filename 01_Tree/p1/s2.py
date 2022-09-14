V = int(input())                            # 정점 개수, 마지막 정점 번호
arr = list(map(int, input().split()))
E = V - 1

ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

par = [0] * (V + 1)

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p


def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:
            return i


def preorder(n):
    if n:
        print(n, end = ' ')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)

def f(n):                       # global cnt 없이 순회한 정점 수를 리턴하는 함수
    if n == 0:  # 서브트리가 비어있으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1



root = find_root(V)

preorder(root)
print(f(root))