import random


class Atm:

    def __init__(self, username, account_no, password, balance=0):
        self.username = username
        self.password = password
        self.accountNo = account_no
        self.remaining_balance = balance

    def otp(self):
        otp = random.randint(100000, 999999)
        print(f"Your otp is {otp}")
        confirm_otp = int(input("Enter your otp"))
        if (confirm_otp == otp):
            return True
        else:
            return False

    def info(self):
        if self.otp():
            print(
                f'\tUsername : {self.username}\n\tAccount Number :{self.accountNo}\n\tBalance :{self.remaining_balance}\n\t', "-"*10)
        else:
            print("Invalid otp!!!Try Again!!!\n\t", "-"*10)

    def balance(self):
        if self.otp():
            print(f"Your Balance is : Rs {self.remaining_balance}\n\t", "-"*10)
        else:
            print("Invalid otp!!!Try Again!!!\n\t", "-"*10)

    def deposit(self):
        amount = int(
            input("Enter the amount to be deposited to your account: "))
        if self.otp():
            self.remaining_balance += amount
            print(f"Current Balance:{self.remaining_balance}\n\t", "-"*10)
        else:
            print("Invalid otp!!!Try Again!!!\n\t", "-"*10)

    def withdrawal(self):
        amount = int(
            input("Enter the amount to be withdrawn from your account: "))
        if self.otp():
            if amount < self.remaining_balance:
                self.remaining_balance -= amount
                print(
                    f"Withdrawn successfully!!!\nRemaining Balance:{self.remaining_balance}\n\t", "-"*10)
            else:
                print("Your balance is insufficient!!!Try Again!!!\n\t", "-"*10)
        else:
            print("Invalid otp!!!Try Again!!!\n\t", "-"*10)

    def operation(self):
        loop = True
        while loop:
            print(
                "\t1:Account Details\n\t2.Balance Enquiry\n\t3:Deposit\n\t4:Withdrawal\n\t5:Exit")
            option = int(input("Select the Operations you want:"))
            if option == 1:
                self.info()

            elif option == 2:
                self.balance()

            elif option == 3:
                self.deposit()
            elif option == 4:
                self.withdrawal()
            elif option == 5:
                print("Thank you for using our service!!!")
                print("-"*40)
                loop = False
            else:
                print("Invalid option!!!Please Enter a valid option!!!\n\t")


user = Atm("Delhi Ganesh V".upper(), 887079286, "kumar123", 1000)

while True:
    print("-"*40)
    username = input("Enter the Username:").upper()
    password = input("Enter your password")
    if username == user.username and password == user.password:
        user.operation()
    else:
        print("Username and password are incorrect!!!Try again!!!")

        continue
