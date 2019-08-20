def food():
    print("What is your favorite dish? ")
    x = input()
    if x == "hamburger" or x == "steak" or x == "pizza":
        print("You have the right taste!")
    else:
        print("I can't talk with you!")

def color():
    print("What color do you like?")
    y = input()
    if y == "green":
        print("Let's be friends!")
    else:
        print("You are a weird person!")

food()
color()
