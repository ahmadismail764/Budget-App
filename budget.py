class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, descrip=""):
        self.ledger.append({"amount": amount, "description": descrip})

    def withdraw(self, amount, descrip=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": descrip})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, another_obj):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {another_obj.category}")
            another_obj.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
            total += item["amount"]
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    spent = []
    category_names = []
    for category in categories:
        total_withdrawals = sum(
            item["amount"] for item in category.ledger if item["amount"] < 0
        )
        spent.append(total_withdrawals)
        category_names.append(category.category)
    percentages = [int((amount / sum(spent)) * 100) for amount in spent]
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    ----------\n"
    max_len = max(len(name) for name in category_names)
    for i in range(max_len):
        chart += "     "
        for name in category_names:
            chart += name[i] + "  " if i < len(name) else "   "
        chart += "\n"
    return chart
