L=[1,21,5,6]
a=5

def linier_search(L,key):
    #print(L)
    for i in range(0, len(L)):
        #print(i,L[i], key)
        if(key == L[i]):
            return i

    return 'Key Not Found'

r=linier_search(L,a)
print(r)
