class CLASSA:
    def __init__(self):
        self.__x=""
    def set_data (self,xdata):
        self.__x=xdata
    def get_data (self):
        return self.__x
OBJA=CLASSA()
OBJA.set_data("45")
y=OBJA.get_data()
print(y)
