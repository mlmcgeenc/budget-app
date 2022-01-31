class Category:
  name = ""

  def __init__(self, name, ledger=None):
    self.name = name
    if ledger is None:
      ledger = []
    self.ledger = ledger

  def __repr__(self):
    endCap = '*'
    titleString = str(endCap) + self.name + str(endCap)
    lineItems = []
  
    while len(titleString) < 30:
      endCap = endCap + '*' 
      titleString = str(endCap) + self.name + str(endCap)
    for line in self.ledger:
      firstHalf = line["description"][:23] if len(line["description"]) > 23 else line["description"]
      secondHalf = "{:.2f}".format(line["amount"]).rjust(30 - len(firstHalf))
      lineItems.append(firstHalf + secondHalf)
    recieptBody = ("\n".join(lineItems))
    recieptTotal = "Total: " + "{:.2f}".format(self.get_balance()) + "\n"
    reciept = titleString + "\n" + recieptBody + "\n" + recieptTotal
    return reciept

  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance = balance + entry["amount"]
    return balance

  def check_funds(self, check):
    balance = self.get_balance()
    if balance >= check:
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
      category.ledger.append({"amount": amount, "description": "Transfer from " + str(self.name)})
      self.withdraw(amount, "Transfer to " + category.name)
      return True
    else:
      return False

  def print_ledger(self):
    for entry in self.ledger:
      print(entry)

def create_spend_chart(*categories):
  chartKey = ['100|', '90|', '80|', '70|', '60|', '50|', '40|', '30|', '20|', '10|', '0|']
  rowTwo = "        ***_ String One"
  rowThree = "   ********_ String Two"
  rowFour = "       ****_ String Three"
  #rows = [chartKey, rowTwo, rowThree, rowFour]
  s = [chartKey, rowTwo, rowThree, rowFour]
  #x = []
  row = 0
  for i in s:
    row = max(row, len(i))
  col = len(s)
  ans = ["" for i in range(row)]
  j = 0
  for i in range(col):
      j = 0
      while j < len(s[i]):
        #print(j, i)
        while i - len(ans[j]) >= 1:
            ans[j] += " "
        ans[j] += s[i][j]
        j += 1
  for word in ans:
    print(word)
  #for row in rows:
  #  for element in row:
  #    printKey += element.rjust(4) + "\n"
  #  print(printKey)

firstBudget = Category("First_Budget")
secondBudget = Category("Second_Budget")
print("Budgets created:")
firstBudget.deposit(100, "deposit")
firstBudget.withdraw(15, "Spend")
firstBudget.transfer(25, secondBudget)
firstBudget.deposit(50, "deposit")
print(create_spend_chart(firstBudget, secondBudget))