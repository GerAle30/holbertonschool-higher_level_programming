#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# obtener el ultimo digito
last_digit = abs(number) % 10
# si el numero es negativo, el ultimo digito ddebe ser negativo
if number < 0:
    last_digit = -last_digit

    # Construir el mensaje
print(f"Last digit of {number} is {last_digit}", end=" ")

if last_digit > 5:
    print("and is greate than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
