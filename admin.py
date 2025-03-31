import json

ADMIN_FILE = "admin.json"


class Admin:
    """
    Manage admin authentication.
    """

    def __init__(self):
        self.admin = self.load_user()  # Load admin credential
        self.logged_in = None  # Track active session

    def load_user(self):
        """
        Load admin credential from file.
        """
        try:
            with open(ADMIN_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                admin = data.get("admin", {})
                return admin
        except (FileNotFoundError, json.JSONDecodeError):
            return {}, {}

    def login(self, username, password):
        """
        Authenticate admin and set session.
        """
        if self.admin.get(username) == password:
            self.logged_in = username
            print(f"Login successful. Welcome, {username}!")
            return True
        print("Error: Invalid username or password.")
        return False

    def logout(self):
        """
        Clear session if admin is logged in.
        """
        if self.logged_in:
            print(f"Admin {self.logged_in} logged out.")
            self.logged_in = None
        else:
            print("No active session.")



admin1 = Admin()
