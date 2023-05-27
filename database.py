import mysql.connector

cnx = mysql.connector.connect(host='127.0.0.1', port='3306', user='neb120', password='Bentofon12', database='geometricDatabase')
cursor = cnx.cursor()

addPlayerDetails = ("INSERT INTO playerDetails "
               "(userId, userName, password, email, statsId, settingsId) "
               "VALUES (%s, %s, %s, %s, %s, %s)")


playerData = ('10000000', 'neb120', 'Bentofon12', 'Benmosborn2006@gmail.com', '10000001', '10000002')

# Insert new player
cursor.execute(addPlayerDetails, playerData)

cnx.commit()

cursor.close()
cnx.close()