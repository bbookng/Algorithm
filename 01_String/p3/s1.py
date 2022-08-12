def BruteForce(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M
    else: return -1

def BoierMoor(p, t):
    for i in range(len(p) - len(t) + 1):
        for j in range(len(t)):
            if p[i+j] != t[j]:
                break
        else:
            return i
    return -1

def KMP(p, t):
    for i in range(len(p) - len(t)):
