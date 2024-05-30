class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0.0

class ATM:
    def __init__(self):
        self.users = {}  # User ID to User object mapping
        self.current_user = None

    def add_user(self, user_id, pin):
        if user_id in self.users:
            print("User ID already exists. Please choose a different ID.")
            return
        user = User(user_id, pin)
        self.users[user_id] = user
        print("User added successfully.")

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            self.current_user = self.users[user_id]
            print("Login successful. Welcome, {}!".format(user_id))
        else:
            print("Invalid user ID or PIN. Please try again.")

    def display_user_details(self):
        if self.current_user:
            print(f"User ID: {self.current_user.user_id}")
            print(f"Balance: ${self.current_user.balance:.2f}")
        else:
            print("No user is currently logged in.")

class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, transaction):
        self.history.append(transaction)

    def display_transaction_history(self):
        if not self.history:
            print("No transactions yet.")
        else:
            print("Transaction history:")
            for transaction in self.history:
                print(transaction)

class Withdraw:
    def withdraw_amount(self, amount, current_user, transaction_history):
        if amount is None or amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
            return
        if amount > current_user.balance:
            print("Insufficient funds. Please try a lower amount.")
            return
        current_user.balance -= amount
        print("Amount withdrawn: ${}".format(amount))
        transaction_history.add_transaction(f"Withdrawal: ${amount:.2f}")

class Deposit:
    def deposit_amount(self, amount, current_user):
        if amount is None or amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
            return
        current_user.balance += amount
        print("Amount deposited: ${}".format(amount))

class Transfer:
    def make_transfer(self, target_user, amount, current_user, users, transaction_history):
        if amount is None or amount <= 0:
            print("Invalid transfer amount. Please enter a positive value.")
            return
        if target_user == current_user.user_id:
            print("You cannot transfer money to yourself.")
            return
        if amount > current_user.balance:
            print("Insufficient funds. Please choose a lower transfer amount.")
            return
        if target_user not in users:
            print("User {} does not exist.".format(target_user))
            return
        target_user_obj = users[target_user]
        current_user.balance -= amount
        target_user_obj.balance += amount
        transaction_history.add_transaction("Transfer of ${} to user {}".format(amount, target_user))
        print("Amount transferred to user {}: ${}".format(target_user, amount))

def main():
    atm = ATM()
    transaction_history = TransactionHistory()
    withdraw = Withdraw()
    deposit = Deposit()
    transfer = Transfer()

    while True:
        print("\nSelect an option:")
        print("1. Add User")
        print("2. Login")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter a new user ID: ")
            pin = input("Enter a PIN: ")
            atm.add_user(user_id, pin)

        elif choice == "2":
            user_id = input("Enter user ID: ")
            pin = input("Enter PIN: ")

            atm.login(user_id, pin)

            if atm.current_user:
                while True:
                    print("\nSelect an option:")
                    print("1. Display User Details")
                    print("2. Transactions History")
                    print("3. Withdraw")
                    print("4. Deposit")
                    print("5. Transfer")
                    print("6. Logout")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        atm.display_user_details()
                    elif choice == "2":
                        transaction_history.display_transaction_history()
                    elif choice == "3":
                        amount = float(input("Enter the amount to withdraw: $"))
                        withdraw.withdraw_amount(amount, atm.current_user, transaction_history)
                    elif choice == "4":
                        amount = float(input("Enter the amount to deposit: $"))
                        deposit.deposit_amount(amount, atm.current_user)
                    elif choice == "5":
                        target_user = input("Enter the user ID to transfer: ")
                        amount = float(input("Enter the amount to transfer: $"))
                        transfer.make_transfer(target_user, amount, atm.current_user, atm.users, transaction_history)
                    elif choice == "6":
                        atm.current_user = None
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()