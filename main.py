import random

a = input("Podaj liczby:\n")
a=a.split(",")
min = a[0]
max = a[0]
for i in a[1::]:
    if i < min:
        min = i
    if i > max:
        max = i
print("max: " + max)
print("min: " + min)
miasta = {"Warsaw", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"}
random.shuffle(miasta)
print(miasta)
