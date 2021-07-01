# Created by Thijs van Driel 
# Created on 17/06/21
# The purpose of this code is to ask the user which item they would like to purchase at the canteen and give them the corresponding food item

# Version 1
# Sequence 1
# By Thijs van Driel
# Purpose: This sequence asks the user for thier name and if they would like to see the menu. The user also chooses what they would like to purchase in this sequence.
import time
print("Welcome to the Fraser High School canteen") 
time.sleep(1.5) 
print("What is your name") 
n = input ( )
print("Kia Ora " + n)
time.sleep(1.5) 
print("would you like to see our menu?")
ans = input()
if ans.lower() == 'yes' or ans.lower() == "y" : 
  print("We sell pies and burgers at the Fraser High canteen!") 
else: 
    print("Have a nice day, see you next time!")  
    exit()
buy = input ("Would you like a pie for $4.50, or a burger for $7.89, " + n + "?"'\n')
time.sleep(1.5) 

# Sequence 2 
# By Thijs van Driel
# Purpose: If the user chooses the burger in the previous sequence then this sequence will present the user with a confirmation of purchase and an emoji of the burger
if buy.lower() == 'burger': 
  print("Thats great, I love burgers") 
  time.sleep(1.5) 
  print("The burger will be he ready in 5 seconds") 
  time.sleep(5)  
  print("🍔")  
  time.sleep(1.5) 
  print("Thanks for purchasing this item")


# Sequence 3 
# By Thijs van Driel
# Purpose: If the user chooses the pie in sequence 1 then this sequence will present the user with a confirmation of purchase and an emoji of the pie
elif buy.lower() == 'pie':
  print("Pies are my favourite") 
  time.sleep(1.5) 
  print("The pie will be he ready in 5 seconds") 
  time.sleep(5) 
  print("Here is a fresh hot mince pie") 
  print("🥧") 
  time.sleep(1.5)
  print("Thanks for purchasing this item")

  

# Sequence 4 
# By Thijs van Driel 
# Purpose: To say goodbye to the user if they don't want to purchase a pie or a burger
else: 
  print("Sorry, we only sell burgers and pies, see you next time!")
 

