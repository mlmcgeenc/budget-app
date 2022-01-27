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

firstBudget = Category("First_Budget")
secondBudget = Category("Second_Budget")
print("Budgets created:")
print("First Budget: ", firstBudget)
print("Second Budget: ", secondBudget)
print("Deposit:")
firstBudget.deposit(100, "deposit")
firstBudget.print_ledger()
print("Deposit - no description:")
firstBudget.deposit(100)
firstBudget.print_ledger()
print("Withdrawal:")
firstBudget.withdraw(50, "withdrawal")
firstBudget.print_ledger()
print("Withdrawal - no desc:")
firstBudget.withdraw(50)
firstBudget.print_ledger()
print("Transfer:")
firstBudget.transfer(50, "Second_Budget")
firstBudget.print_ledger()
print("Overdrawn:")
firstBudget.withdraw(200)
firstBudget.print_ledger()
print("Second Budget:")
secondBudget.print_ledger()