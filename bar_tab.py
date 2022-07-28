class Tab:
  menu = {
    'Cheese Strings':5,
    'beer': 3,
    'lemonade':90,
    'burger':18
  }

  def __init__(self):
    self.total = 0
    self.items = []
  
  def add(self, item):
    self.items.append(item)
    self.total+= self.menu[item]
  
  def print_bill(self, tax, service):
    tax = (tax/100)* self.total
    service = (service/100)* self.total
    final = self.total + tax + service
    
    for item in self.items:
      print(f'{item:20} price ${self.menu[item]}')

    print(f'{"Total:20"} ${final:.2f}')