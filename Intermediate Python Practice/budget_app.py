class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        output = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            output += f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n"
        output += f"Total: {self.get_balance()}"
        return output
    
def create_spend_chart(categories):
    # --- STEP 1: CALCULATE PERCENTAGES ---
    grand_total = 0
    for category in categories:
        # Fixed: Changed total_spent to grand_total
        grand_total += sum(abs(item['amount']) for item in category.ledger if item['amount'] < 0)

    percentages = []
    for category in categories:
        category_spent = sum(abs(item['amount']) for item in category.ledger if item['amount'] < 0)
    
        # Fixed: Indented this entire block inside the loop
        if grand_total > 0:
            raw_percentage = (category_spent / grand_total) * 100
        else:
            raw_percentage = 0

        # Fixed: Added missing underscore in raw_percentage
        rounded_percentage = (raw_percentage // 10) * 10
        percentages.append(rounded_percentage)

    # --- STEP 2: DRAW Y-AXIS AND BARS ---
    chart = "Percentage spent by category\n"

    # Fixed: The category bar check must live INSIDE the height loop
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        # Each row ends with an extra space and a newline character
        chart += " \n"

    # --- STEP 3: DRAW HORIZONTAL FLOOR ---
    # Fixed: Moved OUTSIDE the loops so it only draws once
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # --- STEP 4: DRAW VERTICAL LABELS ---
    # Fixed: Renamed to category.name and max_len to stay clean
    max_length = max(len(category.name) for category in categories)
    padded_names = [category.name.ljust(max_length) for category in categories]

    # Fixed: Extracted out into a sequential matrix loop
    for i in range(max_length):
        chart += "    "
        for name in padded_names:
            chart += f" {name[i]} "
        chart += " \n"

    return chart.rstrip("\n")
