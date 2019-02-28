List=[55,78,21,3,5,98,47,50]

def selectionSort(List):
    for i in range(len(List)-1,0,-1):
        minimum = 0
        for j in range(1,i+1):
            
