a = [1, 2, 1, 3, 4, 5]
print(a.count(max(a, key=lambda x: a.count(x))))