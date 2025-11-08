import random
numbers = [random.randint(1, 30) for _ in range(7)]
print("Generated numbers:", numbers)
count = 0
for num in numbers:
    if num <= 10:
        continue  
    print(num)
    count += 1
print("Total numbers greater than 10:", count)
