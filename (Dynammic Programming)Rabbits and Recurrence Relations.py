n = 31
k = 5
parent, child = 1, 1
for i in range(n-1):
    child, parent = parent, parent + (child*k)

print(child)