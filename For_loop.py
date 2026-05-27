for hehe in range(5,10,2):
    print(hehe)

prices=[10,20,30]
total=0
for index,item in enumerate(prices,1):
    print(f"Product no{index} : {item} taka")
    total+=item
print("Total: ",total,"taka")