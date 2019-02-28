class Hippo:
    hippposatZoo=0
    @classmethod
    def getnoofhippo(cls):
        return cls.hippposatZoo

    def __init__(self,HName,HWeight):
        self.hipposName=HName
        self.hippoWeight=HWeight
        Hippo.hippposatZoo=Hippo.hippposatZoo+1

    def Feed(self,HWI):
        
        self.hippoWeight+=HWI
        

    def Exercise(self,HWD):
        
        self.hippoWeight-=HWD

   


H1=Hippo("Jabba",68)
H2=Hippo("XXX",78)
print("total no of Hippos in Zoo=",Hippo.getnoofhippo())
print("Name Of a Hippo:",H1.hipposName,"Weight:",H1.hippoWeight)
H1.Feed(H1.hippoWeight)
print("After Feeding:",H1.hipposName,"Weight :",H1.hippoWeight)
print("Name Of a Hippo:",H2.hipposName,"Weight:",H2.hippoWeight)
H2.Feed(H2.hippoWeight)
print("After Feeding:",H2.hipposName,"Weight :",H2.hippoWeight)
H1.Exercise(H1.hippoWeight)
print("After Exercise:",H1.hipposName,"'s","Weight:",H1.hippoWeight)








        
        

    
    
