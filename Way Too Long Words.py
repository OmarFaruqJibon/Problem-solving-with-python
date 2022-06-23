limit = int(input())
i = 0
while i < limit:
    x = input()
    if len(x) > 10:
        print(f"{x[:1]}{len(x) - 2}{x[len(x) - 1:]}")
    else:
        print(x)
    i += 1
