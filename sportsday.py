list = []
listLen = 7 

for i in range(listLen):
    print("scores:")
    list.append(input())
    
print(list)
list.sort()
print (" the sorted list is", list)
print(" Runnerup score is ", list[-2])

