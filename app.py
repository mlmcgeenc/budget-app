class Category:
  name = ""
  ledger = []

  def __init__(self, name):
    self.name = name
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
  def withdraw(self, amount, description=""):
    self.ledger.append({"amount": (-1 * amount), "description": description})
  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance = balance + entry['amount']
    return balance

def create_spend_chart(categories):
  return 'Chart not yet ready'

budget = Category('My Budget')
budget.deposit(50, 'deposit')
budget.deposit(200)
budget.withdraw(50, "milk, cereal, eggs, bacon, bread")
budget.withdraw(50)
print(budget.get_balance())
print(budget.name)
print(budget.ledger[0])