import csv
import pandas as pd
class UsernamesModel:
    filePath = 'tokens.csv'
    noData = "noData"
    def write(self, token, userName):
        if self.countEntries() >= 5:
            raise ValueError("Maximum number of entries (5) reached.")
        else:
            with open(self.filePath, 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([token, userName])

    def update_csv_column(self, target_column_index, new_value):
        df = pd.read_csv(self.filePath, header=None, na_values='nan')

        # Update the values in the target column
        df[target_column_index] = df[target_column_index].astype(str).str.strip().str.lower()

        # Find the first occurrence of "nodata" or "empty slot" and replace it with the new value
        first_occurrence_idx = df.index[
            (df[target_column_index] == self.noData) | (df[target_column_index] == "empty slot")].min()
        if pd.notna(first_occurrence_idx):
            df.at[first_occurrence_idx, target_column_index] = new_value.lower()

        # Convert NaN values to the desired string value
        df = df.fillna(self.noData)

        # Save the modified DataFrame back to the CSV file
        df.to_csv(self.filePath, header=False, index=False)

    def read(self):
        if csvInstance.countEntries() > -1:
            usernames = []  # List to store usernames
            with open(self.filePath, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    usernames.append((row[0], row[1]))
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
            for i in range(5):
                csvInstance.write(self.noData, "Empty slot")

    def userNameIndex(self, targetIndex):
        # Print username 10 if it exists
        usernames = self.read()
        if usernames != None:
            if len(usernames) >= targetIndex:
                return usernames[targetIndex]
            else:
                return "not found"
        else:
            print("There are no usernames stored")

csvInstance = UsernamesModel()
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
# target_column_index = 0  # Replace this with the index of your target column (zero-based)
# new_value = "gay"  # Replace this with the value you want to set for rows with "clear"
#
# csvInstance.update_csv_column(target_column_index, new_value)
usernames = csvInstance.read()
print(usernames)