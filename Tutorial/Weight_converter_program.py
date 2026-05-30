weight = int(input("Give me your Weight: "))
unit = input("Its L or K")
if unit=="l":
    print(f"Your weight is {weight*0.45}")
else:
    print(f"Your wight is {weight/0.45}")
