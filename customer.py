class Customer:
    def __init__(self):
        self.seats = self.initialise_seats()


    @staticmethod
    def initialise_seats():
        seats = {}
        for row in "ABCDEF":
            for col in range(1, 81):
                seat_id = f"{col}{row}"
                seats[seat_id] = "F"


        storage_seats = ["77E", "77F", "78E", "78F", "79E", "79F", "80E", "80F"]
        for seat in storage_seats:
            if seat in seats:
                seats[seat] = "S"

        return seats

    def check_availability(self):
        print("Select group to view seat availability:")
        print("1. Seats 1-20")
        print("2. Seats 21-40")
        print("3. Seats 41-60")
        print("4. Seats 61-80")
        choice = input("Enter your choice (1-4): ").strip()

        group_ranges = {
            "1": (1, 20),
            "2": (21, 40),
            "3": (41, 60),
            "4": (61, 80)
        }

        if choice not in group_ranges:
            print("Invalid choice.")
            return

        start, end = group_ranges[choice]
        print(f"\nSeats from {start} to {end}:")

        for col in range(start, end + 1):
            row_display = []
            for row in "ABC":
                seat_id = f"{col}{row}"
                status = self.seats[seat_id]
                row_display.append(f"{seat_id}:{status}")
            row_display.append("X")

            for row in "DEF":
                seat_id = f"{col}{row}"
                status = self.seats[seat_id]
                row_display.append(f"{seat_id}:{status}")

            print("  ".join(row_display))

    def book(self):
        print("Booking Options:")
        print("1. Book one single seat.")
        print("2. Book multiple seats.")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            self.book_single_seat()
        elif choice == "2":
            self.book_multiple_seats()
        else:
            print("Invalid choice.")

    def book_single_seat(self):
        print("\n--- Booking One Seat ---")
        name = input("Enter your name: ").strip()
        phone = input("Enter your phone number: ").strip()
        passport = input("Enter your passport number: ").strip()
        gender = input("Enter your gender: ").strip()
        seat = input("Enter seat to book (e.g., 10A): ").strip().upper()

        if seat not in self.seats:
            print("Invalid seat number.")
            return

        if self.seats[seat] == "F":
            self.seats[seat] = "R"
            print(f"Seat {seat} booked successfully for {name}.")
        else:
            print(f"Seat {seat} is not available. Status: {self.seats[seat]}")

    def book_multiple_seats(self):
        print("\n--- Booking Multiple Seats ---")
        try:
            count = int(input("How many seats would you like to book?: ").strip())
            if count <= 0:
                print("Seat count must be at least 1.")
                return
        except ValueError:
            print("Invalid number.")
            return

        for i in range(count):
            print(f"\n--- Booking seat {i + 1} of {count} ---")
            name = input("Enter your name: ").strip()
            phone = input("Enter your phone number: ").strip()
            passport = input("Enter your passport number: ").strip()
            gender = input("Enter your gender: ").strip()
            seat = input("Enter seat to book (e.g., 10A): ").strip().upper()

            if seat not in self.seats:
                print("Invalid seat number. Skipping...")
                continue

            if self.seats[seat] == "F":
                self.seats[seat] = "R"
                print(f"Seat {seat} booked successfully for {name}.")
            else:
                print(f"Seat {seat} is not available. Status: {self.seats[seat]}")

    def cancel(self):
        pass







customer1 = Customer()
