import pyautogui as pg
import time
import webbrowser

points=0

#Question goes here
answer = pg.prompt(
"""
What is you favorite dessert of the four?

a)shave ice
b)ice cream
c)smore's
d)gelato
e)cookie dough
"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points =+ 4
elif answer == "e":
    points =+ 5


#Question goes here
answer = pg.prompt(
"""
What would you rather do on the weekend?

a)surf
b)go to a zoo/aquarium
c)rock climb
d)shop
e)go out to brunch
"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points =+ 4
elif answer == "e":
    points =+ 5

#Question goes here
answer = pg.prompt(
"""
What's your favorite of these colors?

a)orange
b)blue
c)green
d)pink
e)yellow
"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points =+ 4
elif answer == "e":
    points =+ 5

#Question goes here
answer = pg.prompt(
"""
What's your favorite holday?

a)Christmas/Hannukah/Quanza
b)Easter
c)Thanksgiving
d)Valentine's Day
e)Your Birthay
"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points =+ 4
elif answer == "e":
    points =+ 5

#Question goes here
answer = pg.prompt(
"""
What's your favorite breed of dog?

a)Chow Chow
b)Pit Bull
c)Lab
d)Poodle
e)Pug
"""
    )

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points =+ 4
elif answer == "e":
    points =+ 5
# end of survey
pg.alert ("OK, here's where you should travel to..")

if points < 8:
    pg.alert ("You should go to Honolulu, Hawaii!")
    webbrowser.open("http://media.royalcaribbean.com/content/shared_assets/images/ports/hero/HNL_01.jpg")
elif points < 13 and points >= 8:
    pg.alert("You should go to Cape Town, South Africa!")
    webbrowser.open("http://media.natgeotraveller.in/wp-content/uploads/2017/01/Niloufer-Editorial-photo.jpg")
elif points < 17 and points >= 13:
    pg.alert("You should go to Yellowstone National Park!")
    webbrowser.open("http://cdn.history.com/sites/2/2017/03/GettyImages-154931596.jpg")
elif points < 21 and points >=17:
    pg.alert ("You should go to Paris, France!")
    webbrowser.open("http://www.ladyhattan.com/wp-content/uploads/2014/03/paris-france-photograph.jpg")
elif points < 26 and points >= 21:
    pg.alert ("You should go to New York City!")
    webbrowser.open("http://blog.newyorkpass.com/wp-content/uploads/2017/11/nyc-aerial-skyline.jpg")
# A = hawaii B = Africa C = Yellowstone D = Paris E = NYC
