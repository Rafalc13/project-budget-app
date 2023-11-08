class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({'amount': -amount, 'description': description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    return balance

  def transfer(self, amount, b_category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {b_category.category}')
      b_category.deposit(amount, f'Transfer from {self.category}')
      return True
    return False

  def check_funds(self, amount):
    return self.get_balance() >= amount

  def __str__(self):
    title = self.category.center(30, '*')
    ledg = ''
    for item in self.ledger:
      ledg += f'{item["description"][:23]:23}{item["amount"]:>7.2f}\n'
    return f'{title}\n{ledg}Total: {self.get_balance():.2f}'




def create_spend_chart(categories):
  chart = 'Percentage spent by category'
  total = 0
  spend = {}
  print(chart, total, spend)
  
  for cat in categories:
    spend[cat.category] = {}
    spend[cat.category]['amount'] = round(sum([abs(item['amount']) for item in cat.ledger if item['amount'] < 0]), 2)
    total += spend[cat.category]['amount']

  name = {k:(v['amount']/total*100) - ((v['amount']/total*100) % 10) for k,v in spend.items()}
  print(name)

  for i in range(100, -10, -10):
    chart += '\n' + str(i).rjust(3) + '| '
    for cat, pr in name.items():
      chart += 'o  ' if pr >= i else '   '
  chart += '\n    -' + '-'*3*len(name.keys())
  print(chart)

  for x in range(0, max(len(item) for item in name)):
    chart += '\n     '
    for cat in name.keys():
      try:
        chart += cat[x] + '  '
      except:
        chart += '   '
  return chart

