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


import math
import turtle

turtle.shape("turtle")
turtle.setup(width=900, height=700)
turtle.speed(0)
turtle.bgcolor('black')
turtle.color('red')

def heart1(h):
    return 15 * math.sin(h) ** 3

def heart2(h):
    return 12 * math.cos(h) - 5 * math.cos(2 * h) - 2 * math.cos(3 * h) - math.cos(4 * h)



for i in range(600):
    x, y = heart1(i) * 20, heart2(i) * 20
    turtle.goto(x, y)

# Draw "I Love You" in the center
turtle.penup()
turtle.goto(0, -45)
turtle.pendown()
turtle.write('I Love You', align='center', font=('Arial', 50, 'bold'))

turtle.done()






