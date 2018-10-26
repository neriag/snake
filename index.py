def clear_screen():
  print(chr(27) + "[2J")

clear_screen()
print("\033[10;10HHello")
