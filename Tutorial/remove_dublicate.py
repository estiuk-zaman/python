nums=[2,3,2,5,7,5,7,1]
uniq=[]
for i in nums:
    if i not in uniq:
        uniq.append(i)
uniq.sort()
print(uniq)