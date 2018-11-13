import pyautogui as pg
import time as t
import webbrowser as wb
points = 0
"""
name = pg.prompt("Whats your name?").title()
if name == "Simon":
  pg.alert("Good, you passed " + name)
  points +=68 + 1
  wb.open("https://www.youtube.com/watch?v=fTMyjXl5ZqA")
elif name == "Jurgis":
  pg.alert ("Sceptre " + name + " = Yes.")
  points +=419 + 1
  wb.open("https://www.greenwich-post.com/wp-content/uploads/sites/21/2016/03/DanGutmanKids.jpg")
elif name == "Ryan":
  pg.alert ("All around fun guy?")
  t.sleep(2)
  wb.open("https://www.youtube.com/watch?v=g-sgw9bPV4A")
  points -=100
elif name == "Gus":
  pg.alert ("I cleen nowe.")
  wb.open("https://www.youtube.com/watch?v=g9WZrq9u3y8")
elif name == "Mr. Rohdie":
  pg.alert("Hi Mr. Rohdie")
elif name == "Mr. Rill":
  pg.alert(" Hi Mr. Rill!")
else:
  pg.alert ("Hello there "+ name)
  wb.open("https://www.youtube.com/watch?v=94rPNPMwoaE")
game = pg.prompt("what is your favorite video game?").title()
if game == "Fortnite":
  pg.alert ("DED")
  t.sleep(1)
  points +=123
  wb.open("https://www.youtube.com/watch?v=zEpB4aNHllA")
elif game == "Roblox":
  pg.alert ("oof")
elif game == "Clash of Clans":
  pg.alert("really? cmon")
elif game == "PubG":
  pg.alert ("why")
  wb.open("https://www.youtube.com/watch?v=OfNUoJCCPkQ")
  points -=3
elif game == "COD":
  pg.alert ("Great game, cant wait for Bo4")
  t.sleep(2)
  wb.open("https://www.youtube.com/watch?v=TqGj7ArNJw0")
  points +=15
elif game == "Candy Crush":
  pg.alert ("What are you, 92")
  t.sleep(.654)
  wb.open("https://www.google.com/")
  points -=92
else:
  pg.alert ("OK")
  
food = pg.prompt("food?").title()
if food == "Spaghut":
  pg.alert("yes")
  t.sleep(2)
  wb.open("https://www.youtube.com/watch?v=cE1FrqheQNI")
elif food == "Pizza with pineapple and Ketchup":
  pg.alert("thats disgusting, how do u eat " + food)
  wb.open("https://www.youtube.com/watch?v=jUy9_0M3bVk")
elif food == "Food":
  pg.alert(".....")
  wb.open("https://www.youtube.com/watch?v=duoCDRMg6t8")
elif food == "ants":
  pg.alert("ANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTSANTS")
  wb.open("https://www.youtube.com/watch?v=ny0qSMVuU6k")
elif food == "Pizza":
  pg.alert("pizza is good")
  wb.open("https://www.pizzahut.com/index.php?f=login#/pizza/create-your-own#pbTop")
elif food == "Pasta":
  pg.alert("I love pasta!")
  wb.open("https://www.foodnetwork.com/recipes/food-network-kitchen/low-cal-fettuccine-alfredo-recipe-2118317")
  points += 2.345433234432113
else:
  pg.alert("your favorite food is " + food)
sports = pg.prompt("favorite sport?").title()
if sports == "Football":
  pg.alert("Football is great")
elif sports == "Baseball":
    pg.alert("Thats a good sport")
elif sports == "Basketball":
    pg.alert("great!")
elif sports == "Hockey":
  pg.alert("oK!")
elif sports == "Fooseball":
  pg.alert("not a sport tho")
elif sports == "Ping-Pong":
  pg.alert("Thats not really a sport...")
else:
  pg.alert("Thats a good sport too!")

movies = pg.prompt("Favorite movie").title()
if "Avengers" in movie:
  character = pg.prompt("Which avenger do you like the most").title()

  if character == "Iron Man":
    pg.alert("I like Spider-Man better")
if movies == "Avengers":
  pg.alert("Did you see infinity war?")
elif movies == "Superman":
   pg.alert("they are getting worse.")
elif movies == "Justice league":
    pg.alert("That failed horribly")
elif movies == "Deadpool":
  pg.alert("such a good movie!")
elif movies == "Halloween":
  pg.alert("Great movie!")
elif movies == "Incredibles":
  pg.alert("good kids movie!")
else:
  pg.alert("Huh, havent heard of that")
pg.alert ("your points are " + str(points))
"""
ice_cream = pg.confirm ("which is your favorite","Choose one",["chocolate","vanilla","caramel"])

