import pyodbc
import datetime
import Selenium

con = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-B2TO9V3\VARUN;'
                      'Database=library;'
                      'Trusted_Connection=yes;')
cursor = con.cursor()
##UI1=int(input('SELECT OPTIONS BELOW\n WHAT IS YOUR ROLE?\n 1.LIBRARIAN\n 2.USER\n 3.Exit\n Select your Option:'))

def menu():
    print("   1.Register as a Student")
    print("   2.Register as a Librarian")
    print("   3.Enter New Book")
    print("   4.Update Student Details")
    print("   5.Update Book details")
    print("   6.View Books Available")
    print("   7.View Student List")
    ch = int(input("Please Enter a Choice: "))
    if(ch == 1):
        name = input("Enter Your Name: ")
        CNo = input("Enter Contact Number: ")
        cursor.execute('insert into student values(?,?)',(name,CNo))
        print("Record Inserted Successfully")
    elif(ch == 2):
        Lname = input("Enter Name: ")
        LCNo = input("Enter Contact Number: ")
        cursor.execute('insert into librarian values(?,?)',(Lname,LCNo))
        print("Record Inserted Successfully")
    elif(ch == 3):
        Bname = input("Enter Book Name: ")
        Author_Name = input("Enter Author name: ")
        ISBN = input("Emter ISBN number for book: ")
        cursor.execute('insert into book_d values(?,?,?)',(Bname,Author_Name,ISBN))
        print("Record Inserted Successfully")
    elif(ch == 4):
        sid = input('Enter Student Id: ')
        name = input('Enter new name: ')
        CNo = input('Enter New Contact number: ')
        cursor.execute('EXEC update_stud @StudName=?,@StudCNo=?,@Studid=?',(name,CNo,sid))
        print("Record updated Successfully")
    elif(ch == 5):
        bid = input('Enter ID for book which is to be updated: ')
        bname = input(' enter new book name: ')
        Isbn = input('enter new ISBN number: ')
        Author = input('Enter new author name: ')
        cursor.execute('EXEC books @bookId=?,@bookname=?,@ISBNNo=?,@bookAName=?',(bid,bname,Isbn,Author))
        print('Records Updated Successfully')
    
        


##for row in cursor:
##    print(row)
menu()

con.commit()
con.close()
