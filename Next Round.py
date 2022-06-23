n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for x in a:
    if x > 0 and x >= a[k-1]:
        c += 1
print(c)
