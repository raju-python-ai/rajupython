
class ATM:
    def __init__(self, name, acc_no, pin, balance=0):
        """Initialize the ATM account with user details."""
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def balance_inquiry(self, pin):
        """Check and display account balance."""
        if self.pin == pin:
            print(f"Your current balance is: ₹{self.balance}")
            self.transaction_history.append("Balance inquiry performed.")
        else:
            print("Invalid PIN!")

    def cash_withdraw(self, amount, pin):
        """Withdraw cash if sufficient balance exists."""
        if self.pin == pin:
            if amount > self.balance:
                print("Insufficient balance!")
            else:
                self.balance -= amount
                print(f"Successfully withdrawn ₹{amount}. Remaining balance: ₹{self.balance}")
                self.transaction_history.append(f"₹{amount} withdrawn.")
        else:
            print("Invalid PIN!")

    def cash_deposit(self, amount, pin):
        """Deposit cash into the account."""
        if self.pin == pin:
            self.balance += amount
            print(f"Successfully deposited ₹{amount}. New balance: ₹{self.balance}")
            self.transaction_history.append(f"₹{amount} deposited.")
        else:
            print("Invalid PIN!")

    def pin_change(self, new_pin, pin):
        """Change the PIN if the old PIN matches."""
        if self.pin == pin:
            self.pin = new_pin
            print("PIN successfully updated!")
            self.transaction_history.append("PIN changed.")
        else:
            print("Invalid PIN!")

    def view_transaction_history(self, pin):
        """Display the transaction history."""
        if self.pin == pin:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print("-", transaction)
        else:
            print("Invalid PIN!")

# Create an ATM account
user = ATM(name="Raju", acc_no=123456789, pin=2004, balance=5000)

# Main program loop
while True:
    print("\n----- ATM Menu -----")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. PIN Change")
    print("5. Transaction History")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        user_pin = int(input("Enter your PIN: "))
        user.balance_inquiry(user_pin)
    elif choice == "2":
        user_pin = int(input("Enter your PIN: "))
        amount = int(input("Enter the amount to withdraw: "))
        user.cash_withdraw(amount, user_pin)
    elif choice == "3":
        user_pin = int(input("Enter your PIN: "))
        amount = int(input("Enter the amount to deposit: "))
        user.cash_deposit(amount, user_pin)
    elif choice == "4":
        user_pin = int(input("Enter your current PIN: "))
        new_pin = int(input("Enter your new PIN: "))
        user.pin_change(new_pin, user_pin)
    elif choice == "5":
        user_pin = int(input("Enter your PIN: "))
        user.view_transaction_history(user_pin)
    elif choice == "6":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")



