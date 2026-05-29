number = input("Phone: ")
num_mapping ={
    "1":"One",
    "2":"Two",
    "3":"Three"
}
output=""
for ch in number:
    output+=(num_mapping.get(ch)+" ")
print(output)