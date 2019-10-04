import turtle

scn = turtle.Screen()
scn.bgcolor("light blue")

jim = turtle.Turtle()
dwight = turtle.Turtle()
mike = turtle.Turtle()

jim.penup()
jim.goto(0, 0)
jim.pendown()

jim.fillcolor("green")
jim.begin_fill()

jim.forward(700)
jim.right(90)
jim.forward(500)
jim.right(90)
jim.forward(1400)
jim.right(90)
jim.forward(500)
jim.right(90)
jim.forward(700)
jim.end_fill()

dwight.penup()
dwight.goto(350, 400)
dwight.pendown

dwight.fillcolor("yellow")
dwight.begin_fill()

dwight.circle(45)
dwight.end_fill()

mike.penup()
mike.goto(-210, 0)
mike.pendown()

mike.fillcolor("brown")
mike.begin_fill()

mike.forward(120)
mike.left(90)
mike.forward(100)
mike.left(90)
mike.forward(120)
mike.left(90)
mike.forward(100)
mike.end_fill()

mike.fillcolor("red")
mike.begin_fill()

mike.backward(100)
mike.left(90)
mike.forward(120)
mike.left(135)
mike.forward(86)
mike.left(90)
mike.forward(80)
mike.end_fill()

jim.penup()
jim.goto(10, 10)
jim.pendown()

jim.fillcolor("blue")
jim.begin_fill()

jim.forward(130)
jim.left(90)
jim.forward(75)
jim.left(90)
jim.forward(85)
jim.right(90)
jim.forward(35)
jim.left(90)
jim.forward(45)
jim.left(90)
jim.forward(110)
jim.end_fill()

jim.fillcolor("black")
jim.begin_fill()

jim.circle(10)
jim.end_fill()

jim.penup()
jim.goto(120, 10)
jim.pendown()

jim.fillcolor("black")
jim.begin_fill()

jim.circle(10)
jim.end_fill()

dwight.penup()
dwight.goto(-400, 0)
dwight.pendown()

dwight.fillcolor("brown")
dwight.begin_fill()

dwight.forward(10)
dwight.left(90)
dwight.forward(200)
dwight.left(90)
dwight.forward(10)
dwight.end_fill()
dwight.backward(10)

dwight.fillcolor("light green")
dwight.begin_fill()

dwight.circle(50)
dwight.end_fill()

turtle.exitonclick()





