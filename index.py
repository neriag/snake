from snake import *

def clear_screen():
  print(chr(27) + "[2J")

def print_at(x,y,text):
  output = "\033[" + str(x) + ";" + str(y) + "H" + text;
  print(output);

s = Snake()
clear_screen()
print(s.__dict__)
#print_at(s.head[0],s.head[1], "Hello")

