def clear_screen():
  print(chr(27) + "[2J")

def print_at(x,y,text):
  output = "\033[" + str(x) + ";" + str(y) + "H" + text;
  print(output);


clear_screen()
print_at(50,50, "Hello")
