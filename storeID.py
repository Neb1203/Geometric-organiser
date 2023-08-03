import csv

class Csv:
    file_path = 'tokens.csv'
    def write(self, token, userName):
        num_entries = self.count_entries()
        if num_entries >= 5:
            raise ValueError("Maximum number of entries (5) reached.")
        else:
            with open(self.file_path, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([token, userName])

    def read(self):
        if csv_instance.count_entries() > -1:
            usernames = []  # List to store usernames
            with open(self.file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)  # Skip the header row
                for row in csv_reader:
                    usernames.append(row[1])  # Append the username to the list
            return usernames
        else:
            return "sheet doesn't exist"

    def get_token_by_username(self, username):
        if csv_instance.count_entries() > -1:
            with open('tokens.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    if row[1] == username:
                        return row[0]  # Return the token associated with the username

    def count_entries(self):
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            return len(list(csv_reader)) - 1

    def reset(self):
        self.file_path = 'tokens.csv'
        with open(self.file_path, 'w', newline='') as csv_file:
            pass

csv_instance = Csv()
usernames = csv_instance.read()
if csv_instance.count_entries() > -1:
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
username_to_find = "user2"
token_found = csv_instance.get_token_by_username(username_to_find)
if token_found:
    print(f"The token for '{username_to_find}' is: {token_found}")
else:
    print(f"Username '{username_to_find}' not found.")