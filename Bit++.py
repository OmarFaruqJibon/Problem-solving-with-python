n = int(input())
c = 0
for i in range(n):
    bit = input()
    if bit.lower() == "x++" or bit.lower() == "++x":
        c +=1
    if bit.lower() == "x--" or bit.lower() == "--x":
        c -=1

print(c)
