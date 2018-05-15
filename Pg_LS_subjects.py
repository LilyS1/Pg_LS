name = "Lily Schweinfurth"

subjects = ["English", "Math", "Science", "History", "Spanish"]

print("Hello " + name)

for i in subjects:
    print("One of my subjects is " + i)

colors = ["orange", "yellow", "brown", "red", "blue"]

for i in colors:
    if i == "brown":
        print(i + " is my least favorite color")
    elif i == "orange" or i == "yellow":
        print("One of my favorite colors is " + i)
    else:
        print("one color is " + i)



movies = []

while True:
    print("what's one of your favorite movies? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("one of youe favorite movies is " + i)
