
with open("plik.txt", "rt") as fh:
    for index, line in enumerate(fh, 1):
        if 3 <= index <=5:
            print(line, end='')

"""
with open("plik.txt") as fh:
    all_content = fh.read(-1)
    print(all_content)
"""