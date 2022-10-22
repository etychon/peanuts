
import random as rand

class Peanuts:
  members = []
  constraints = []
  options = {}
  draws = []

  def __init__(self):
    self.members = []

  def add_members (self, m: list):
    self.members = self.members + m
  
  def list_members (self):
    return(self.members)

  def add_constraints (self, tuples):
    self.constraints = self.constraints + tuples

  def list_constraints (self):
    return(self.constraints)

  def list_options (self):
      return(self.options)

  def addDawResult(self, a, b):
    """
    Register that "a" makes a gift to "b" and clean
    all remains options according to this draw
    """

    self.draws = self.draws + [(a, b)]

    # remove the recipient (b) from the array of options
    del self.options[b]
    
    # remove this gifter (a) from the list of options
    for z in self.options:
      if a in self.options[z]:
        self.options[z].remove(a)


  def print_draws(self):
    print("{:>12} -> {:<12}".format("FROM", "TO"))
    print("    ---------------------------")
    for a, b in self.draws:
      print("{:>12} -> {:<12}".format(a, b))

  def draw (self):
    # For each member build a list of who the member (x)
    # can receive a gift from (y)
    # x <- y
    for x in self.members:
      self.options[x] = []
      for y in self.members:
        # Can't gift to youself
        # Can't gift if in constraint list
        if ( x != y) and ((y, x) not in self.constraints):
          self.options[x] = self.options[x] + [y]

    # Let's distribute who gifts to who
    while (len(self.options)>0):

      skip = 0

      # look for single choice options
      for x in self.options:
        if len(self.options[x]) == 1:
          # add to the draws that we found one draw
          q = self.options[x][0]
          self.addDawResult(q, x)
          skip = 1
          break

      if skip == 1:
        continue

      # Pick a random receiver
      i = rand.choice(list(self.options.keys()))
      # Pick a random gifter from that receiver's list
      t = rand.choice(list(self.options[i]))
      self.addDawResult(t, i)
      # break
          
    return(self.draws)
