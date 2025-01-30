class student :
  grade =  10
  name = "Penguin"

  def intro(self):
    print("Hello I am a student")

  def detail(self) :
    print("My name is", self.name)
    print("I am in Grade", self.grade)

o = student()
o.intro()
o.detail()