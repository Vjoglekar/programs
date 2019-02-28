with open('E:\Fileexmp.txt','w') as f:
    f.write('write')

with open('E:\Fileexmp.txt') as f:
    print(f.read())
