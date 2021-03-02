class Machine:

    def __init__(self, water, milk, coffee_beans, dis_cups, money):
        self.user_input = ''
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.dis_cups = dis_cups
        self.money = money

    def action(self):
        if self.user_input != "exit":
            self.user_input = input("Write action (buy, fill, take, remaining, exit):\n>")

            if self.user_input == "buy":
                Machine.buy(self)
            if self.user_input == "fill":
                Machine.fill(self)
            if self.user_input == "take":
                Machine.take(self)
            if self.user_input == "remaining":
                self.remaining()
        else:
            exit()

    def buy(self):
        buy_item = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n>"))
        if buy_item == "1":
            if self.water >= 250 and self.coffee_beans >= 16:
                print("I have enough resources, making you  a coffee!")
                self.water, self.coffee_beans = self.water - 250, self.coffee_beans - 16
                self.money += 4
                self.dis_cups -= 1
                self.action()
            else:
                print("sorry, not enough water!")
                self.action()
        elif buy_item == "2":
            if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20:
                    print("I have enough resources, making you  a coffee!")
                    self.water, self.milk, self.coffee_beans = self.water - 350, self.milk - 75, self.coffee_beans - 20
                    self.money += 7
                    self.dis_cups -= 1
                    self.action()
            else:
                print("sorry, not enough water!")
                self.action()
        elif buy_item == "3":
            if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12:
                    print("I have enough resources, making you  a coffee!")
                    self.water, self.milk, self.coffee_beans = self.water - 200, self.milk - 100, self.coffee_beans - 12
                    self.money += 6
                    self.dis_cups -= 1
                    self.action()
            else:
                print("sorry, not enough water!")
                self.action()
        else:
            self.action()
        
    
    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n>"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n>"))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n>"))
        self.dis_cups += int(input("Write how many of disposable cups do you want to add:\n>"))
        self.action()

        

    def take(self):
        print("I gave you", self.money)
        self.money = 0
        self.action()

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.dis_cups, "of disposable cups")
        print("$"+str(self.money), "of money")
        self.action()

    
machine1 = Machine(400, 540, 120, 9, 550)
machine1.action()

