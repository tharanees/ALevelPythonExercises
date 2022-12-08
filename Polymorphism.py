class product:
    def __init__(self,xitem_no):
        self.__item_no=xitem_no
    def get_data(self):
        return(self.__item_no)
    def print_data(self):
        print(self.__item_no)
class cd(product):
    def __init__(self,xitem_no,xartist):
        product.__init__(self,xitem_no)
        self.__artist=xartist
    def print_data(self):
        product.print_data(self)
        print(self.__artist)
class book(product):
    def __init__(self,xitem_no,xauthor_id):
        product.__init__(self,xitem_no)
        self.__author_id=xauthor_id
    def print_data(self):
        product.print_data(self)
        print(self.__author_id)
xitem_no=input("enter the item_no")
xartist=input("enter the artist")
xauthor_id=input("enter the author id")
ThisCd=cd(xitem_no,xartist)
ThisBook=book(xitem_no,xauthor_id)
ThisCd.print_data()
ThisBook.print_data()
