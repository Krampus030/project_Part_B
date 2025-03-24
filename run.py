from admin import admin1
from ui import CustomerCLI, CompanyCLI



class CLIApp:
    """
    Command-line application for user authentication.
    """

    def __init__(self):
        self.admin1 = admin1
        self.customer1 = customer1
        self.customer = CustomerCLI(self.admin)
        self.admin = CompanyCLI(self.admin)

    def run(self):
        """
        Interactive CLI loop for handling customer commands.
        """
        while True:
            command_set = self.admin if self.logged_in else self.customer

            command_name = input("Enter command: ").strip()

            command = command_set.commands.get(command_name)

            if command:
                command()
            else:
                print(f"Error: Unknown command '{command_name}'.")
                print("Use 'help' to see available commands.")


if __name__ == "__main__":
    app = CLIApp()
    app.run()