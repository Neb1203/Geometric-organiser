import uuid

class HashingGenerator:
    def password(self, password):
        hashUserID = uuid.uuid5(uuid.NAMESPACE_URL, password)
        return hashUserID
        print("Success")


