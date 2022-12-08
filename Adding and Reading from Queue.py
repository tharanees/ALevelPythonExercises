Q=[0 for c in range (1,8)]
maximum=6
size=0
front=1
rear=0
choice="Yes"
while size!=maximum and choice=="Yes":
    if rear==maximum:
        rear=1
    else:
        rear+=1
    Q[rear]=input("enter new item")
    size+=1
    choice=input("enter")
while size!=0:
    print(Q[front])
    size=size-1
    if front==maximum:
        front=1
    else:
        front+=1
    
