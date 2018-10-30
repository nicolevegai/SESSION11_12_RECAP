print("This program asks for a number and tests if it is prime")
while True:
    try:
        read_line = input("Please give me an integer number")
        num = int(read_line)
    except ValueError:
        print("That was not a valid integer number")
        continue
    break
for i in range (2, num // 2):
    if num % i == 0:
        print("The number", num, "is not prime")
        exit()
print("The number", num, "is prime")

# generate 100 numbers, print only the prime ones
import random

rand = []
for i in range(0, 100):
    rand.append(random.randint(1, 10000))

for num in rand:
    prime = True
    for i in range(2, num // 2):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)