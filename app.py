class Category:
  name = ""
  totalSpent = 0

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
      balance += entry["amount"]
      continue
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
      self.totalSpent = self.totalSpent + amount
      return True
    else:
      return False

  def transfer(self, amount, category=""):
    if self.check_funds(amount) == True:
      category.ledger.append({"amount": amount, "description": "Transfer from " + str(self.name)})
      self.withdraw(amount, "Transfer to " + category.name)
      self.totalSpent = self.totalSpent + amount
      return True
    else:
      return False

  def print_ledger(self):
    for entry in self.ledger:
      print(entry)

def create_bar(number, string):
  i = 0
  while i < number:
    string = string + 'o'
    i +=1
  return string

def create_spend_chart(*categories):
  spendingTotal = categories[0].totalSpent + categories[1].totalSpent + categories[2].totalSpent
  chartKey = ['100|', '90|', '80|', '70|', '60|', '50|', '40|', '30|', '20|', '10|', '0|']
  # str(int(categories[0].totalSpent/spendingTotal*10)).rjust(11) = the number of 'o' that should appear to represent the % of total spending
  strOneBar = ""
  strOneBarCount = int(categories[0].totalSpent/spendingTotal*10)
  stringOne = create_bar(strOneBarCount, strOneBar).rjust(11) + "_" + categories[0].name
  stringTwo = str(int(categories[1].totalSpent/spendingTotal*10)).rjust(11) + "_" + categories[1].name
  stringThree = str(int(categories[2].totalSpent/spendingTotal*10)).rjust(11) + "_" + categories[2].name
  
  strings = [stringOne, stringTwo, stringThree]
  # initialize 'lists' with chartKey as
  # the first list.
  lists = [chartKey]
  # convert each string into a list of
  # single characters and add each list 
  # to the array 'lists'
  for string in strings:
    convertedList = [char for char in string]
    lists.append(convertedList)
  # create variable 'rowLen' and find the
  # length of the longest string
  rowLen = 0
  for string in strings:
    rowLen = max(rowLen, len(string))
  # if a list is shorter than rowLen add
  # white space indexes to the end of the 
  # list so all lists are the same length
  for list in lists:
    while len(list) < rowLen:
      list.append(" ")
  # initialize the list 'outPut' and create
  # empty indexes for each printed row. This
  # requires as many indexes or 'rows' as
  # there are characters in our lists of characters
  outPut = []
  i = 0
  while i < rowLen:
    outPut.append("")
    i += 1

  j = 0
  while j < rowLen:
    if outPut[j] != None:
      for entry in lists:
        if entry[j] == "_":
          outPut[j] += "__"
        else:
          outPut[j] += entry[j].rjust(4) if entry == chartKey else entry[j][:2].rjust(2)
          continue
      j += 1
    else:
      outPut[j] += " "
  for index in outPut:
    print(index)
  for category in categories:
    print(category.get_balance())

firstBudget = Category("First Budget")
secondBudget = Category("Second Budget")
thirdBudget = Category("Third Budget")
print("Budgets created:")
firstBudget.deposit(100, "deposit")
secondBudget.deposit(100, "deposit")
thirdBudget.deposit(100, "deposit")

firstBudget.withdraw(10, "withdraw 10")
secondBudget.withdraw(20, "withdraw 20")
thirdBudget.withdraw(30, "withdraw 30")

firstBudget.withdraw(10, "withdraw 10")
secondBudget.withdraw(20, "withdraw 20")
thirdBudget.withdraw(30, "withdraw 30")
print(create_spend_chart(firstBudget, secondBudget, thirdBudget))