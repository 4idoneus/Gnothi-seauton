class SnackBar:
    """Models the machine states: q_check and q_dispense"""
    def __init__(self, menu):
        self.menu = menu

    def report(self):
        print("\n--- STOCK REPORT ---")
        for item in self.menu.menu:
            print(f"{item.name}: {item.stock} units")

    def is_in_stock(self, snack):
        """Represents the q_check state logic"""
        if snack.stock > 0:
            return True
        else:
            return False

    def get_snack(self, snack):
        """Represents the q_dispense state logic"""
        snack.stock -= 1