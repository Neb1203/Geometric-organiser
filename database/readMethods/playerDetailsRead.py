import mysql.connector

class playerDetails:
    def __init__(self):
        cnx = mysql.connector.connect(host='127.0.0.1', port='3306', user='neb120', password='Bentofon12', database='geometricDatabase')
        cursor = cnx.cursor()
    def read(self, select, email, password):
        qry = """SELECT %s FROM playerDetails
                 "WHERE email = %s AND password = %s"""
        data = (select, email, password)
        self.cursor.execute(qry, data)

# hire_start = datetime.date(1999, 1, 1)
# hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, 4) #, (hire_start, hire_end)

for (userName, password, email) in cursor:
    print(userName, password, email)
    print(password)
cursor.close()
cnx.close()