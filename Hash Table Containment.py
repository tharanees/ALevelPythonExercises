class Hash_Table:
    def __init__(self):
        self.__list=[]
        for i in range (5):
            self.__list.append(node())
    def Hash(self,key_field):
        address=key_field%10
        return address
    def insert(self,new_key,new_data):
        TableFull=False
        index=self.Hash(new_key)
        pointer=index
        while (self.__list[pointer]).get_key() !=-1 and TableFull==False:
            pointer+=1
            if pointer>=5:
                pointer=0
            if pointer==index:
                TableFull=True
        #if TableFull is false, then not TableFull will be true
        if not TableFull:       
            self.__list[pointer].set_data(new_key,new_data) 
        else:
            print("Table is Full")
    def find(self,SearchKey):
        ItemNotExist=False
        index=self.Hash(SearchKey)
        pointer=index
        while self.__list[pointer].get_key()!=SearchKey and ItemNotExist==False :
            pointer+=1
            if pointer>=5:
                pointer=0
            if pointer==index:
                ItemNotExist=True
        if ItemNotExist==False:
            print("THE KEY IS",self.__list[pointer].get_key())
            print("THE DATA IS",self.__list[pointer].get_data())
        else:
            print("Record not found")
class node:
    def __init__(self):
        self.__key=-1
        self.__data=""
    def set_data(self,xkey,xdata):
        self.__key=xkey
        self.__data=xdata
    def get_key(self):
        return(self.__key) 
    def get_data(self):
        return(self.__data)

mylist=Hash_Table()
mylist.insert(4521,"jo")
mylist.insert(9874,"jim")
mylist.insert(4781,"khan")
mylist.insert(9994,"jonny")
mylist.insert(9991,"mary")
while True:
    #assuming the search key is existing in the hash table.
    search=int(input("searching item?")) 
    mylist.find(search)
