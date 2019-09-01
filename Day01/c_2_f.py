
"""
	Konwersja temperatury C do F
	
	T(°F) = T(°C) × 9/5 + 32

"""

temp_c = input("Podaj temp. w C: ")
temp_c = float(temp_c)
temp_f = temp_c * 9/5 + 32
print("Temp. w F = ",temp_f)

"""
 i na nowo do C
 T(°C) = (T(°F) - 32) × 5/9

"""
temp_c = (temp_f - 32) * 5/9
print("Temp. w C = ",temp_c)

