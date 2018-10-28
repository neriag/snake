import Queue

class Snake:
  def __init__(self, print_at):
    self.head  = {"x":20, "y":20}
    self.body = Queue.Queue()
    self.direction = {"x":1,"y":0}
    print_at(self.head["x"], self.head["y"], "X")

  def move(self, print_at):
    self.body.put(self.head)
    self.head = {"x":self.head["x"] + self.direction["x"], "y":self.head["y"] + self.direction["y"]}
    tail = self.body.get()
    print_at(tail["x"], tail["y"], " ")
    print_at(self.head["x"], self.head["y"], "X")