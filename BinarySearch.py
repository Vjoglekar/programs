L=[1,25,36,7,52,0]
key=7
L.sort()
print(L)
def binary_search(searchList,key):

    length=len(searchList)
    low=0
    upper= length - 1

    while(low <= upper):
        middle=(low + upper)//2

        if(key == searchList[middle]):
            return middle
        elif (key < searchList[middle]):
            upper = middle - 1

        elif (key > searchList[middle]):

            low= middle + 1
    return False

r=binary_search(L,key)
print(r)
