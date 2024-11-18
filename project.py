class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Hello {self.holder_name}, thank you for depositing ${amount:.2f}. Your new balance is now ${self.balance:.2f}.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Hello {self.holder_name}, you have successfully withdrawn ${amount:.2f}. Your remaining balance is now ${self.balance:.2f}.")
            else:
                print(f"Hello {self.holder_name}, insufficient funds. Your current balance is ${self.balance:.2f}. Please try a smaller amount.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def check_balance(self):
        print(f"Hello {self.holder_name}, your account balance is ${self.balance:.2f}. Thank you for banking with us!")

def main():
    print("Welcome to the Basic Banking System!")
    # Creating a sample bank account
    account = BankAccount(account_number="12345678", holder_name="Maxias", balance=1000000.0)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print(f"Goodbye, {account.holder_name}! Thank you for using the Basic Banking System. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
