class Demo:
  name = ""
  value = ""
  def __init__(self, name):
    self.name = name
  def add_value(self, input):
    self.value = input
  def transfer_value(self, target):
    target.add_value(self.value)

itemOne = Demo("item_one")
itemTwo = Demo("item_two")
itemOne.add_value("1")
itemTwo.add_value("2")
print("Item one name and value: ", itemOne.name + ' ' + itemOne.value)
print("Item two name and value: ", itemTwo.name + ' ' + itemTwo.value)
itemTwo.transfer_value(itemOne)
print("Item one name and value: ", itemOne.name + ' ' + itemOne.value)
