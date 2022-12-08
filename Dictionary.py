# create a dictionary
phonedirectory={}
# enter data into dictionary
for count in range (3):
    name=input("enter the name")
    phone=input("enter the phone number")
    phonedirectory[name]=phone
#print the name and number in the dictionary
for name in phonedirectory:
    print(name)
    print(phonedirectory[name])
#ALTERNATIVELY
for name,number in phonedirectory.items():
    print(name, number, sep = " | ") # by default sep = " "
#print the number of a specific person
search_name=input("enter the name of whose number is needed")
if search_name in phonedirectory:
    print(phonedirectory[search_name])
