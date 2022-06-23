n = input()

single = n[len(n)-2:]
shata = n[len(n)-3:]
shata2 = shata[:1]

hajar = n[len(n)-5:]
hajar2 = hajar[:2]

lakh = n[len(n)-7:]
lakh2 = lakh[:2]

koti = n[:len(n)-7]

print(f"{koti} kuti {lakh2} lakh {hajar2} hajar {shata2} shata {single}")
