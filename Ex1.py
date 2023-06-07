def enter_sum():
    while (True):
        res = input(
            "Enter your sum (must be a multiple of 50, enter 0 to exit), $: ")
        try:
            sum = int(res)
            if (sum < 0):
                print("Sum must be positive!")
            elif (sum % 50 != 0):
                print("Sum must be a multiple of 50!")
            else:
                return sum
        except ValueError:
            print("That's not a number!")


def enter_menu():
    while (True):
        res = input()
        try:
            num = int(res)
            if (num <= 0 or num > 3):
                print("Incorrect enter!")
            else:
                return num
        except ValueError:
            print("That's not a number!")


def comission(sum):
    if sum == 0:
        return 0
    comis = sum / 100 * 1.5
    if comis < 30:
        comis = 30
    elif comis > 600:
        comis = 600
    return comis


def withdraw(balance):
    while (True):
        print("Attention! Comission will be 1.5%( min-30$, max-600$)!")
        sum = enter_sum()
        if sum <= balance or sum == 0:
            break
        else:
            print("You don't have enough money!")
    comis = round(comission(sum), 2)
    print("Your cash:", sum, "$")
    print("Your comission:", comis, "$")
    return (balance-sum-comis)


balance = 0
count = 0
while (True):
    balance = round(balance, 2)
    if balance > 5000000:
        tax = round((balance*0.1), 2)
        print("Your wealth tax is", tax, "$")
        balance = round(balance-tax, 2)
    print("-------------------------------\nYour balance:", balance, "$")
    print("Enter 1 to deposit money,\nEnter 2 to withdraw money,\nEnter 3 to exit:")
    menu = enter_menu()
    match menu:
        case 1:
            balance += enter_sum()
        case 2:
            balance = withdraw(balance)
        case 3:
            print("Application closed")
            break
    count += 1
    if count == 3:
        count = 0
        if balance > 0:
            bonus = round((balance/100*3), 2)
            print("This is your third operation! You get bonus:", bonus, "$")
            balance += bonus
            
