# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"


##  Make sure to answer the following prompts about your coding experience:

## 1. How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

# Encapsulation. Max_speed, condition and price are encapsulated within the class. Repair () is then used to modify the state. Inheritance: AnakinsPod and SebulbasPod inherit from the Podracer class. Abstraction: The class contains the code needed for the other podracers to inherit. Polymorphism: I don't see any polymorphism here but it can be used. 




## 2. Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

# No, OOP makes the integration of new podracers streamlined. All I have to do is have the new podracers inherit the class and that's that!

## 3. How in particular did Object Oriented Programming assist in the solving of this problem?

# The structure used in the class provided the framework for the other podracers. The interactions seen using repair () can be modified, making for a quick and easy fix when certain podracers need editing. This approach makes for the generation of new objects easy and fast. 


