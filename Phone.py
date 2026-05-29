number = input("Phone: ")
num_mapping ={
    "1":"One",
    "2":"Two",
    "3":"Three"
}

for ch in number:
    print(num_mapping.get(ch))