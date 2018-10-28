from __future__ import print_function
import time
from snake import *

def clear_screen():
  print(chr(27) + "[2J")

def print_at(x,y,text):
  output = "\033[" + str(y) + ";" + str(x) + "H" + text
  print(output, end="")

clear_screen()
s = Snake(print_at)
for i in range(10):
  time.sleep(1)
  print("") # I'm not sure why, but this line is needed if we want the sleep to work well
  s.move(print_at)

