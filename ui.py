import sys
from database import InfoDatabase


class CustomerCLI:
    """
    Command line interface for customer interactions.
    """

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
        """
        Admin login for staff access.
        """
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.admin.login(username, password)

    def check_availability(self):
        """
        Show available seats.
        """
        self.customer.check_availability()

    def book(self):
        """
        Book a seat with customer input.
        """
        self.customer.book()

    def cancel(self):
        """
        Cancel an existing booking.
        """
        self.customer.cancel()

    def status(self):
        """
        Check current booking status.
        """
        self.customer.status()

    def exit(self):
        """
        Exit the program.
        """
        print("Thank you for using the booking system, SEE YOU")
        sys.exit()

    def help(self):
        """
        Display list of available commands.
        """
        print("\nAvailable commands:")
        print("  1.help                - show help message.")
        print("  2.check availability  - check available seat.")
        print("  3.book a seat(s)      - book a seat by entering personal information.")
        print("  4.cancel a seat       - cancel a seat by entering the exact the same information while booking.")
        print("  5.booking status      - check the booking status.")
        print("  exit                  - exit the program.")
        print("  admin login           - * admin account, staff only.")


class CompanyCLI:
    """
    Command line interface for admin operations.
    """

    def __init__(self, admin_instance):
        self.admin = admin_instance
        self.db = InfoDatabase()
        self.commands = {
            "1": self.help,
            "2": self.check_customer_info,
            "3": self.check_customer,
            "4": self.logout
        }

    def logout(self):
        """
        Log out of the admin interface.
        """
        self.admin.logout()

    def check_customer_info(self):
        """
        Display all current bookings.
        """
        print("\n--- All Bookings ---")
        bookings = self.db.get_all_customer()
        if not bookings:
            print("No bookings found.")
            return

        for i, (name, gender, phone, passport) in enumerate(bookings, start=1):
            print(f"{i}. Name: {name}, Gender: {gender}, Phone: {phone}, Passport: {passport}")
        # for loop to traverse all rows, and display them.


    def check_customer(self):
        """
        Display all current booked seats
        """
        print("\n--- All Bookings ---")
        booking = self.db.get_all_bookings()
        if not booking:
            print("No bookings found.")
            return

        for i, (id, name, reference, seat) in enumerate(booking, start=1):
            print(f"{i}. Id: {id}, Name: {name}, Reference: {reference}, Seat: {seat}")


    def help(self):
        """
        Display list of available admin commands.
        """
        print("\nAvailable commands:")
        print("  1.help                - show help message.")
        print("  2.check customer info   - check the customer info.")
        print("  3.check booked seat   - check the amount the seat booked.")
        print("  4.logout              - back to customer command menu.")


# Startup message
print("Please go to Terminal and input python run.py to use the program")
print("Or run 'run.py' directly")
