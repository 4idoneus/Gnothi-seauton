from snacks import SnackMenu
from snackbar import SnackBar
from money_handler import MoneyHandler
import logging
import time

logging.basicConfig(level=logging.DEBUG)

# --- SETUP ---
my_money = MoneyHandler()
snack_menu = SnackMenu()
snack_bar = SnackBar(snack_menu)

CURRENCY = "₺"
'''The admin section is not shown in the JFLAP because its not abot transaction of our NFA. It is about maintenance '''

def admin(choice,menu):

    if choice == "report":
        my_money.report()
        snack_bar.report()
        print("_" * 50)
    elif choice == "add":
        logging.debug("Adding ingredients to machine.")
        water = int(input("How much water you are going to add? "))
        protein_bar = int(input("How much protein bar you are going to add? "))
        dried_nuts = int(input("How much dried nuts you are going to add? "))
        cola = int(input("How much cola you are going to add? "))
        menu.find_snack("Water").stock += water
        menu.find_snack("Cola").stock += cola
        menu.find_snack("Protein Bar").stock += protein_bar
        menu.find_snack("Dried Nuts").stock += dried_nuts
    else:
        logging.debug(f"Admin type command {choice} is closing machine")
        print("Shutting down system...")
        quit()
def countdown(message, seconds=5):
    """Simulates physical time delay"""
    for n in range(seconds, 0, -1):
        time.sleep(1)
        print(f"\r{message}... {n-1}", end="")

def give_snack(order):
    #  FIND ITEM
    snack = snack_menu.find_snack(order)

    logging.debug(f"\n[State: q_check{snack.name}] Checking sensors for {snack.name}...")
    if snack_bar.is_in_stock(snack):
        print(f"{snack.name} is {snack.cost}{CURRENCY}")
        answer = input("Confirm selection? Yes/y or No/n \nAnswer: ").lower()
        if answer in ["yes","y"]:
            if  my_money.make_payment(snack.cost,CURRENCY):
                logging.debug(f"\n[State: q_dispense] Transaction Successful, Giving the snack.")
                countdown("Finding the snack.")
                countdown("Taking the snack from the shelf")
                countdown("Placing the snack to the tray.")
                print("\n")
                snack_bar.get_snack(snack)
                print("Thank you for your purchase!!\n")
                time.sleep(10)
        else:
            logging.debug(f"\n[State: q_cancel] Transaction Cancelled. ")
            print("See you later")
    else:
        logging.debug(f"\n[State: q_cancel] Transaction Cancelled. ")
        print("The item you choose is not available.")

# --- STATE: q0 (Idle/Selection) ---
while True:
    print("\n"*50)
    options = snack_menu.get_items()
    print(f""" Give Snack Machine
    {"-" * 50}
    How To Use :
        1.Select the snack you want.
        2.Insert your money by type.
        3.Wait for the snack to be ready.
        4.Get your snack.
        5.Enjoy it.
    {"-" * 50}""")
    response = input(f"""What would you like?
    {options}
    Answer: """).lower()
    print("_" * 50)
    if response in ["report","off","add"]:
        admin(response,snack_menu)

    elif response in ["protein bar","water","cola","dried nuts"]:
        logging.debug(f"\n[State: q0] User Selected '{response}'")
        give_snack(response)
    else:
        print("Invalid type. Try again!")