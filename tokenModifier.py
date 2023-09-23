import sys

class TokenModifier:
    def __init__(self):

        self.file_path = r"tokens.txt"
            # os.path.join(self.current_directory, "tokens.txt")
    def get_last_session(self):
        session_ids = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    session_id = line.strip()  # Remove leading/trailing whitespace and newline
                    if session_id:
                        session_ids.append(session_id)
            if session_ids:
                lastSessionIndex = len(session_ids) - 1
                return session_ids[lastSessionIndex]
            return None
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

