class Binary_Tree:
    def __init__(self):
        self.__start=None
        self.__free=0
        self.__Tree=[]
        for count in range (6):
            self.__Tree.append(node(count+1,"",None))
        self.__Tree.append(node(None,"",None))
    def add_node(self,NewData):
        if self.__free==None:
            print("Tree is full")
        else:
            self.__Tree[self.__free].set_data(NewData)
            temp=self.__free
            self.__free=self.__Tree[self.__free].get_leftpointer()
            self.__Tree[temp].set_leftpointer(None)
            self.__Tree[temp].set_rightpointer(None)
            if self.__start == None:
                self.__start=temp
            else:
                ThisNodePointer=self.__start
                while ThisNodePointer != None: #repeats until leaf node is reached
                    previous=ThisNodePointer
                    if self.__Tree[ThisNodePointer].get_data()>NewData:
                        turnedleft=True
                        ThisNodePointer=self.__Tree[ThisNodePointer].get_leftpointer()
                    else:
                        turnedleft=False
                        ThisNodePointer=self.__Tree[ThisNodePointer].get_rightpointer()
                if turnedleft==True:
                    self.__Tree[previous].set_leftpointer(temp)
                else:
                    self.__Tree[previous].set_rightpointer(temp)

    def findnode(self,dataitem):
        ThisNodePointer=self.__start
        Found=False
        while ThisNodePointer!=None and Found==False:
            if self.__Tree[ThisNodePointer].get_data()==dataitem:
                Found=True
            else:
                if self.__Tree[ThisNodePointer].get_data()>dataitem:
                    ThisNodePointer=self.__Tree[ThisNodePointer].get_leftpointer()
                else:
                    ThisNodePointer=self.__Tree[ThisNodePointer].get_rightpointer()
        return ThisNodePointer #returns null pointer if item not found

class node:
    def __init__(self,xleft,xdata,xright):
        self.__left=xleft
        self.__data=xdata
        self.__right=xright
    def set_data(self,xdata):
        self.__data=xdata
    def set_leftpointer(self,xleft):
        self.__left=xleft
    def set_rightpointer(self,xright):
        self.__right=xright
    def get_data(self):
        return(self.__data)
    def get_leftpointer(self):
        return(self.__left)
    def get_rightpointer(self):
        return(self.__right)
MyTree=Binary_Tree()
MyTree.add_node("J")
MyTree.add_node("C")
MyTree.add_node("L")
MyTree.add_node("B")
MyTree.add_node("K")
MyTree.add_node("D")
MyTree.add_node("M")
x=MyTree.findnode("K")
print(x) #prints 4

