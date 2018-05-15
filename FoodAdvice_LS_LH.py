#meal planner by Lindsay and Lily

import pyautogui as pg
import webbrowser

answer = pg.confirm("Would you like food?","",['yes', 'no'])

if answer == 'no':
    pg.alert("Ok, goodbye")

elif answer == 'yes':
    question2 = pg.confirm("What meal would you like to make?","", ['Breakfast', 'Lunch', 'Dinner', 'Snack'])

    if question2 == "Breakfast":
        question3 = pg.confirm("Do you have any food restrictions?","", ['No', 'Gluten-free', 'Vegetarian', 'Vegan', 'Lactose-intolerant'])

        if question3 == "No":
            webbrowser.open("https://www.foodnetwork.com/recipes/robert-irvine/french-toast-recipe-1951408")
        elif question3 == "Gluten-free":
            webbrowser.open("https://www.foodnetwork.com/recipes/a-bowl-of-gluten-free-oatmeal-recipe-2109230")
        elif question3 == "Vegetarian":
            webbrowser.open("https://www.foodnetwork.com/recipes/food-network-kitchen/pancakes-recipe-1913844")
        elif question3 == "Vegan":
            webbrowser.open("https://www.foodnetwork.com/recipes/food-network-kitchen/vegan-banana-bread-3362239")
        elif question3 == "Lactose-intolerant":
            webbrowser.open("https://www.foodnetwork.com/recipes/marcela-valladolid/avocado-toast-2684065")

    elif question2 == "Lunch":
        question3 = pg.confirm("Do you have any food restrictions?","", ['No', 'Gluten-free', 'Vegetarian', 'Vegan', 'Lactose-intolerant'])
        if question3 == "No":
            webbrowser.open
            
        elif question3 == "Gluten-free":
            webbrowser.open("

        elif question3 == "Vegetarian":
            webbrowser.open("https://www.foodnetwork.com/recipes/ina-garten/tomato-sandwich-with-basil-mayonnaise-recipe-1945384")

        elif question3 == "Vegan":
            webbrowser.open("http://ohsheglows.com/2011/10/24/black-bean-and-butternut-squash-burritos/")

        elif question3 == "Lactose-intolerant":
            webbrowser.open("
          
    elif question2 == "Dinner":
        question3 = pg.confirm("Do you have any food restrictions?","", ['No', 'Gluten-free', 'Vegetarian', 'Vegan', 'Lactose-intolerant'])
        if question3 == "No":
            webbrowser.open("

        elif question3 == "Gluten-free":
            webbrowser.open("

        elif question3 == "Vegetarian":
            webbrowser.open("

        elif question3 == "Vegan":
            webbrowser.open("

        elif question3 == "Lactose-intolerant":
            webbrowser.open("
   
    elif question2 == "Snack":
        question3 = pg.confirm("Do you have any food restrictions?","", ['No', 'Gluten-free', 'Vegetarian', 'Vegan', 'Lactose-intolerant'])
        if question3 == "No":
            webbrowser.open("

        elif question3 == "Gluten-free":
            webbrowser.open("

        elif question3 == "Vegetarian":
            webbrowser.open("

        elif question3 == "Vegan":
            webbrowser.open("

        elif question3 == "Lactose-intolerant":
            webbrowser.open("

