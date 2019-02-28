my_list=[1,2,3,4]
def changeme(mylist):
   my_list=[1,4,2,4]
    print("My list inside the function:",my_list)
    return
changeme(my_list)
print("My list outside the function:",my_list)
    
