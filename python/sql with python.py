import pyodbc # type: ignore

connection_string=("Driver={ODBC Driver 17 for SQL Server};"
                   "Server=LAPTOP-2JD3H0E6;"
                   "Database=eccomerce;"
                   "Trusted_Connection=yes;") 
try:
    connection=pyodbc.connect(connection_string)
    cursor=connection.cursor()
    print("connection successfull")
    cursor.execute("select * from customers")
    cursor.execute("select name from customers where customer_id=1 ")
    rows=cursor.fetchall()
    for row in rows:
        print(row) # print each row in customers table
    connection.close()
except exception as e: # type: ignore
    print("error",e)
