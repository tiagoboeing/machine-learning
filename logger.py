from os.path import isfile, join
from config import IS_DEBUG

if not IS_DEBUG:
  print('Running in production mode! 😊')

class Logger():
  def log(message, separator = False):
    if IS_DEBUG:
      if (message):
        print(message)
      if separator:
        print('-' * 80)