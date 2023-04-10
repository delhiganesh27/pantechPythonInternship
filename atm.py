import random


class atm:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.remaining_balance = 1000

    def otp(self):
        otp = random.randint(100000, 999999)
        print(f"Your otp is {otp}")
        confirm_otp = int(input("Enter your otp"))
        if (confirm_otp == otp):
            return True
        else:
            return False

    def balance(self):
        if self.otp():
            print(f"Your Balance is : Rs {self.remaining_balance}")
        else:
            print("Invalide otp")

    def deposit(self):
        amount = int(
            input("Enter the amount to be deposited to your account: "))
        if self.otp():
            self.remaining_balance += amount
            print(f"Current Balance:{self.remaining_balance}")
        else:
            print("Invalid otp")

    def withdrawal(self):
        amount = int(
            input("Enter the amount to be withdrawn from your account: "))
        if self.otp():
            self.remaining_balance -= amount
            print(f"Remaining Balance:{self.remaining_balance}")
        else:
            print("Invalid otp")

    def operation(self):
        while (1):
            print("\t1:Balance Enquiry\n\t2:Deposit\n\t3:Withdrawal\n\t4:Exit")
            option = int(input("Select the Operations you want:"))
            if option == 1:
                self.balance()
                continue
            elif option == 2:
                self.deposit()
                continue
            elif option == 3:
                self.withdrawal()
                continue
            elif option == 4:
                print("Thank you for using our service!!!")
                break
            else:
                print("Invalid option!!!Please Enter a valid option!!!")


username = input("Enter the Username:")
password = input("Enter your password")
user1 = atm(username, password)
user1.operation()
