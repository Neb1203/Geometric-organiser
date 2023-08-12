import sys

class TokenModifier:
    def __init__(self):

        self.file_path = r"E:\Computer Science\Programming project\geometric-organiser-api\tokens.txt"
            # os.path.join(self.current_directory, "tokens.txt")
    def read_session_ids(self):
        session_ids = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    session_id = line.strip()  # Remove leading/trailing whitespace and newline
                    if session_id:
                        session_ids.append(session_id)
                        print(session_ids)
            return session_ids
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def write_session_ids(self, session_ids):
        try:
            with open(self.file_path, "w") as file:
                for session_id in session_ids:
                    file.write(session_id + "\n")  # Write each session ID on a new line
            print("Session IDs updated successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

tokenModifer = TokenModifier()
print(tokenModifer.read_session_ids())
