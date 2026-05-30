customer={
    "Name":"istii",
    "Age":30,
    "isVarified": True
}

print(customer["Name"])
print(customer["isVarified"])
customer["Name"]="Oishik"
customer["BirthDay"]="2003"
print(customer["BirthDay"])
print(customer.get("Name"))