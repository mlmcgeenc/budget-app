class Category:
  name = ""

  def __init__(self, name, ledger=None, totalSpent=None):
    self.name = name
    if ledger is None:
      ledger = []
    self.ledger = ledger
    if totalSpent is None:
      totalSpent = 0
    self.totalSpent = totalSpent

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
    recieptTotal = "Total: " + "{:.2f}".format(self.get_balance())
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
  while i < (number + 1):
    string = string + 'o'
    i +=1
  return string

def create_spend_chart(categories):
  spendingTotal = 0
  chartKey = ['100| ', '90| ', '80| ', '70| ', '60| ', '50| ', '40| ', '30| ', '20| ', '10| ', '0| ', '-']

  for category in categories:
    spendingTotal = spendingTotal + category.totalSpent

  strings = []
  for category in categories:
    categoryBar = ""
    categoryBarCount = int(int(category.totalSpent)/spendingTotal*10)
    categoryString = create_bar(categoryBarCount, categoryBar).rjust(11) + "-" + category.name
    strings.append(categoryString)
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
        if entry[j] == "-":
          outPut[j] += "    -" if entry == chartKey else "---"
        else:
          outPut[j] += entry[j].rjust(5) if entry == chartKey else entry[j][:3].ljust(3)
          continue
      j += 1
    else:
      outPut[j] += " "
  chart = "\n".join(outPut)
  finalString = 'Percentage spent by category' + "\n" + chart
  
  return finalString

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

#print(food)
#print(clothing)
#print(auto)

print(create_spend_chart([food, clothing, auto]))
#create_spend_chart([food, clothing, auto])