a = int(input())
y = 0
for x in range (a):
    z = input()
    if z.count('1') > 1:
        y = y+1
print(y)
