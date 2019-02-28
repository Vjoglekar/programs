import pymssql
conn = pymssql.connect(
    
    host=r'DESKTOP-B2TO9V3\VARUN',
    user=r'DESKTOP-B2TO9V3\VARUN',
    password=9881340577,
    database='practice'
)
con = pymssql.connect(server,user,password,"practice")
cursor = con.cursor()
cursor.executemany("insert into student values(%d,%s,%d),[(1, 'John Smith',20 ),(2, 'Jane Doe', 22),(3, 'Mike T.', 21)]")
con.commit()
con.close()
                   
