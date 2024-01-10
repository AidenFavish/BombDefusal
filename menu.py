import settings
import turtle as trtl

gcard = None

def menu():
    global gcard
    
    # Draws menu background
    card = settings.newTurtle()
    card.hideturtle()
    gcard = card # create global alias
    card.pensize(0)
    card.fillcolor(0.05, 0.05, 0.25)
    card.begin_fill()
    settings.drawSquare(card, -250, -250, 500, 500)
    card.end_fill()

    # Draw title
    card.goto(-185, 150)
    card.pencolor("white")
    card.write("Lazy Bomb Defusal Game", font=("Arial", 30, "bold"))

    # Draw options
    card.goto(-150, 25)
    card.pencolor("green")
    card.write("[1] EASY", font=("Arial", 20, "bold"))
    card.goto(-150, -25)
    card.pencolor("orange")
    card.write("[2] MEDIUM", font=("Arial", 20, "bold"))
    card.goto(-150, -75)
    card.pencolor("red")
    card.write("[3] HARD", font=("Arial", 20, "bold"))
    card.goto(-150, -175)
    card.pencolor("white")
    card.write("[9] QUIT", font=("Arial", 20, "bold"))

def cleanup():
    global gcard
    gcard.clear()
