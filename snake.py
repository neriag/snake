import Queue

class Snake:
  def __init__(self, print_at):
    self.head  = {"x":20, "y":20}
    self.body = Queue.Queue()
    self.direction = {"x":1,"y":0}
    self.initialize(print_at)

  def grow(self, print_at):
    self.body.put(self.head)
    self.head = {"x":self.head["x"] + self.direction["x"], "y":self.head["y"] + self.direction["y"]}
    print_at(self.head["x"], self.head["y"], "X")
  
  def initialize(self, print_at):
    BASIC_SIZE = 10
    for i in range(BASIC_SIZE):
      self.grow(print_at)

  def change_direction(self, newDirection):
      self.direction =  {'right': {"x":1,"y":0},
                         'left':  {"x":-1,"y":0},
                         'up': {"x":0,"y":-1},
                         'down': {"x":0,"y":1}}.get(newDirection, self.direction)
        

  def move(self, print_at):
    self.body.put(self.head)
    self.head = {"x":self.head["x"] + self.direction["x"], "y":self.head["y"] + self.direction["y"]}
    tail = self.body.get()
    print_at(tail["x"], tail["y"], " ")
    print_at(self.head["x"], self.head["y"], "X")