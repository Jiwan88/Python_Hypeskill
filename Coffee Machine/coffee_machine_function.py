water = 400
milk = 540
coffee_beans = 120
dis_cups = 9
money = 550
want = ''


def action():
    global money, dis_cups, water, milk, coffee_beans, want

    if(want != "exit"):
        want = input("Write action (buy, fill, take, remaining, exit):\n>")

        if want == "remaining":
            print("The coffee machine has:")
            print(water, "of water")
            print(milk, "of milk")
            print(coffee_beans, "of coffee beans")
            print(dis_cups, "of disposable cups")
            print("$"+str(money), "of money")
            action()

        if want == "buy":
            buy_item = (input(
                "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n>"))
            if buy_item == "1":
                if water >= 250 and coffee_beans >= 16:
                    print("I have enough resources, making you  a coffee!")
                    water, coffee_beans = water - 250, coffee_beans - 16
                    money += 4
                    dis_cups -= 1
                    action()
                else:
                    print("sorry, not enough water!")
                    action()
            elif buy_item == "2":
                if water >= 350 and milk >= 75 and coffee_beans >= 20:
                    print("I have enough resources, making you  a coffee!")
                    water, milk, coffee_beans = water - 350, milk - 75, coffee_beans - 20
                    money += 7
                    dis_cups -= 1
                    action()
                else:
                    print("sorry, not enough water!")
                    action()
            elif buy_item == "3":
                if water >= 200 and milk >= 100 and coffee_beans >= 12:
                    print("I have enough resources, making you  a coffee!")
                    water, milk, coffee_beans = water - 200, milk - 100, coffee_beans - 12
                    money += 6
                    dis_cups -= 1
                    action()
                else:
                    print("sorry, not enough water!")
                    action()
            else:
                action()

        if want == "fill":
            water += int(input("Write how many ml of water do you want to add:\n>"))
            milk += int(input("Write how many ml of milk do you want to add:\n>"))
            coffee_beans += int(
                input("Write how many grams of coffee beans do you want to add:\n>"))
            dis_cups += int(input("Write how many of disposable cups do you want to add:\n>"))
            action()

        if want == "take":
            print("I gave you", money)
            money = 0
            action()

    else:
        exit()


action()
