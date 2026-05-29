import random

for i in range(3):
    print(random.randint(1, 10))

teammates = ['Alice', 'Bob', 'Charlie', 'David']
random_teammate = random.choice(teammates)
print(random_teammate)