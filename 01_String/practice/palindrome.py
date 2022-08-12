n = input()


if n == n[::-1]:
    print('true')
else:
    print('false')


def sol2(n):
    n = list(n)
    tmp = list(n)
    for i in range(len(n)//2):
        tmp[i], tmp[-1-i] = tmp[-1-i], tmp[i]
    if n == tmp:
        return True
    else:
        return False

print(sol1(n))
print(sol2(n))