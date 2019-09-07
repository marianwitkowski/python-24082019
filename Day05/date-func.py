"""
Kilka funkcji w związku z czasem/datą
"""
import datetime
import time

today = datetime.datetime.today() #dzisiaj
print("Dzisiaj=",today)

curr_time = datetime.datetime.now().time()
print("Czas=",curr_time)

day_of_week = ["Pon", "Wto", "Sro", "Czw", "Pią", "Sob", "Nie"]
week_day =datetime.date.weekday(today) # 0 -poniedziałek
print("Dzien tygodnia=",week_day,day_of_week[week_day])

# formatowanie daty
# https://www.programiz.com/python-programming/datetime/strftime
birthday = datetime.datetime(1976, 8, 15, 6, 0, 0)
print(birthday.strftime("%Y-%m-%d"))

diff = today - birthday
print("dni",diff.days,"sekund",diff.seconds)

now =  datetime.datetime.now().time()
print(now.strftime("%H:%M:%S"))

print("do petli")
t1 = time.time_ns()
for _ in range(0, int(10E3)):
    x = 1
t2 = time.time_ns()
print("roznica=",(t2-t1))

