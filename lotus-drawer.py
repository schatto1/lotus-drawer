import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(1)

    for i in range(4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("red")
    angie.speed(1)

    angie.circle(100)

    
window = turtle.Screen()
window.bgcolor("white")
draw_square()
draw_circle()
window.exitonclick()
