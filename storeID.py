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
        if csvInstance.countEntries() > -1:
            usernames = []  # List to store usernames
            with open(self.filePath, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Skip the header row
                for row in csv_reader:
                    usernames.append(row[1])  # Append the username to the list
            return usernames
        else:
            return "sheet doesn't exist"

    def getTokenByUsername(self, username):
        if csvInstance.countEntries() > -1:
            with open('tokens.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if row[1] == username:
                        return row[0]  # Return the token associated with the username

    def countEntries(self):
        with open(self.filePath, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            return len(list(csv_reader)) - 1

    def reset(self):
        with open(self.filePath, 'w', newline='') as csv_file:
            print("reset succesfull")

csvInstance = Csv()
usernames = csvInstance.read()

for idx, username in enumerate(usernames, start=1):
    print(f"Username {idx}: {username}")

# Get all usernames individually
print(usernames)
# Print username 10 if it exists
if len(usernames) >= 3:
    username_3 = usernames[2]  # Index 9 corresponds to the 10th username
    print("Username 10:", username_3)
else:
    print("Username 10 not found.")
usernameToFind = "user2"
tokenFound = csvInstance.getTokenByUsername(usernameToFind)
if tokenFound:
    print(f"The token for '{usernameToFind}' is: {tokenFound}")
else:
    print(f"Username '{usernameToFind}' not found.")
csvInstance.reset()