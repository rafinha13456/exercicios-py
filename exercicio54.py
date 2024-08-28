n = 1
cont1 = cont2 = cont3 = cont4 = 0
while n >= 0:
    n = int(input())
    if n >= 0 and n <= 25:
        cont1 += 1
    elif n >= 26 and n <= 50:
        cont2 += 1
    elif n >= 51 and n <= 75:
        cont3 += 1
    elif n >= 76 and n <= 100:
        cont4 += 1

print(f"Intervalo [0-25]: {cont1}")
print(f"Intervalo [26-50]: {cont2}")
print(f"Intervalo [51-75]: {cont3}")
print(f"Intervalo [76-100]: {cont4}")