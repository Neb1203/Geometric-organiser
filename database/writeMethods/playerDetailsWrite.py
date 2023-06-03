import mysql.connector

class playerDetailsWrite:
    def __init__(self, userName, password, email):
        self.userName = userName
        self.password = password
        self.email = email
    def playerDetailsInsert(self):
        cnx = mysql.connector.connect(host='127.0.0.1', port='3306', user='neb120', password='Bentofon12', database='geometricDatabase')
        cursor = cnx.cursor()
        addPlayerDetails = ("INSERT INTO playerDetails "
                       "(userName, password, email) "
                       "VALUES (%s, %s, %s)")
        playerData = (self.userName, self.password, self.email)
        cursor.execute(addPlayerDetails, playerData)

        cnx.commit()

        cursor.close()
        cnx.close()

playerDetailsWrite("neb1203", "james", "enbb@gmail.com").playerDetailsInsert()
# Insert new player
