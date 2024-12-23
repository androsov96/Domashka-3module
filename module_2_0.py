import random
random_2 = random.randint(3, 20)
password = []
for i in range(1, random_2):
    for j in range(1, random_2):
        if random_2 % (i + j) == 0 and i < j:
            password.append((i, j))

result ="".join(f'{i}{j}' for i, j in password)
print(f"{random_2} - {result}")



