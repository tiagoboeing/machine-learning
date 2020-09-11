from weka import Weka

global IS_DEBUG
IS_DEBUG = True # Change to log or not in terminal

if __name__ == "__main__":
    Weka('./images').extract()
