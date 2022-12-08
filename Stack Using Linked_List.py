def insert(dataitem,free,start,stack):
    if free != None: #stack not full
        temp=free
        stack[temp].data=dataitem
        free=stack[temp].pointer
        stack[temp].pointer=start
        start=temp
    else:
        print("stack is full")
    return(free,start,stack)  

def pop(free,start,stack):
    if start!=None:
        print(stack[start].data)
        temp=stack[start].pointer
        stack[start].pointer=free
        free=start
        start=temp
    else:
        print("stack is empty")
    return(free,start,stack)


start=None
free=0
class node:
    def __init__(self,val):
        self.data=""
        self.pointer=val
stack=[]
for c in range (3):
    stack.append(node(c+1))
stack.append(node(None))

##testing section
free,start,stack=insert("B",free,start,stack)
print(free,start)
free,start,stack=pop(free,start,stack)
print(free,start)
free,start,stack=pop(free,start,stack)
print(free,start)
free,start,stack=insert("C",free,start,stack)
print(free,start)
free,start,stack=insert("D",free,start,stack)
print(free,start)
free,start,stack=pop(free,start,stack)
print(free,start)
free,start,stack=insert("A",free,start,stack)
print(free,start)
free,start,stack=insert("E",free,start,stack)
print(free,start)
free,start,stack=pop(free,start,stack)
print(free,start)

