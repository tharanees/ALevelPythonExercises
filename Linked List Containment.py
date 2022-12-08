class Linked_List:
    def __init__(self):
        self.__start=None
        self.__free=0
        self.__list=[]
        for count in range (5):
            self.__list.append(node(count+1,""))
        self.__list[4].set_ptr(None)

    def add(self,newitem):
        if self.__free==None:
            print("list full")
        else:
            self.__list[self.__free].set_data(newitem)
            temp=self.__free
            self.__free=self.__list[self.__free].get_ptr()
            ThisNodePointer=self.__start
            while ThisNodePointer!=None and self.__list[ThisNodePointer].get_data()<newitem:
                previous=ThisNodePointer
                ThisNodePointer=self.__list[ThisNodePointer].get_ptr()
            if ThisNodePointer==self.__start:
                self.__list[temp].set_ptr(self.__start)
                self.__start=temp
            else:
                self.__list[temp].set_ptr(self.__list[previous].get_ptr())
                self.__list[previous].set_ptr(temp)
                
    def delete (self,dataitem):
        ThisNodePointer=self.__start
        while ThisNodePointer!=None and self.__list[ThisNodePointer].get_data()!=dataitem:
            previous=ThisNodePointer
            ThisNodePointer=self.__list[ThisNodePointer].get_ptr()
        if ThisNodePointer != None:
            if ThisNodePointer==self.__start:
                self.__start=self.__list[ThisNodePointer].get_ptr()
            else:
                self.__list[previous].set_ptr(self.__list[ThisNodePointer].get_ptr())
            self.__list[ThisNodePointer].set_ptr(self.__free)
            self.__free=ThisNodePointer
        else:
            print("such node doesn't exist in list")

    def findnode(self,dataitem):
        ThisNodePointer=self.__start
        while ThisNodePointer!=None and self.__list[ThisNodePointer].get_data()!=dataitem:
            ThisNodePointer=self.__list[ThisNodePointer].get_ptr()
        return ThisNodePointer  # returns null pointer if item is not found

    #ALTERNATIVE TO FIND NODE
    def findnode_alt(self,dataitem):
        ThisNodePointer=self.__start
        Found=False
        while ThisNodePointer!=None and Found==False:
            if self.__list[ThisNodePointer].get_data()==dataitem:
                Found=True
            else:
                ThisNodePointer=self.__list[ThisNodePointer].get_ptr()
        return ThisNodePointer

    def outputallnodes(self):
        ThisNodePointer=self.__start
        while ThisNodePointer!=None:
            a=self.__list[ThisNodePointer].get_data()
            b=self.__list[ThisNodePointer].get_ptr()
            ThisNodePointer=self.__list[ThisNodePointer].get_ptr()
            print(a,"   ",b)

class node:
    def __init__(self,xptr,xdata):
            self.__data=xdata
            self.__ptr=xptr
    def set_data(self,xdata):
        self.__data=xdata
    def set_ptr(self,xptr):
        self.__ptr=xptr
    def get_data(self):
        return(self.__data)
    def get_ptr(self):
        return(self.__ptr)

MyList=Linked_List()
MyList.add("D")
MyList.add("F")
MyList.add("E")
MyList.add("B")
x=MyList.findnode("B")
print(x) #prints 3
MyList.outputallnodes()


