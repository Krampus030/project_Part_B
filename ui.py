
class CustomerCLI:
    def __init__(self, admin_instance, user_instance):
        self.admin = admin_instance
        self.user = user_instance
        self.commands = {
            "1": self.help,
            "2": self.check_availabitily,
            "3": self.book,
            "4": self.cancel,
            "5": self.status,
            "exit": self.exit,
            "admin": self.login
        }

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.admin.login(username, password)


    def help(self):
        print("\nAvailable commands:")
        print("  1.help                - show help message.")
        print("  2.check availability  - check available seat.")
        print("  3.book a seat(s)      - book a seat by entering personal information.")
        print("  4.cancel a seat       - cancel a seat by entering the exact the same information while booking.")
        print("  5.booking status      - check the booking status.")
        print("  exit                  - exit the program.")
        print("  admin login           - * admin account, staff only.")