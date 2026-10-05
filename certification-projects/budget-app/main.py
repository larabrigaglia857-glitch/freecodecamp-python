class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        amount = -amount
        self.ledger.append({
            'amount': amount,
            'description': description
        })
        return True 


    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")

        return True

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False

        return True

    def __str__(self):
        output = f"{self.name:*^30}\n"

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            output += f"{description:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)      



def create_spend_chart(categories):
    # Calculate total amount spent
    total_spent = 0
    spent = []

    for category in categories:
        amount_spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                amount_spent += -item["amount"]

        spent.append(amount_spent)
        total_spent += amount_spent

    # Calculate percentages, rounded down to nearest 10
    percentages = []
    for amount in spent:
        percentage = int((amount / total_spent) * 100)
        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    # Build chart
    output = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        output += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                output += " o "
            else:
                output += "   "

        output += " \n"

    # Horizontal line
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        output += "     "

        for category in categories:
            if i < len(category.name):
                output += category.name[i] + "  "
            else:
                output += "   "

        output += "\n"

    return output.rstrip("\n")


