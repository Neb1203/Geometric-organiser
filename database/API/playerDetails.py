from fastapi import FastAPI
import uvicorn
from databaseConnect import databaseConnector

app = FastAPI()
databaseConnect = databaseConnector
@app.post("/playerDetails/")
def write(user_name: str, password: str, email: str):
    addPlayerDetails = ("INSERT INTO playerDetails "
                        "(userName, password, email) "
                        "VALUES (%s, %s, %s)")
    playerData = (user_name, password, email)
    databaseConnect.cursor.execute(addPlayerDetails, playerData)

    databaseConnect.cnx.commit()

    databaseConnect.cursor.close()
    databaseConnect.cnx.close()
    return("stored")
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.2", port=5000, log_level="info")

