def add_node(dataitem):
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
            while ThisNodePointer != None: #repeats until leaf node is reached
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

def findnode(dataitem):
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
    return ThisNodePointer #returns null pointer if item not found

def create_tree():    
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


