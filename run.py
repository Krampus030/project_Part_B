from admin import admin1
from customer import customer1
from ui import CustomerCLI, CompanyCLI



class CLIApp:
    """
    Command-line application for user authentication.
    """

    def __init__(self):
        self.admin = admin1
        self.customer1 = customer1
        self.customer_cli = CustomerCLI(self.admin, self.customer1)
        self.admin_cli = CompanyCLI(self.admin)

    def run(self):
        """
        Interactive CLI loop for handling customer commands.
        """
        print("=== Welcome to the Seat Booking CLI ===")
        print("Type '1' for help menu.")

        while True:
            command_set = self.admin_cli if self.admin.logged_in else self.customer_cli

            command_name = input("Enter command: ").strip()

            command = command_set.commands.get(command_name)

            if command:
                command()
            else:
                print(f"Error: Unknown command '{command_name}'.")
                print("Use '1' to see available commands.")


if __name__ == "__main__":
    app = CLIApp()
    app.run()

