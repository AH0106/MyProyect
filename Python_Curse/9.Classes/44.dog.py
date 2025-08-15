class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    The __init__() method  is a special method
    that Python runs automatically whenever we create a new instance based
    on the Dog class.


    The self parameter is required in the method definition, and
    it must come first, before the other parameters. It must be included in
    the definition because when Python calls this method later (to create an
    instance of Dog), the method call will automatically pass the self argument.
    very method call associated with an instance automatically passes self,
    which is a reference to the instance itself; it gives the individual instance
    access to the attributes and methods in the class.
    When we make an instance of Dog, Python will call the __init__() method from the Dog class.

    We’ll pass Dog() a name and an age as arguments; self is passed automatically,
    so we don’t need to pass it.
  """

    def sit(self):
      """Simulate a dog sitting in response to a command."""
      print(f"{self.name} is now sitting")

    def roll_over(self):
      """Simulate rolling over in response to a command."""
      print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)

your_dog = Dog("Lucy", 9)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
