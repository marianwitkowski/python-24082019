import re

def int_to_roman(input):
    if not str(input).isdigit():
        raise Exception("To nie jest liczba arabska")
    input = int(input)
    if not 0 < input < 4000:
        raise Exception("Liczba musi być z zakresu od 1 do 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)


def roman_to_int(input):
    input = str(input).strip().upper()
    if not re.match("^[MDCLXVI]{1,}$", input):
        raise Exception("To nie jest poprawna liczba rzymska")
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input)):
        value = nums[input[i]]
        if i+1 < len(input) and nums[input[i+1]] > value:
            sum -= value
        else: sum += value
    return sum


while True:
    s = input("Podaj liczbę arabską: ").strip()
    if s=="q":
        break
    try:
        roman = int_to_roman(s)
        print(f"{s} to {roman}")
    except Exception as e:
        print("Wyjątek: ",e)
        continue

    try:
        arab = roman_to_int(roman)
        print(f"{roman} to {arab}")
    except Exception as e:
        print("Wyjątek: ",e)
        continue

    print("-"*30)
