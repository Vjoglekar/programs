import pyodbc
import datetime

con = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-B2TO9V3\VARUN;'
                      'Database=library;'
                      'Trusted_Connection=yes;')
cursor = con.cursor()

class Librarian:
    
    def __init__(self,Lname,Lusername,LCN0):
        
	self.Lname=Lname
	self.Lusername=Lusername
	self.LCNo=LCNo
    def PrintingL(self):
	print('Your details are as follows:\nName:'+self.Lname, '\nContact email:'+self.LCN0,'\nYour USERNAME is '+ self.Lusername)
    def uploadl(self):
	cursor.execute('insert into librarian values(?,?,?)',(self.Lname,self.LCNo,self.Lusername))
    def newlibrarian(self,lname,lusername,lcontact):
	self.lname=str(input('Enter your name:'))
	self.lusername=str(input('Enter a preferred/unique user name:'))
	self.lcontact=str(input)


class book:
    
    def __init__(self,bname,author,rentday,rentu):
    
	self.bname=bname
	self.author=author
	self.rentday=rentday
	self.rentU=rentU
    def addbook(self):
	cursor.execute('insert into book_d values(?,?,?,?)',(self.bname,self.author,self.rentday,self.rentU))

class User:
    def __init__(self,name,username,contact):
	self.name=name
	self.username=username
	self.contact=contact
    def PrintingU(self):
	print('Your details are as follows:\nName:'+self.name, '\nContact email:'+self.contact,'\nYour USERNAME is '+ self.username)
    def uploadu(self):
		cursor.execute("INSERT INTO users VALUES (?, ?, ?)",(self.name, self.contact, self.username))



MScreen1=int(input('\n SELECT OPTIONS \n WHAT IS YOUR ROLE?\n 1.LIBRARIAN\n 2.USER\n 3.Exit\n Select your Option:'))
if MScreen1==1:
    
    MScreen2=int(input('\n SELECT OPTIONS BELOW\n 1.REGISTER IF YOU DONT HAVE AN ACCOUNT\n 2.LOG IN using your USERNAME\n 3.EXIT\n SELECT YOUR OPTION:'))
    if MScreen2==1:
        # Librarian Registration
	Lname=str(input('Librarian,Enter your name:'))
	Lusername=str(input('Enter a user name:'))
	LCNo=str(input('Provide your ContactNo:'))
	lib=Librarian(Lname,Lusername,LCNo)
	lib.uploadl()

    if MScreen2==2:
	ln=str(input('Enter your username:'))
	connection=sqlite3.connect('Library.db')
	cursor=connection.cursor()
	cursor.execute('SELECT Name FROM librarians WHERE username=(?);',(ln,))
	lbl=(cursor.fetchall())
	for i, in lbl:
            
	    print(****************\n\nWelcome to the Byte Library,',i)

        MScreen2=(int(input('\n\nWhat would you like to do?\n 1.VIEW ALL BOOKS\n 2.ADD BOOKS TO LIBRARY\n 3.DELETE A BOOK\n 4.DELETE USER\n 5.UPDATE RENTAL DATE of a BOOK\n 6.VIEW OVERDUE BOOKS\n 7.DETAILS OF FINES\n 8.EXIT\n Select your option:')))
        if Mscreen2==3:
                  # Viewbooks
                  print('\n**List of ALL books:**\n (Book Name, Aithor)')
                  query='SELECT BName,Author FROM book_d;'
                  cursor.execute(query)
		  rows=cursor.fetchall()
                  for i in rows:
                      print(i)
		  
                  
                  
                  
                    
                  
                  
		       
























con.commit()
con.close()
