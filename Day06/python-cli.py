import sys

if len(sys.argv)<3:
    raise IndexError("Za mało danych")
print(f"Cześć {sys.argv[1]} {sys.argv[2]}")
#print(sys.argv)

