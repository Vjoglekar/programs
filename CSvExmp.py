import csv
fr = open('s.csv','rt')
fw = open('s1.csv','wt')

try:
    reader = csv.reader(fr)
    writer = csv.writer(fw)

    for row in reader:
        writer.writerow(row)

        
finally:
    print("Load Complete!!")

    fr.close()
    fw.close()
        
    
