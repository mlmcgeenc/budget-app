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
  stringOne = "        ***_ String One"
  stringTwo = "   ********_ String Two"
  stringThree = "       ****_ String Three"
  
  strings = [stringOne, stringTwo, stringThree]
  lists = [chartKey]
  for string in strings:
    convertedList = [char for char in string]
    lists.append(convertedList)
  rowLen = 0
  for string in strings:
    rowLen = max(rowLen, len(string))
  for list in lists:
    while len(list) < rowLen:
      list.append(" ")
  outPut = []
  i = 0
  while i < rowLen:
    outPut.append("")
    i += 1
  j = 0
  while j < rowLen:
    if outPut[j] != None:
      for entry in lists:
        outPut[j] = outPut[j] + entry[j]
        continue
      j += 1
    else:
      outPut[j] = outPut[j] + " "
  for index in outPut:
    print(index)

firstBudget = Category("First_Budget")
secondBudget = Category("Second_Budget")
print("Budgets created:")
firstBudget.deposit(100, "deposit")
firstBudget.withdraw(15, "Spend")
firstBudget.transfer(25, secondBudget)
firstBudget.deposit(50, "deposit")
print(create_spend_chart(firstBudget, secondBudget))