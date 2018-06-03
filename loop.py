myList = [4,0,3,-13,36,300,-200]
print ("before sort:")
print(myList)

lenList = len(myList)
for i in range(0,lenList-1):
    for j in range(i+1,lenList):
        if myList[i] > myList[j]:
            myList[i],myList[j] = myList[j],myList[i]
print("after soft:")
print(myList)
