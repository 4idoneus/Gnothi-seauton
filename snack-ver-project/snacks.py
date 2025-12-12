class Snacks:
    def __init__(self, name, stock, cost):
        self.name = name
        self.stock = stock
        self.cost = cost

class SnackMenu:
    def __init__(self):
        # Initial Stock
        self.menu = [
            Snacks(name="Protein Bar", stock=0, cost=55),
            Snacks(name="Water", stock=10, cost=5),
            Snacks(name="Dried Nuts", stock=10, cost=30),
            Snacks(name="Cola", stock=10, cost=15),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            # Display Price for user convenience
            options += f"-- {item.name}\n    "
        return options

    def find_snack(self, order_name):
        for item in self.menu:
            if item.name.lower() == order_name.lower():
                return item
        return None