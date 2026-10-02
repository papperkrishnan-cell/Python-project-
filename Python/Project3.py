class vehicle:
  def __init__(self, company, model, color, engine, fule):
    self.company = company
    self.model = model
    self.color = color
    self.engine = engine
    self.fule = fule
  def startEnging(self):
      print("staring engine")
  def changeGear(self):
      print("staring Gear")
class car(vehicle):
  def __init__(self, company, model, color, engine, fule, bodyType):
    super().__init__(company, model, color, engine, fule)
    self.bodyType = bodyType
  def openingSunroof(self):
    print("openingSunroof")
c = car("bmw", "xs", "black", 280000, "dissel", "sdv")
print(c.color)
print(c)
print(f"Company: {c.company}, Model: {c.model}, Color: {c.color}")
