import turtle

def draw_square(the_turtle):
    for i in range(4):
        the_turtle.forward(100)
        the_turtle.right(90)


def draw_art():
    # Create screen
    window = turtle.Screen()
    window.bgcolor("white")

    # Create the turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)

    # Draw lotus circle from squares
    for i in range(36):
        draw_square(brad)
        brad.right(10)

    # Exit when user closes window
    window.exitonclick()
        
    
draw_art()
