class Category:
  ledger = [1, 2, 3, 4, 5]

  def deposit(self, value):
    self.ledger.append(value)




def create_spend_chart(categories):
  return 'Chart not yet ready'

budget = Category()
budget.deposit(6)
print(budget.ledger)