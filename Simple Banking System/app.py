import random
import sqlite3
import database

db_file = 'card.s3db'
global checksum
connection = database.connect()


class Bank:
    def __init__(self):
        self.card_no = None
        self.pin = None
        self.option = None
        self.system = True
        self.log_in_status = False

    def operation(self):
        while self.system:
            print("1. Create an account\n2. Log into account\n0. Exit\n")
            self.option = int(input(">"))
            if self.option == 1:
                Bank.create_acc(self)
            if self.option == 2:
                Bank.log_in(self)
            if self.option == 0:
                Bank.close(self)

    # luhn pass or fail
    def luhn(self, number):
        num_list = [int(i) for i in number[:-1]]
        for i in range(0, len(num_list), 2):
            num_list[i] = num_list[i] * 2

        for i in range(len(num_list)):
            if num_list[i] > 9:
                num_list[i] -= 9

        total_check = sum(num_list) + int(number[-1])
        if total_check % 10 == 0:
            return True

    def create_acc(self):
        num = str(400000) + str(random.randint(100_000_000, 999_999_999))
        num_list = [int(i) for i in num]
        for i in range(0, len(num_list), 2):
            num_list[i] = num_list[i] * 2

        for i in range(len(num_list)):
            if num_list[i] > 9:
                num_list[i] -= 9

        for i in range(10):
            total = sum(num_list) + i
            if total % 10 == 0:
                checksum = i
                break
            else:
                total = sum(num_list)

        self.card_no = num + str(checksum)
        self.pin = str(random.randint(1000, 9999))
        print("Your card has been created")
        print("Your card number:")
        print(self.card_no)
        print("Your card PIN:")
        print(self.pin)

        database.create_table(connection)
        database.insert_card(connection, self.card_no, self.pin)
        connection.commit()

    def log_in(self):
        card_no1 = input("Enter your card number:\n>")
        pin1 = input("Enter your PIN:\n>")
        if (card_no1, pin1) == database.log_in_db(connection, card_no1, pin1):
            print("You have successfully logged in!")
            self.log_in_status = True
            while self.log_in_status:
                self.log_in_operation(card_no1)
        else:
            print("Wrong card number or PIN!")

    def log_in_operation(self, card_no1):
        print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n")
        login_option = int(input(">"))
        connection = database.connect()
        balance = database.show_balance(connection, card_no1)
        if login_option == 1:
            balance = database.show_balance(connection, card_no1)
            print(f"Balance: {balance[0]}" )
            self.log_in_operation(card_no1)

        if login_option == 2:
            add_amount = int(input("Enter income:"))
            database.add_balance(connection, balance[0] + add_amount, card_no1)
            print("Income was added!")
            connection.commit()
            self.log_in_operation(card_no1)

        if login_option == 3:
            transfer_ac = input("Transfer\nEnter card number:\n>")
            transfer_ac_balance = database.show_balance(connection, transfer_ac)
            if transfer_ac == card_no1:
                print("You can't transfer money to the same account!")
                self.log_in_operation(card_no1)
            elif self.luhn(transfer_ac) != True:
                print("Probably you made a mistake in the card number. Please try again!")
                self.log_in_operation(card_no1)
            elif database.find_card(connection, transfer_ac) == None:
                print("Such a card does not exist.")
                self.log_in_operation(card_no1)
            else:
                transfer_amount = int(input("Enter how much you want to transfer:"))
                if balance[0] == 0 or (balance[0] - transfer_amount < 0):
                    print("Not enough money!")
                    self.log_in_operation(card_no1)
                database.add_balance(connection, transfer_ac_balance[0] + transfer_amount, transfer_ac)  # add balance in transfer account
                database.add_balance(connection, (balance[0] - transfer_amount), card_no1)  # decrease balance in main account
                connection.commit()
                print("Success!")
                self.log_in_operation(card_no1)
                connection.commit()
                
        elif login_option == 4:
            database.delete_card(connection, card_no1)
            print("The account has been closed!")
            self.log_in_status = False
            self.operation()

        elif login_option == 5:
            print("You have successfully logged out!")
            self.log_in_status = False
            self.operation()
        else:
            exit()

    def close(self):
        self.system = False


account = Bank()
account.operation()
print("Bye!")
