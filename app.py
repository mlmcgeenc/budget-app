class Category:
  name = ""
  ledger = []

  def __init__(self, name):
    self.name = name

  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance = balance + entry["amount"]
    return balance

  def check_funds(self, check):
    balance = self.get_balance()
    if balance > check:
      return True
    else:
      return False

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": (-1 * amount), "description": description})
      return True
    else:
      return False

  def transfer(self, amount, category=""):
    if self.check_funds(amount) == True:
      self.withdraw(amount, "Transfer to " + str(category))
      secondBudget.deposit(amount, "Transfer from " + str(self.name))
      return True
    else:
      return False

  def print_ledger(self):
    for entry in self.ledger:
      print(entry)

def create_spend_chart(categories):
  return "Chart not yet ready"

budget = Category("Test Budget")
secondBudget = Category("Second_Budget")
print("Budget created:")
print(budget)
print("Deposit:")
budget.deposit(100, "deposit")
budget.print_ledger()
print("Deposit - no description:")
budget.deposit(100)
budget.print_ledger()
print("Withdrawal:")
budget.withdraw(50, "withdrawal")
budget.print_ledger()
print("Withdrawal - no desc:")
budget.withdraw(50)
budget.print_ledger()
print("Transfer:")
budget.transfer(50, "Second_Budget")
budget.print_ledger()
print("Overdrawn:")
budget.withdraw(200)
budget.print_ledger()
print("Second Budget:")
secondBudget.print_ledger()