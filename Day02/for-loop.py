"""
Przyklad uzycia pętli loop
"""

for x in [1, 2, 3, 4, 5, 6, 7]:
    print(x, end=", ")

print("\n===============")
for x in ["PL", "DE", "UK", "US"]:
    if x=="UK":
        break
    print(x, end=", ")
print("\n===============")

for x in ["PL", "DE", "UK", "US"]:
    if x=="DE":
        continue
    print(x, end=", ")

print("\n======")
for x in [1, True, "Ala ma kota", -12.3456, None]:
    print(x, end=", ")

