List=[0 for c in range (5)]
for c in range (5):
    List[c]=int(input("enter the data"))

for pointer in range (1,len(List)):
    itemtobeinserted=List[pointer]
    currentitem=pointer-1
    while List[currentitem]>itemtobeinserted and currentitem>=0:
        List[currentitem+1]=List[currentitem]
        currentitem=currentitem-1
    List[currentitem+1]=itemtobeinserted
        
for c in range (5):
    print(List[c])
