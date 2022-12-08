array=[0 for count in range (1,12)]
for count in range (1,11):
    array[count]=int(input("enter the number to the array"))
search=int(input("enter the number to be searcheed"))
hp=10
lp=1
found=False
notfound=False
while found==False and notfound==False:
    mp=int((lp+hp)/2)
    if array[mp]==search:
        found=True
    else:
        if lp>=hp:
            notfound=True
        else:
            if array[mp]<search:
                lp=mp+1
            else:
                hp=mp-1
if found==True:
    print(mp)
else:
    print("not found")
