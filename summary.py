import turtle as trtl
import settings

card = None
diff = None

def summarize(status, difficulty, chances, timeRemaining):
    global card, diff
    diff = difficulty  #  Save global alias

    # Draws menu background
    card = settings.newTurtle()
    card.hideturtle()
    card.pensize(0)
    card.fillcolor(0.05, 0.05, 0.25)
    card.begin_fill()
    settings.drawSquare(card, -250, -250, 500, 500)
    card.end_fill()

    # Write status
    card.goto(-125, 150)
    card.color("green" if status == "DEFUSED" else "red")
    card.write(f"STATUS: {status}", font=("Arial", 25, "bold"))

    # Write difficulty
    card.goto(-100, 100)
    card.color("white")
    card.write(f"Difficulty: {difficulty}", font=("Arial", 20, "bold"))

    # Write chances left
    card.goto(-100, 50)
    card.color("white")
    card.write(f"Chances left: {chances}", font=("Arial", 20, "bold"))

    # Write difficulty
    card.goto(-100, 0)
    card.color("white")
    card.write(f"Time remaining: {timeRemaining}", font=("Arial", 20, "bold"))

    card.color("cyan")  # new color for buttons

    # Play again
    card.goto(-100, -100)
    card.write(f"[1] Play again", font=("Arial", 20, "bold"))

    # Play again
    card.goto(-100, -150)
    card.write(f"[2] Main menu", font=("Arial", 20, "bold"))

def cleanup():
    card.clear()
