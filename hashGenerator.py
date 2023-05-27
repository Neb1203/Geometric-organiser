import sqlite3
import uuid


class HashingGenerator:
    def __init__(self):
        pass
    def UserName(self, userName):
        hashUserId = uuid.uuid5(uuid.NAMESPACE_URL, userName)
        print(hashUserId)
hashingGenerator = HashingGenerator()
hashingGenerator.UserName("neb120")
