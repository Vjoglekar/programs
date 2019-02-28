List=[55,78,21,3,5,98,47,50]

def bubbleSort(List):
    for i in range(len(List)-1,0,-1):
        for j in range(i):
            if(List[j] > List[j+1]):
                List[j],List[j+1]= List[j+1],List[j]
        print(List)

        
bubbleSort(List)
print(List)
