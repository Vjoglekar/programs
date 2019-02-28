class Taxi:
    NoOfTaxis=0
    @classmethod
    def getnooftaxi(cls):
        return cls.NoOfTaxis
    
    def __init__(self,drivername,onDuty,cities):
        self.dname=drivername
        self.oduty=onDuty
        self.cities=cities
        self.passengerNo=0
        Taxi.NoOfTaxis=Taxi.NoOfTaxis+1

    def changeDname(self,NewName):
        self.dname=NewName

    def pickPass(self,NumOfPass):
        self.passengerNo+=NumOfPass
        
    def splitname(self):
        return self.dname.split()
        

T1=Taxi("Alex Turner",True,['Banglore','Hosur'])
T2=Taxi("Bob Marshal",True,['Pune','Mumbai'])
T3=Taxi("XYZ",True,['XXX'])
print(T1.dname)
##T1.changeDname('Bob Marshal')
##print('Changed Name is:',T1.dname)
##
##T1.pickPass(1)
##print('Passenger Number Incremented to :',T1.passengerNo)
print("Number Of Taxis We have :",Taxi.getnooftaxi(),"Taxi's")

