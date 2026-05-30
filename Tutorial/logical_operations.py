hasHighIncome=False
isGoodCredit=False
if hasHighIncome and isGoodCredit:
    print("Its and")
elif hasHighIncome or isGoodCredit:
    print("Its or")
elif hasHighIncome and not isGoodCredit:
    print("and .. not")
else:
    print("Hehe")