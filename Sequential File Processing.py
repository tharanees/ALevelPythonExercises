import pickle
class CarRecord:
    def __init__(self):
        self.VehicleID=""
        self.Registration=""
CAR=[CarRecord() for count in range (3)]
for count in range (3):
    CAR[count].VehicleID=input("")
    CAR[count].Registration=input("")
Filehandle=open("car.DAT","wb")
for count in range (3):
    pickle.dump(CAR[count],Filehandle)
Filehandle.close()
Filehandle=open("car.DAT","rb")
car=[]
for count in range (3): #not for count in range (1,3) bcs when appending an array indexing starts from 0
    car.append(pickle.load(Filehandle))
Filehandle.close()
for count in range (3):
     print(car[count].VehicleID,car[count].Registration)
