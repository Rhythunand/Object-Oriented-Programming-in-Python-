class parrot :
  species = "Bird"

  def __init__(self,name,age):
    self.name = name
    self.age = age

blu = parrot("Blu",10)
Woo = parrot("Wlu",15)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(Woo.species))

print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} yaers old".format(Woo.name,Woo.age))