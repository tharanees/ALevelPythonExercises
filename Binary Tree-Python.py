def add_node(dataitem,free,start,Tree):
    if free==None:
        print("Tree is full")
    else:
        Tree[free].data=newitem
        temp=free
        free=Tree[free].leftpointer
        Tree[temp].leftpointer=None
        Tree[temp].rightpointer=None
        if start == None:
            start=temp
        else:
            ThisNodePointer=start
            while ThisNodePointer != None:
                previous=ThisNodePointer
                if Tree[ThisNodePointer].data>dataitem:
                    turnedleft=True
                    ThisNodePointer=Tree[ThisNodePointer].leftpointer
                else:
                    turnedleft=False
                    ThisNodePointer=Tree[ThisNodePointer].rightpointer
            if turnedleft==True:
                Tree[previous].leftpointer=temp
            else:
                Tree[previous].rightpointer=temp
    return (free,start,Tree)
def findnode(dataitem,start,Tree):
    ThisNodePointer=start
    Found=False
    while ThisNodePointer!=None and Found==False:
        if Tree[ThisNodePointer].data==dataitem:
            Found=True
        else:
            if Tree[ThisNodePointer].data>dataitem:
                ThisNodePointer=Tree[ThisNodePointer].leftpointer
            else:
                ThisNodePointer=Tree[ThisNodePointer].rightpointer
    return ThisNodePointer

    
class node:
    def __init__(self,left,right):
        self.data=""
        self.leftpointer=left
        self.rightpointer=right
Tree=[]
for count in range (6):
    Tree.append(node(count+1,None))
Tree.append(node(None,None))
start=None
free=0
print("1. ADD NEW NODE")
print("2. FIND A NODE")
print("3. OUTPUT TREE")
print("4. EXIT")
while True:
    option=input("ENTER THE OPTION")
    if option=="1":
        newitem=input("enter new item to be added")
        free,start,Tree=add_node(newitem,free,start,Tree)
    else:
        if option=="2":
            dataitem=input("enter the data item to be searched")
            pointer=findnode(dataitem,start,Tree)
            print("The data "+dataitem+" is in pointer "+str(pointer))
        else:
            if option=="3":
                for c in range (len(Tree)):
                    print(Tree[c].leftpointer,Tree[c].data,Tree[c].rightpointer)
            else:
                break

                
