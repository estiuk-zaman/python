name = ["istii","Estik","Oishik"]
print(name[-2])

name = ["istii","Estik","Oishik"]
print(name[0])

name = ["istii","Estik","Oishik","Subaita","Zuairia","Nafeez","Wahid"]
print(name[1:4])

name[0]="Istii"
print(name)

numbers=[5,8,7,4,1,3,6,7,12,55]
max=numbers[0]
for item in numbers:
    if item > max:
        max=item
print("Max:",max)