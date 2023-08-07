import csv

class Csv:
    filePath = 'tokens.csv'
    def write(self, token, userName):
        num_entries = self.countEntries()
        if num_entries >= 5:
            raise ValueError("Maximum number of entries (5) reached.")
        else:
            with open(self.filePath, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([token, userName])

    def read(self):
        csvInstance = Csv()
        if csvInstance.countEntries() > -1:
            usernames = []  # List to store usernames
            with open(self.filePath, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Skip the header row
                for row in csv_reader:
                    usernames.append(row[1])  # Append the username to the list
            return usernames
        else:
            print("Sheet is empty")

    def getTokenByUsername(self, username):
        if username != None:
            if csvInstance.countEntries() > -1:
                with open('tokens.csv', 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        if row[1] == username:
                            return row[0]  # Return the token associated with the username
        else:
            return None
    def countEntries(self):
        with open(self.filePath, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            return len(list(csv_reader))

    def reset(self):
        with open(self.filePath, 'w', newline='') as csv_file:
            for i in range(4):
                csvInstance.write("clear", "clear")

    def userNameIndex(self, targetIndex):
        # Print username 10 if it exists
        csvInstance = Csv()
        usernames = csvInstance.read()
        if usernames != None:
            if len(usernames) >= targetIndex:
                return usernames[targetIndex]
            else:
                return "not found"
        else:
            print("There are no usernames stored")
csvInstance = Csv()
# usernames = csvInstance.read()
#
# # if isinstance(usernames, tuple):
# #     for idx, username in enumerate(usernames, start=1):
# #         print(f"Username {idx}: {username}")
# print(csvInstance.userNameIndex(0))
# # Get all usernames individually
# # print(usernames)
# csvInstance.write("jay", "fat")

# usernameToFind = "user2"
# tokenFound = csvInstance.getTokenByUsername(usernameToFind)
# if tokenFound:
#     print(f"The token for '{usernameToFind}' is: {tokenFound}")
# else:
#     print(f"Username '{usernameToFind}' not found.")
# csvInstance.reset()