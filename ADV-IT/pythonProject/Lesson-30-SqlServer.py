import pypyodbc
import sys

MySQLServer = "LAPTOP-KRVOOSJM\SQLEXPRESS"
MyDatabase = "Test"

connection = pypyodbc.connect('Driver= {SQL Server};'
                              'Server=' + MySQLServer + ';'
                              'Database=' + MyDatabase + ';'
                              #'uid=username;'
                              #'pwd=mypassword;'
                                                )
cursor = connection.cursor()
try:
    MySqlQuery = ("""
                    SELECT id, first_name, lst_name, phone_number
                    FROM dbo.Customer
                    WHERE last_name = 'Zhuravlev'       
            """)
    cursor.execute(MySqlQuery)
    results = cursor.fetchall()


    for row in results:
        id = row[0]
        firstname =  row[1]
        lastname = row[2]
        phonenumber = row[3]

        print("Welcome " + str(firstname) + " " + str(lastname) + " your telephone number is " + str(phonenumber) +
             " and your id is " + str(id))
except Exception:
    print(sys.exc_info()[1])
else:
    print("Catch successful result")
connection.close()
