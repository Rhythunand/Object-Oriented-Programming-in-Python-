class robot :
  spec = 'robot'
  def __init__(self,name,fav):
    self.name = name
    self.fav = fav

tom = robot("Tom","Football")
jerry = robot("Jerry","Cricket")

print("My name is {}. I like to play {}, I am a {}".format(tom.name,tom.fav,tom.spec))
print("My name is {}. I like to play {}, I am a {} too".format(jerry.name,jerry.fav,jerry.spec))