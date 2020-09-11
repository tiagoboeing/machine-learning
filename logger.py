from os.path import isfile, join

# f = open('.config', 'r')
# f.read()

# print(f)

# if not main.IS_DEBUG:
#   print('Running in production mode! 😊')

class Logger():
  def log(message, separator = False):
    # if main.IS_DEBUG:
    if (message):
      print(message)
    if separator:
      print('-' * 80)