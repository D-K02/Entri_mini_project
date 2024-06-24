import re


class Account:
    def __init__(self, account_no, account_hold, initial_bal, custom_id, login_pas, transaction_password):
        self.__account_number__ = account_no
        self.account_holder = account_hold
        self.balance = float(initial_bal)
        self.__customer_id__ = custom_id
        self.login_password = login_pas
        self.transaction_password = transaction_password

    # login method for All operations after logging in successfully.
    def login(self, user_id, login_passw):
        if (self.__customer_id__ == user_id) & (self.login_password == login_passw):
            while True:
                try:
                    opti = int(input(
                        "Enter 1-Deposits, 2-Withdrawal, 3-Change Password, 4-View Balance, Any other number-Logout"))
                    if opti == 1:
                        amount = float(input("Enter The amount you want to Deposit:"))
                        self.deposit(amount)
                    elif opti == 2:
                        try:
                            amount = float(input("Enter the amount you want to withdraw:"))
                        except:
                            print(" Enter a valid number")
                            self.login(user_id,login_passw)
                        if amount <= 0:
                            print("Enter valid amount")
                            self.login(user_id, login_passw)
                        try:
                            transaction_pass = int(input("Enter the four digit transaction password:"))
                            if transaction_pass != self.transaction_password:
                                print("Invalid transaction password")
                                # self.login(user_id, login_passw)
                            else:
                                self.withdraw(amount)
                        except:
                            print("Invalid Transaction password ")

                    elif opti == 3:
                        psw = int(input("Enter 1- change Login Password, 2 - change Transaction Password :"))
                        if psw == 1:
                            self.login_pass()
                            break
                        elif psw == 2:
                            self.transaction_pass()
                    elif opti == 4:
                        print(f"Your Balance is {self.balance}")
                    else:
                        print("Logging out....")
                        break
                except TypeError:
                    print("Please enter valid response ")
                except ValueError:
                    print("Please Enter Valid Response ")
        else:
            print("Invalid password.\n Please login again")

    def validate_password(self, password):
        pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
        match = re.match(pattern, password)
        return bool(match)

    # login_pass method for changing login password after logging in successfully
    def login_pass(self):
        try:

            current_password = input("Enter Current login password:")
            if self.login_password == current_password:
                print("The password must be at least eight characters long.")
                print("The password must contain at least one uppercase letter.")
                print("The password must contain at least one lowercase letter.")
                print("The password must contain at least one digit.")
                new_password = input("Enter New password")
                if current_password == new_password:
                    print("Current password and new password cannot be the same")
                else:
                    valid = self.validate_password(new_password)
                    if valid:
                        self.login_password = new_password
                        print("Login Password changed successfully")
                    else:
                        print("Invalid password format")
                        opt2 = int(input("Enter 1 - Try again, Press Any other key - Go back"))
                        if opt2 == 1:
                            self.login_pass()
            else:
                print("Invalid password")
        except:
            print('Unknown Error Occurred. \n Please login again')

    # transaction_pass method for changing transaction password after logging in successfully
    def transaction_pass(self):
        try:
            current_tran = int(input("Enter Current transaction Password:"))
        except:
            print("invalid transaction password type.")
        if current_tran != self.transaction_password:
            print("Invalid transaction password")
            try:
                opt3 = int(input("Enter 1 - Try again, 2 - Go back"))
                if opt3 == 1:
                    self.transaction_pass()
            except:
                print("Type error: please enter valid response")
        else:
            try:
                new = int(input("enter new four digit transaction password:"))
                if new == current_tran:
                    print("Current transaction password and new transaction password cannot be the same.")
                else:
                    self.transaction_password = new
                    print("Transaction Password changed successfully")
            except TypeError:
                print("Invalid transaction password format.")

    def deposit(self, amount):
        try:
            if amount <= 0:
                print("Enter valid amount")
            else:
                self.balance = self.balance + amount
                print(f"Your balance is {self.balance}")
        except:
            print("Enter a positive integer")

    def withdraw(self, amount):
        try:
            if amount <= 0:
                print("Enter valid amount")
            else:
                if self.balance < amount:
                    print("Insufficient Balance in Account")
                else:
                    self.balance = self.balance - amount
                    print(f"Your balance is {self.balance}")
        except TypeError:
            print("Enter a positive integer")


r1 = Account(1969010006583, "Jane Doe", 12000, "B54321", "@Jane123", 1234)
print("Welcome to ABC Bank\n")
while True:

    try:
        opt = int(input("Enter 1 - Login, 2 - Forgot Password, 3 - exit"))
        if opt == 1:
            customer_id = input("Enter Customer ID:")
            if r1.__customer_id__ != customer_id:
                print("Invalid Customer ID")
            else:
                login_password = input("Enter Login Password:")
                if login_password != r1.login_password:
                    print("Invalid login password")
                else:
                    r1.login(customer_id, login_password)
        elif opt == 2:
            customer_id = input("Enter Customer ID:")
            if customer_id != r1.__customer_id__:
                print("Invalid Customer Id")
            else:
                account_num = int(input("Enter Account number:"))
                if r1.__account_number__ != account_num:
                    print("invalid account number.")
                else:
                    print("The password must be at least eight characters long.")
                    print("The password must contain at least one uppercase letter.")
                    print("The password must contain at least one lowercase letter.")
                    print("The password must contain at least one digit.")
                    new_pass: str = input("Enter New password")
                    validate = r1.validate_password(new_pass)
                    if validate:
                        r1.login_password = new_pass
                    else:
                        print("Invalid password format")

        elif opt == 3:
            break
        else:
            print("enter valid response.")
    except:
        continue
