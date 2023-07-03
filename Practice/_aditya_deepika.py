import time

def display_message(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

def propose():
    display_message("Dear love [DEEPIKA, LIFELINE, SUPERGIRL, BABY, ],")
    display_message("I wanted to express my feelings to you in a unique way, so I wrote you this Python coding.")
    display_message("You are the most incredible person I've ever met, and I can't imagine my life without you.")
    display_message("From the moment we met, you captured my heart, and every day since then, my love for you has grown.")
    display_message("Will you do me the honor of becoming my partner for life?")
    display_message("My only hope is to see us married. And living a happily married life.Where we both see the ups and down of life and face it together.")
    display_message("With all my love,")
    display_message("[Yours and only ADITYA]")
    display_message("I LOVE U ENDLESSLY WILL U MARRY ME")

propose()

print('\u2764')
print('\u2764')
print('\u2764')
print('\u2764')


import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Happy Journey!")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create the turtle object
heart = turtle.Turtle()
heart.shape("turtle")
heart.color("red")
heart.speed(2)

# Move the turtle to the starting position
heart.penup()
heart.goto(0, -200)
heart.pendown()

# Draw the heart shape
heart.begin_fill()
heart.left(140)
heart.forward(224)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(224)
heart.end_fill()

# Move the turtle to the text position
heart.penup()
heart.goto(0, 0)
heart.pendown()

# Write the text message
heart.color("black")
heart.write("Happy Journey Baby i pray ur all wish come true in this trip!", align="center", font=("Arial", 10, "bold"))

# Hide the turtle
heart.hideturtle()

# Exit on click
turtle.done()

# Aditya love Deepika













