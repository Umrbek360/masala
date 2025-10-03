# Pythonda arifmetik operatorlar mavzusidan algoritmik masalalar
#1. Ikki sonni yig‘indisi
a = int(input("son kiriting: "))
b = int(input("son kiriting: "))
sum = a + b
print(f"Yig'indi: , {sum} , ga teng")

#2. To‘rtburchakning yuzasi
l = int(input("son kiriting: "))
w = int(input("son kiriting: "))
area = l * w
print(f"To'rt burchakni yuzi: , {area} , ga teng")

#3. Uch sonning o‘rtacha arifmetigi
x = int(input("son kiriting: "))
y = int(input("son kiriting: "))
z = int(input("son kiriting: "))
avg = (x+y+z) / 3
print(f"o'rta arifmetiki: , {avg} , ga teng")

#4. To‘g‘ri to‘rtburchak perimetri
a = int(input("son kiriting: "))
b = int(input("son kiriting: "))
p = 2 * (a + b)
print(f" To‘rtburchakning perimetri: , {p} , ga teng")

#5. Soatni daqiqaga aylantirish
h = int(input("soat kiriting: "))
m = int(input("daqiqa kiriting: "))
total_min = h * 60 + m
print(f"Umumiy daqiqalar: , {total_min} , ga teng")

#6. Pul birligini konvertatsiya
usd = int(input("pulni kiriting: "))
sum = usd * 12000
print(f"dolr: , {sum} , ga teng")

#7. Ikki son farqi (modul)
a = int(input("sonni kiriting: "))
b = int(input("sonni kiriting: "))
diff = abs(a - b)
print(f"soni modli:,  {diff}, ga teng")

#8. Darajaga ko‘tarish
x = int(input("sonni kiriting: "))
n = int(input("sonni kiriting: "))
power = x ** n
print(f"soni darajasi: , {power} , ga teng")

#9. Bo‘linma va qoldiq
a = int(input("sonni kiriting: "))
b = int(input("sonni kiriting: "))
quotient = a // b
print(f"soni qoldig'i: , {quotient} , ga teng")

#10. Sonlarni almashtirish (temp ishlatmasdan)
a = int(input("sonni kiriting: "))
b = int(input("sonni kiriting: "))
a , b = b , a
print(f"Almashgan son: , {a, b} , ga teng")

#II. Hayotiy muammolar
#1. Oylik ijara to‘lovi bo‘lib-bo‘lib to‘lash
total_rent = int(input("son kiriting: "))
per_month = total_rent / n
print(f"ijara haqi , {per_month} , ga teng: ")

#2. Yo‘l bosib o‘tish vaqti
d = int(input("masofa kiriting (km)da: "))
v = int(input("tezlik  kiriting (km/soat)da: "))
time = d / v
print(f":{time}")

#3. Yo‘lovchilarga chiptani taqsimlash
seats = int(input("o'rindiqlar sonni  kiriting: "))
passengers = int(input("yo'lovchilar sonini kiriting: "))
per_person = passengers // seats
left = passengers % seats
print(f"Har biriga: {passengers // seats} ta chipta, Qolgan: {passengers % seats}")

#4. Yoqilg‘i sarfi
consumption = float(input("100 km uchun sarf kiriting: "))
d = int(input("100 km uchun masofa kiriting: "))
fuel = consumption * d / 100.
print(f"Sarf qilingan yoqilg‘i: {fuel} litr")

#5. Oylik ish haqi (soliqdan keyin)
salary = float(input("Brutto maosh: "))
net = salary * (1 - 0.12)
print(f"Netto maosh: , {net} , ga teng")

# 6. Kechikkan to‘lov jarimasi
amount = float(input("Summani kiriting: "))
days = int(input("kechikish kunlarini kiriting: "))
penalty = amount * 0.001 * days
print(f"Jami to‘lov: , {penalty} , ga teng")

# 7. Chegirma
price = int(input("Narx kiriting: "))
discount = int(input("chegirma (%) kiriting: "))
paid = price * (1 - discount / 100)
print(f"To‘lanadigan summa: , {paid} , ga teng")

# 8. Oddiy foiz hisoblash
p = int(input("Asos kiriting: "))
r = int(input("foiz stavkasi kiriting: "))
t = int(input("yillar kiriting: "))
interest = p * r / 100 * t
total = p + interest
print(f"Foiz: {interest}, Jami summa: {total}")

## 9. Ovqat retsepti miqdorini oshirish
base_qty = int(input("Asosiy miqdor (gramm) kiriting: "))
people = int(input("odamlar soni kiriting: "))
per_person = base_qty / 4
needed = per_person * people
print(f"asosi miqdor , {per_person} , needed , {needed} , ga teng")
# 10. Tip qo‘shish

bill = float(input("Hisob-kitob summasi: "))
tip = bill * 0.10
total = bill + tip
print(f"Tip: {tip}, Jami to‘lov: {total}")
