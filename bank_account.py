## Scott's Bank account simulator - created September, 2025
## Copyright Scott Daigger 2025


# establish account class
class Account():
    def __init__(self,balance):
        self.balance = balance

# establish checking acount
checking_account = Account(balance = 0)

# establish savings account
savings_account = Account(balance = 0)

# continue program?
continue_program = True

# amount of transaction
amount = 0

# welcome people to the game
def start_program():
    print("Welcome to the Bank Account Simulator!")
    print(" ")

# function to prompt user on what to do
def prompt():
    print("Which of the following would you like to do?")
    print("1: Check your balances")
    print("2: Deposit money")
    print("3: Withdraw money")
    print("4: Quit")
    print(" ")

# select which account
which_account = " "
account_choice = " "
def choose_account():
    global account_choice
    global which_account
    valid_input = False
    

    while valid_input == False: 
        account_choice = input("Type 1 for checking, or 2 for savings: ")
        print(" ")
        
        if account_choice == "1":
            valid_input = True
            which_account = "checking"
            print("You chose 1 for checking")
            print(" ")
        elif account_choice == "2":
            valid_input = True
            which_account = "savings"
            print("You chose 2 for savings")
            print(" ")
        else:
            print(" ")
            print("Sorry, invalid entry")
            print(" ")
    

        

# function for what do do after prompt
def execute_program():
    global selection
    global checking_account
    global savings_account
    global which_account
    global amount
    global account_choice
    valid_input = False 
    prompt()
    selection = input("Enter the number for your selection: ")
    print(" ")
    
    if selection == "1":
        print("===== BALANCES =====")
        print(" ")
        print("Your checking account balance is $" + str(checking_account.balance))
        print("Your savings account balance is $" + str(savings_account.balance))
        print(" ")
        execute_program()
    elif selection == "2":
        print("===== DEPOSITS =====")
        print(" ")
        choose_account()

        while valid_input == False:
            if which_account == "checking":
                amount = input("How much would you like to add to your checking account? Please enter a whole number without a dollar sign: ")
                print(" ")
                if amount.isdigit():
                    valid_input = True
                    checking_account.balance = checking_account.balance + int(amount)
                    print("===== CONFIRMATION =====")
                    print("Adding $" + amount + " to your account.")
                    print("Your new balance is $" + str(checking_account.balance))
                    print(" ")
                else: 
                    print("Sorry, invalid entry")
                    print(" ")
                    
            elif which_account == "savings":
                amount = input("How much would you like to add to your savings account? Please enter a whole number without a dollar sign: ")
                print(" ")
                if amount.isdigit():
                    valid_input = True
                    savings_account.balance = savings_account.balance + int(amount)
                    print("===== CONFIRMATION =====")
                    print("Adding $" + amount + " to your account.")
                    print("Your new balance is $" + str(savings_account.balance))
                    print(" ")
                else: 
                    print("Sorry, invalid entry")
                    print(" ")
        execute_program()
        
    elif selection == "3":
        print("===== WITHDRAWLS =====")
        print(" ")
        choose_account()
        sufficient_funds = False 
        valid_input = False

        while valid_input == False:   
            if which_account == "checking":
                print("Your current balance is $" + str(checking_account.balance))
                amount = input("How much would you like to withdraw from your checking account? Please enter a whole number without a dollar sign: ")
                print(" ")
                if amount.isdigit():
                    if checking_account.balance - int(amount) >= 0:
                        valid_input = True
                        checking_account.balance = checking_account.balance - int(amount)
                        print("===== CONFIRMATION =====")
                        print("Withdrawing $" + amount + " from your account.")
                        print("Your new balance is $" + str(checking_account.balance))
                        print(" ")
                    else: 
                        print("Sorry, you don't have sufficient funds to withdraw $" + amount + ". Your available funds are $" + str(checking_account.balance))
                        print(" ")
                else: 
                    print("Sorry, invalid entry")
                    print(" ")
            elif which_account == "savings":
                print("Your current balance is $" + str(savings_account.balance))
                amount = input("How much would you like to withdraw from your savings account? Please enter a whole number without a dollar sign: ")
                print(" ")
                if amount.isdigit():
                    if savings_account.balance - int(amount) >= 0:
                        valid_input = True
                        savings_account.balance = savings_account.balance - int(amount)
                        print("===== CONFIRMATION =====")
                        print("Withdrawing $" + amount + " from your account.")
                        print("Your new balance is $" + str(savings_account.balance))
                        print(" ")
                    else: 
                        print("Sorry, you don't have sufficient funds to withdraw $" + amount + ". Your available funds are $" + str(savings_account.balance))
                        print(" ")
                else: 
                    print("Sorry, invalid entry")
                    print(" ")
        execute_program()
        
    elif selection == "4":
        print("===== QUIT =====")
        print(" ")
        print("Have a great day!")
        

    else:
        selection = input("Sorry, please enter a number 1, 2, or 3 for your selection")
        print(" ")
        execute_program()       

# create functions for adding and withdrawing (check balance before, make sure there's sufficient funds), o



#actually run program
start_program()
execute_program()