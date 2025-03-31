import sys
from database import InfoDatabase


class CustomerCLI:
    def __init__(self, admin_instance, customer_instance):
        self.admin = admin_instance
        self.customer = customer_instance
        self.commands = {
            "1": self.help,
            "2": self.check_availability,
            "3": self.book,
            "4": self.cancel,
            "5": self.status,
            "exit": self.exit,
            "admin login": self.login
        }

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.admin.login(username, password)


    def check_availability(self):
        self.customer.check_availability()

    def book(self):
        self.customer.book()

    def cancel(self):
        self.customer.cancel()

    def status(self):
        self.customer.status()

    def exit(self):
        print("Thank you for using the booking system, SEE YOU")
        sys.exit()

    def help(self):
        print("\nAvailable commands:")
        print("  1.help                - show help message.")
        print("  2.check availability  - check available seat.")
        print("  3.book a seat(s)      - book a seat by entering personal information.")
        print("  4.cancel a seat       - cancel a seat by entering the exact the same information while booking.")
        print("  5.booking status      - check the booking status.")
        print("  exit                  - exit the program.")
        print("  admin login           - * admin account, staff only.")



class CompanyCLI:
    def __init__(self, admin_instance):
        self.admin = admin_instance
        self.db = InfoDatabase()
        self.commands = {
            "1": self.help,
            "2": self.check_booked_seat,
            "3": self.logout

        }


    def logout(self):
        self.admin.logout()


    def check_booked_seat(self):
        print("\n--- All Bookings ---")
        bookings = self.db.get_all_bookings()
        if not bookings:
            print("No bookings found.")
            return

        for i, (name, gender, phone, passport) in enumerate(bookings, start=1):
            print(f"{i}. Name: {name}, Gender: {gender}, Phone: {phone}, Passport: {passport}")


    def help(self):
        print("\nAvailable commands:")
        print("  1.help                - show help message.")
        print("  2.check booked seat   - check the amount the seat booked.")
        print("  3.logout              - back to customer command menu.")


print("Please go to Terminal and input python run.py to use the program")
print("Or run 'run.py' directly")
