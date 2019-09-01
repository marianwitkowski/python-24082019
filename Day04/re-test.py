""""
Wyrażenia regularne
"""
import re

"""
 k....a - 5 znakow zaczyna od 'k' a konczy na 'a'
 Ma*k  - Zaczyna sie od 'Ma' , potem jest zero lub wiecej znakow i konczy na k
 Ma+k - - Zaczyna sie od 'Ma' , potem jest jeden lub wiecej znakow i konczy na k
 Ma?k - - Zaczyna sie od 'Ma' , potem jest zero lub jeden znak i konczy na k
 [^0-9] - znaki spoza zakresu od 0 do 9
"""
# wyszukiwanie wszystkich elementów wg wzorca
txt = "Mały Marek machał\tmakatką\ntrzymająć\ntrzy piwa"
print(txt)
wynik = re.findall("ma|trz", txt.lower())
print(wynik)

kod_pocztowy = "12-345"
wynik = re.match("^[0-9]{2}-[0-9]{3}$", kod_pocztowy.strip())
print(wynik)

#wynik = txt.replace(" ","*").replace("\t","*").replace("\n","*") # old-fashion style
wynik = re.sub("\s", "*", txt, 2)
print(wynik)

txt = "abcd efs jh 1SS23 fd  ZFSSS 3"
wynik = re.findall("\d", txt)
print("".join(wynik))

wynik = [znak for znak in txt if znak.isdigit()]
print("".join(wynik))

