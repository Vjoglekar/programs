def parentfunction():
    a=20
    def childfun():
        nonlocal a
        a=40
        c=30
        d=a+c
        return d
    childfun()
    print('Printing a',a)
    return childfun
f=parentfunction()
print(f())
