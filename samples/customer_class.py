class Customer:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print_customer(self):
    print("Hello my name is " + self.name)