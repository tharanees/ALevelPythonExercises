def factorial (num):
    if num==1:
        result=1
    else:
        result=num*factorial(num-1)
    return result
num=int(input("enter number"))
answer=factorial(num)
print(answer)
