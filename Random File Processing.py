import pickle
class record:
    def __init__(self):
        self.ITEM_NO=""
        self.ITEM_NAME=""
        self.PRICE=0
ThisItem=record()
ThisItem.ITEM_NO=input("")
ThisItem.ITEM_NAME=input("")
ThisItem.PRICE=int(input(""))
filehandle=open("PRODUCT.DAT","rb+")
address=hash(ThisItem.ITEM_NO)
filehandle.seek(address)
pickle.dump(ThisItem,filehandle)
filehandle.close()
filehandle=open("PRODUCT.DAT","rb")
SearchID=input("")
address=hash(SearchID)
filehandle.seek(address)
ThisItem=pickle.load(filehandle)
print(ThisItem.ITEM_NO)
print(ThisItem.ITEM_NAME)
print(ThisItem.PRICE)
filehandle.close()
