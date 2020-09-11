from os.path import isfile, join

debug = globals().get('IS_DEBUG')

if not debug:
  print('Running in production mode! 😊')

class Logger():
  def log(message, separator = False):
    if debug:
      if (message):
        print(message)
      if separator:
        print('-' * 80)