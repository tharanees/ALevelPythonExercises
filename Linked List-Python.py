def add(newitem,free,start,listA):
    if free==None:
        print("list full")
    else:
        listA[free].data=newitem
        temp=free
        free=listA[free].pointer
        ThisNodePointer=start
        while ThisNodePointer!=None and listA[ThisNodePointer].data<newitem:
            previous=ThisNodePointer
            ThisNodePointer=listA[ThisNodePointer].pointer
        if ThisNodePointer==start:
            listA[temp].pointer=start
            start=temp
        else:
            listA[temp].pointer=listA[previous].pointer
            listA[previous].pointer=temp
    return (free,start,listA)

def delete (dataitem,free,start,listA):
    ThisNodePointer=start
    while ThisNodePointer!=None and listA[ThisNodePointer].data!=dataitem:
        previous=ThisNodePointer
        ThisNodePointer=listA[ThisNodePointer].pointer
    if ThisNodePointer != None:
        if ThisNodePointer==start:
            start=listA[ThisNodePointer].pointer
        else:
            listA[previous].pointer=listA[ThisNodePointer].pointer
        listA[ThisNodePointer].pointer=free
        free=ThisNodePointer
    else:
        print("such node doesn't exist in list")
    return (free,start,listA)


def findnode(dataitem,start,listA):
    ThisNodePointer=start
    while ThisNodePointer!=None and listA[ThisNodePointer].data!=dataitem:
        ThisNodePointer=listA[ThisNodePointer].pointer
    return ThisNodePointer

def findnode_alt(dataitem,start,listA):
    ThisNodePointer=start
    Found=False
    while ThisNodePointer!=None and Found==False:
        if listA[ThisNodePointer].data==dataitem:
            Found=True
        else:
            ThisNodePointer=listA[ThisNodePointer].pointer
    return ThisNodePointer


def outputallnodes(start,listA):
    ThisNodePointer=start
    while ThisNodePointer!=None:
        print(listA[ThisNodePointer].data," ",listA[ThisNodePointer].pointer)
        ThisNodePointer=listA[ThisNodePointer].pointer


class node:
    def __init__(self,val):
        self.data=""
        self.pointer=val
listA=[]
for count in range (4):
    listA.append(node(count+1))
listA.append(node(None))
start=None
free=0
print("1. ADD NEW NODE")
print("2. DELETE A NODE")
print("3. FIND A NODE")
print("4. OUTPUT ALL NODES")
print("5. EXIT")
while True:
    option=input("ENTER THE OPTION")
    if option=="1":
        newitem=input("enter new item to be added")
        free,start,listA=add(newitem,free,start,listA)
    else:
        if option=="2":
            dataitem=input("enter the node to be deleted")
            free,start,listA=delete(dataitem,free,start,listA)
        else:
            if option=="3":
                dataitem=input("enter the data item to be searched")
                pointer=findnode_alt(dataitem,start,listA)
                print("The data "+dataitem+" is in pointer "+str(pointer))
            else:
                if option=="4":
                    outputallnodes(start,listA)
                    print("The free pointer is",free)
                    print("The root pointer is", start)
                else:
                    break
                
                

