myList = [4,0,3,-13,5,8,31,36,-100]
print ("before sort:")
print(myList)

lenList = len(myList)
for i in range(0,lenList-1):
    for j in range(i+1,lenList-1):
        if myList[i] > myList[j]:
            myList[i],myList[j] = myList[j],myList[i]
print("after soft:")
print(myList)
