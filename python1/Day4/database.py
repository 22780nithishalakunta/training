import pyodbc
server='HYDTRNG14\SQLEXPRESS'
database='python'
username='sa'
password='nithish@780'
cxcn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


mycursor=cxcn.cursor()
res=mycursor.execute("select empno,sal,comm,(sal+comm) as salary from emp")
myrecs=res.fetchall();
print(myrecs)
