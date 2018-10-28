from __future__ import print_function
import time
from snake import *
import curses

MAP_HEIGHT = 100
MAP_WIDTH = 100


def print_at(x,y,text):
  output = "\033[" + str(y) + ";" + str(x) + "H" + text
  print(output, end="")

def moveNTimes(s, N):
  for i in range(N):
    time.sleep(0.1)
    print("") # I'm not sure why, but this line is needed if we want the sleep to work well
    s.move(print_at)

def getDirection(key):
  if key == "KEY_UP":
    return 'up'
  elif key == 'KEY_DOWN':
    return 'down'
  elif key == 'KEY_LEFT':
    return 'left'
  elif key == 'KEY_RIGHT':
    return 'right'
  return 'nothing'

def main(win):
  win.nodelay(True)
  key=""
  s = Snake(print_at)
  while 1:        
    try:              
      key = win.getkey()
      s.change_direction(getDirection(str(key)))
      moveNTimes(s,1)   
    except Exception as e: 
      # No input
      moveNTimes(s,1)        

curses.wrapper(main)