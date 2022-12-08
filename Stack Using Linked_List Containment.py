class STACK:
    def __init__(self):
        self.__start=None
        self.__free=0
        self.__stack=[]
        for c in range (3):
            self.__stack.append(node(c+1))
        self.__stack.append(node(None))
    def insert(self,dataitem):
        if self.__free != None: #stack not full
            temp=self.__free
            self.__stack[temp].set_data(dataitem)
            self.__free=self.__stack[temp].get_ptr()
            self.__stack[temp].set_ptr(self.__start)
            self.__start=temp
        else:
            print("stack is full")
    def pop(self):
        if self.__start!=None:
            a=(self.__stack[self.__start].get_data())
            print(a)
            temp=self.__stack[self.__start].get_ptr()
            self.__stack[self.__start].set_ptr(self.__free)
            self.__free=self.__start
            self.__start=temp
        else:
            print("stack is empty")
class node:
    def __init__(self,val):
        self.__data=""
        self.__pointer=val
    def set_data(self,xdata):
        self.__data=xdata
    def set_ptr(self,xptr):
        self.__pointer=xptr
    def get_data(self):
        return(self.__data)
    def get_ptr(self):
        return(self.__pointer)
MyStack=STACK()
MyStack.insert("B")
MyStack.pop()


MyStack.pop()
MyStack.insert("C")
MyStack.insert("D")
MyStack.pop()
MyStack.insert("A")
MyStack.insert("E")
MyStack.pop()
MyStack.pop()
MyStack.pop()
MyStack.insert("G")
MyStack.insert("M")
MyStack.pop()
MyStack.pop()
