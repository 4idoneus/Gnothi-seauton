import logging
import time
logging.basicConfig(level=logging.DEBUG)

class MoneyHandler:
    CURRENCY = "₺"
    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def remaining_money(self,price):
        change = self.money_received - price
        return change

    def make_payment(self,cost,currency):
        """Represents the q_owe states"""
        self.money_received = 0  # Reset for new transaction
        logging.debug(f"\n[State: q_owe{cost}] Waiting for {cost}{currency}...")
        print("You can only give 5₺,10₺,20₺,and 50₺ banknotes.\nIf you want to exit from system please write 'c' or 'close'.")
        while self.money_received < cost:
            owed = cost - self.money_received
            logging.debug(f"\n[State: q_owe{owed}] Waiting for {owed}{currency}...")
            money_given = input(f"\nRemaining: {owed}{currency}. Insert money: ")
            if money_given in ["close","c"]:
                if self.money_received > 0:
                    print(f"Returning the given money {self.money_received}.")
                    logging.debug(f"\n[State: q_cancel] Returning {self.money_received}{currency}. Transaction Cancelled. " )
                    for n in range(self.money_received, 0, -5):
                        time.sleep(1)
                        print(f"\rRemaining change {n-5}", end="")
                    time.sleep(3)
                else:
                    logging.debug(f"\n[State: q_cancel] Transaction Cancelled. ")
                    time.sleep(3)
                return False
            if money_given in ["5", "10", "20", "50"]:
                self.money_received += int(money_given)
            else:
                print("Invalid Banknote! (Only 5, 10, 20, 50 accepted)")
        logging.debug(f"\n[State: q_dispense] Transaction Successful")
        change = self.money_received - cost
        self.profit += cost
        if change > 0:
            print(f"Your change is {change}{currency}")
            for n in range(change, 0, -5):
                time.sleep(1)
                print(f"\rRemaining change {n - 5}", end="")
            time.sleep(3)
        return True