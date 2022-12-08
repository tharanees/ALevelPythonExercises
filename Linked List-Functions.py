def add(newitem):
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

def delete (dataitem):
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

def findnode(dataitem):
    ThisNodePointer=start
    while ThisNodePointer!=None and listA[ThisNodePointer].data!=dataitem:
        ThisNodePointer=listA[ThisNodePointer].pointer
    return ThisNodePointer  # returns null pointer if item is not found

#ALTERNATIVE TO FIND NODE
def findnode_alt(dataitem):
    ThisNodePointer=start
    Found=False
    while ThisNodePointer!=None and Found==False:
        if listA[ThisNodePointer].data==dataitem:
            Found=True
        else:
            ThisNodePointer=listA[ThisNodePointer].pointer
    return ThisNodePointer


def outputallnodes():
    ThisNodePointer=start
    while ThisNodePointer!=None:
        print(listA[ThisNodePointer].data," ",listA[ThisNodePointer].pointer)
        ThisNodePointer=listA[ThisNodePointer].pointer

def create_list():
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

                

