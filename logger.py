class Logger():  
  def log(self, message):
    print('-' * 80)
    if (message):
      print(f'{message}')