import mysql.connector

cnx = mysql.connector.connect(host='127.0.0.1', port='3306', user='neb120', password='Bentofon12', database='geometricDatabase')
cursor = cnx.cursor()

addPlayerDetails = ("INSERT INTO playerDetails "
               "(userName, password, email) "
               "VALUES (%s, %s, %s)")


playerData = ('neb1203', 'Bentofon123', 'neb120345@gmail.com')

# Insert new player
cursor.execute(addPlayerDetails, playerData)

cnx.commit()

cursor.close()
cnx.close()