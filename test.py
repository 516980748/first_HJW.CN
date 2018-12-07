

print("Hello world!")

print("\n")
for i in range(20):
    print("**", end="")
print("\n")


import math


def math_test():
    a = math.pi
    print("a =", a)

    r = 3

    a = 1 / 3

    b = math.sqrt((math.acos(a) ** 2 + math.asin(a) ** 2) * r)

    print("b =", b)

    for a in range(5):
        print("a =", a)

    for b in range(3, 10):
        print("b =", b)


# math_test()


print("\n")
for i in range(20):
    print("**", end="")
print("\n")


def test_12():
    for a in range(5):

        print("a = ", a)


# test_12()


def test_13():
    for a in range(3, 10):

        print("a = ", a)


# test_13()


def test_14():
    for a in range(4, 13, 3):

        print("a = ", a)


# test_14()

def test_15():
    for a in range(15, 5, -2):

        print("a = ", a)


# test_15()

def test_16():
    for a in range(5, 3):

        print("a = ", a)


# test_16()


def test_17():
    for i in range(1, 11):
        print(i * i)


# test_17()

def test_18():
    for i in [1, 3, 5, 7, 9]:
        print(i, ":", i**3)
    print(i)


# test_18()


def test_19():
    x = 2
    y = 10
    for i in range(0, y, x):
        print(i, end=" ")
        print(x + y)
    print("done")


# test_19()


def test_20():
    ans = 0
    for i in range(1, 11):
        ans = ans + i * i
        print(i)
    print(ans)
    print("done")


# test_20()


def test_21():
    a = round(314.15926, -1)

    print(a)


# test_21()

import math


def test_22():
    r = float(input("Input your radius of choisses: "))
    V = 4 / 3 * math.pi * r ** 3
    A = 4 * math.pi * r * r

    print("The volume of the ball is: ", V, "and the area of the ball is:", A,)


# test_22()


import math


def pizza_pice():
    p_a = float(input("Input your Pizza's price per square inch:"))
    p_r = float(input("Input your Pizza's radius:"))

    A = math.pi * p_r * p_r

    print("Your Pizza's price is ", A)


# pizza_pice()


def och_mol():
    print("Input the number of oxygens, hydrogen atoms, and carbon atoms in each molecule :", end=" ")
    o, h, c = map(int, input().split())
    mol_ohc = o * 15.994 + h * 1.0794 + c * 12.0107

    print("The atoms is : O%sH%sC%d" % (o, h, c))
    print("The mols of atoms: ", mol_ohc)


# och_mol()

def inch_distance():
    time_d = float(input(
        "Time difference between lightning and thunder input (secend) :"))
    distance_thunder = time_d * 1100
    distance_mile = distance_thunder // 5280
    distance_foot = distance_thunder - 5280 * distance_mile

    print("The distance to strike is %d mile %d foot ." %
          (distance_mile, distance_foot))


# inch_distance()


def cost_coffee():
    pound = float(input("Total coffee weight(pound) : "))
    order = int(input("Total coffee order : "))
    order_pound = float(input("Weitht of each order(pound) : "))

    cost_coffee = pound * 10.5 + order * (order_pound * 0.86 + 1.5)

    print("Total of cost ", cost_coffee)


# cost_coffee()

def slope_math():
    x_1, y_1 = map(float, input("Input coordinates 1 : ").split())
    x_2, y_2 = map(float, input("Input coordinates 2 : ").split())
    slope = (y_2 - y_1) / (x_2 - x_1)

    print("The slope of two coordinates is :", slope)


# slope_math()

import math


def distance_math():
    x_1, y_1 = map(float, input("Input coordinates 1 : ").split())
    x_2, y_2 = map(float, input("Input coordinates 2 : ").split())
    distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

    print("The distance od two coordinates is :", distance)


# distance_math()


def epact_C():
    year = int(input("Input your years:"))
    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30

    print("The value of the leap surplus:", epact)


# epact_C()


import math


def triangle_area():
    a, b, c = map(float, input(
        "Input the three sides lenth of triangle :").split())
    s = (a + b + c) / 2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The triangle's area is :", A)


# triangle_area()


import math


def heigth_ladder():
    heigth, degrees = map(float, input(
        "Input your ladder's heigth and the angle of wall and ladder(The unit of angle is degree) : ").split())
    radians = math.pi / 180 * degrees
    length = heigth / math.sin(radians)

    print("The leagth of the ladder is :", length)


# heigth_ladder()


def n_value():
    n = int(input("Input the value of n :"))
    v = 0
    c = range(0, n, 1)
    for i in c:
        v = v + i

    print("The  gross value is: ", v)


# n_value()


def nnn_value():
    n = int(input("Input the value of n :"))
    v = 0
    c = range(0, n, 1)
    for i in c:
        v = v + i**3

    print("The  gross value is: ", v)


# nnn_value()


def value_input():
    input_x = list(map(float, input("Input your number: ").split()))
    v_i = 0
    for i in input_x:
        v_i = v_i + i

    print("The gross value is :", v_i)


# value_input()

def fbnqs():
    n = int(input("Input your number:"))
    fbnqs_x = 0
    fbnqs_y = 1
    list_s = []
    for i in range(n + 1):
        list_s.append(fbnqs_y)
        print(fbnqs_y)
        fbnqs_x, fbnqs_y = fbnqs_y, fbnqs_x + fbnqs_y

    print("The fbnqs n is :", list_s[n])


# fbnqs()

from graphics import *


def win_test():
    # Open a graphics windows
    win = GraphWin('Shapes')
    # Draw a red circle centered at point (100, 100) with radius 30
    center = Point(100, 100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)
    # Put a textual label n the center of the circle
    label = Text(center, "Red Circle")
    label.draw(win)
    # Draw a square using a Rectangle object
    rect = Rectangle(Point(30, 30), Point(70, 70))
    rect.draw(win)
    # Draw a line segment using a Line object
    line = Line(Point(20, 30), Point(180, 165))
    line.draw(win)
    # Draw an oval using the Oval object
    oval = Oval(Point(20, 120), Point(180, 199))
    oval.draw(win)


# win_test()

from graphics import *


def sweetsmile():
    win = GraphWin()
    center = Point(90, 55)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)
    # Incorrect way to create two circle.
    leftEye = Circle(Point(80, 50), 5)
    leftEye.setFill('yellow')
    leftEye.setOutline('red')
    # rightEye = Circle(Point(100, 50), 5)
    # rightEye.setFill('yellow')
    # rightEye.setOutline('red')
    rightEye = leftEye.clone()
    rightEye.move(20, 0)
    leftEye.draw(win)
    rightEye.draw(win)

    # rightEye = leftEye
    # rightEye.move(20, 0)


# sweetsmile()


# futval_graph.py

from graphics import *


def futval_graph():

    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)

    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("red")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        # calculate vale for the next year
        principal = principal * (1 + apr)
        # Draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill("yellow")
        bar.setWidth(2)
        bar.draw(win)
    input("Pass <Enter> to quit")
    win.close()


# futval_graph()


def test_graph_1():
        # create a default 200x200 windows
    win = GraphWin("Tic-Tac-Toe", 1366, 768)

    # set coordinates to go from (0,0) in the lower left
    #   to (3,3) in the upper right
    win.setCoords(0.0, 0.0, 3.0, 3.0)

    # draw vertical lines
    Line(Point(1, 0), Point(1, 3)).draw(win)
    Line(Point(2, 0), Point(2, 3)).draw(win)

    # Draw horizontal lines
    Line(Point(0, 1), Point(3, 1)).draw(win)
    Line(Point(0, 2), Point(3, 2)).draw(win)

    input("Pass <Enter> to quit.")

# test_graph_1()


def test_graph_2():
        # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        # calculate vale for the next year
        principal = principal * (1 + apr)
        # Draw bar for this value
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Pass <Enter> to quit.")
    win.close()


# test_graph_2()


from graphics import *


def test_click():
        # click.py
    win = GraphWin("Click Me!!")
    for i in range(10):
        p = win.getMouse()
        print("You click at: ", p.getX(), p.getY())

    input("Pass <Enter> to quit.")
    win.close()


# test_click()


# triangle.pyw
from graphics import *


def triangle_main():
    win = GraphWin("Draw a Triangle.", 640, 480)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points.")
    message.draw(win)

    # Get and draw three vertices of trangle.
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()


# triangle_main()


# clickntype.py

def clickntype():
    win = GraphWin("Click and Type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)

#    text = input("Pass <Enter> to quit.")
#    text.draw(win)
#    win.close()


# clickntype()


# covert_gui.py
# Program to covert Celsius to Fahrenheit using a simple graphical interface.

from graphics import *


def covert_gui():
    win = GraphWin("Celsius Temperature: ", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(1, 3), "Celsius Temperature: ").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature: ").draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25, 1), "")
    outputText.draw(win)
    button = Text(Point(1.5, 2.0), "Covert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    # wait for a mouse click
    win.getMouse()

    # covert input
    celsius = float(inputText.getText())
    fahrenheit = 9.0 / 5.0 * celsius + 32

    # display output and change button
    outputText.setText(round(fahrenheit, 2))
    button.setText("Quit")

    # wait for click and then quit
    win.getMouse()
    win.close()


# covert_gui()

from graphics import *


def win_circle():
    win = GraphWin("Hello World", 640, 480)
    shape = Circle(Point(50, 50), 20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
    win.close()


# win_circle()


def win_rectangle():
    win = GraphWin("Hello World", 640, 480)
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        shapeCopy = shape.clone()
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shapeCopy.move(dx, dy)
        shapeCopy.draw(win)
    Text(Point(320, 240), "Click angin to quit.").draw(win)
    win.getMouse()

    win.close()


# win_rectangle()


def bull_win():
    win = GraphWin("Bull", 640, 480)
    bull_1 = Circle(Point(320, 240), 30)
    bull_1.setFill("yellow")
    bull_1.setOutline("yellow")
    bull_2 = Circle(Point(320, 240), 60)
    bull_2.setFill("red")
    bull_2.setOutline("red")
    bull_3 = Circle(Point(320, 240), 90)
    bull_3.setFill("blue")
    bull_3.setOutline("blue")
    bull_4 = Circle(Point(320, 240), 120)
    bull_4.setFill("black")
    bull_4.setOutline("black")
    bull_5 = Circle(Point(320, 240), 150)
    bull_5.setFill("white")
    # bull_5.setOutline("white")

    bull_5.draw(win)
    bull_4.draw(win)
    bull_3.draw(win)
    bull_2.draw(win)
    bull_1.draw(win)
    # bull_6.draw(win)

    Text(Point(320, 460), "Click angin to quit.").draw(win)
    win.getMouse()


# bull_win()


from graphics import *


def sweet_face():
    win = GraphWin("sweet face", 640, 480)

    h1 = win.getMouse()
    h2 = win.getMouse()
    head = Oval(h1, h2)
    head.setFill("yellow")
    head.setOutline("yellow")
    head.draw(win)

    e1 = win.getMouse()
    e2 = win.getMouse()
    leftEye = Oval(e1, e2)
    leftEye.setFill("red")
    leftEye.setOutline("red")
    leftEye.draw(win)

    rightEye = leftEye.clone()
    p = win.getMouse()
    c = leftEye.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    rightEye.move(dx, dy)
    rightEye.draw(win)

    m1 = win.getMouse()
    m2 = win.getMouse()
    mouth = Oval(m1, m2)
    mouth.setOutline("red3")
    mouth.setFill("red3")
    mouth.draw(win)

    Text(Point(320, 460), "Click angin to quit.").draw(win)
    win.getMouse()


# sweet_face()


def tree_win():
    win = GraphWin("Christmes tree and snowman", 640, 480)
    CT1 = win.getMouse()
    CT2 = win.getMouse()
    CT3 = win.getMouse()
    ChristmesTree = Polygon(CT1, CT2, CT3)
    ChristmesTree.setFill("green")
    ChristmesTree.setOutline("green")
    ChristmesTree.draw(win)

    CT13 = win.getMouse()
    CT23 = win.getMouse()
    CT33 = win.getMouse()
    ChristmesTreeCopy1 = Polygon(CT13, CT23, CT33)
    ChristmesTreeCopy1.setFill("green")
    ChristmesTreeCopy1.setFill("green")
    ChristmesTreeCopy1.setOutline("green")
    ChristmesTreeCopy1.draw(win)

    CT6 = win.getMouse()
    CT7 = win.getMouse()
    CT8 = win.getMouse()
    ChristmesTreeCopy2 = Polygon(CT6, CT7, CT8)
    ChristmesTreeCopy2.setFill("green")
    ChristmesTreeCopy2.setOutline("green")
    ChristmesTreeCopy2.draw(win)

    CT4 = win.getMouse()
    CT5 = win.getMouse()
    ChristmesTree2 = Rectangle(CT4, CT5)
    ChristmesTree2.setFill("brown")
    ChristmesTree2.setOutline("brown")
    ChristmesTree2.draw(win)

    CT11 = win.getMouse()
    CT21 = win.getMouse()
    CT31 = win.getMouse()
    snowman = Polygon(CT11, CT21, CT31)
    snowman.setFill("red")
    snowman.setOutline("red")
    snowman.draw(win)

    h1 = win.getMouse()
    h2 = win.getMouse()
    head = Oval(h1, h2)
    head.setFill("white")
    head.setOutline("white")
    head.draw(win)

    e1 = win.getMouse()
    e2 = win.getMouse()
    leftEye = Oval(e1, e2)
    leftEye.setFill("red")
    leftEye.setOutline("red")
    leftEye.draw(win)

    rightEye = leftEye.clone()
    p = win.getMouse()
    c = leftEye.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    rightEye.move(dx, dy)
    rightEye.draw(win)

    m1 = win.getMouse()
    m2 = win.getMouse()
    mouth = Oval(m1, m2)
    mouth.setOutline("red3")
    mouth.setFill("red3")
    mouth.draw(win)

    h3 = win.getMouse()
    h4 = win.getMouse()
    snowmanHead = Oval(h3, h4)
    snowmanHead.setFill("white")
    snowmanHead.setOutline("white")
    snowmanHead.draw(win)

    Text(Point(320, 460), "Click angin to quit.").draw(win)
    win.getMouse()


# tree_win()

def dice_win():
    win = GraphWin("Five Dice", 640, 640)
    win.setCoords(0.0, 0.0, 6.0, 6.0)

    def dice(a = 0):
        dice =Rectangle(Point(0.5+a, 2.5), Point(1.5+a, 3.5))
        dice.draw(win)
        dice.setFill("white")
        dice.setOutline("red")
        
    def pointn(a = 0):
        p = Circle(Point(1.0, 3.0), 0.2 - a)
        p.draw(win)
        p.setFill("red")
        p.setOutline("red")
    
    dice(0)
    pointn(0)

    dice(1)
    p1 = Circle(Point(1.8, 3.0), 0.1)
    p1.setFill("red")
    p1.setOutline("red")
    p1.draw(win)
    p2 = p1.clone()
    p2.move(0.4, 0)
    p2.draw(win)


    dice(2)
    p3 = p1.clone()
    p3.move(1, -0.3)
    p3.draw(win)
    p4 = p1.clone()
    p4.move(1.2, 0)
    p4.draw(win)
    p5 = p1.clone()
    p5.move(1.4, 0.3)
    p5.draw(win)

    dice(3)
    p6 = p1.clone()
    p6.move(2, -0.3)
    p6.draw(win)
    p7 = p1.clone()
    p7.move(2, 0.3)
    p7.draw(win)
    p8 = p1.clone()
    p8.move(2.4, -0.3)
    p8.draw(win)
    p9 = p1.clone()
    p9.move(2.4, 0.3)
    p9.draw(win)    
            

    dice(4)
    p10 = p1.clone()
    p10.move(3, -0.3)
    p10.draw(win)
    p11 = p1.clone()
    p11.move(3, 0.3)
    p11.draw(win)
    p12 = p1.clone()
    p12.move(3.4, -0.3)
    p12.draw(win)
    p13 = p1.clone()
    p13.move(3.4, 0.3)
    p13.draw(win)
    p14 = p1.clone()
    p14.move(3.2, 0)
    p14.draw(win)

    Text(Point(3, 5), "Click angin to quit.").draw(win)
    win.getMouse()


# dice_win()


def futval_graph1():

    # Introduction
    # print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    # principal = float(input("Enter the initial principal: "))
    # apr = float(input("Enter the annualized interest rate: "))
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 240)
    win.setBackground("white")

    Text(Point(500, 50), "This program plots the growth \nof a 10-year investment.").draw(win)
    Text(Point(480, 100), "Enter the initial principal:").draw(win)
    Text(Point(450, 130), "Enter the annualized interest rate:").draw(win)
    inputText1 = Entry(Point(600, 100), 5)
    inputText1.setText("1000")
    inputText1.draw(win)
    inputText2 = Entry(Point(600, 130), 5)
    inputText2.setText("0.1")
    inputText2.draw(win)



    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)

    win.getMouse()

    principal = float(inputText1.getText())
    apr = float(inputText2.getText())


    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("red")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1, 11):
        # calculate vale for the next year
        principal = principal * (1 + apr)
        # Draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill("yellow")
        bar.setWidth(2)
        bar.draw(win)
    Text(Point(520, 230), "Click angin to quit.").draw(win)
    win.getMouse()
    # input("Pass <Enter> to quit")
    # win.close()

# futval_graph1()

from math import *
from graphics import *

def intersection():
    win = GraphWin("The intersection volume.", 640, 640)
    win.setCoords(-10.0, -10.0, 10.0, 10.0)

    Text(Point(5.9, 8), "Input Radius of circle:").draw(win)
    Text(Point(5.6, 7), "Input the line`s intercept:").draw(win)

    Text(Point(5.9, 6), "X value of intersection 1:").draw(win)
    Text(Point(5.9, 5), "X value of intersection 2:").draw(win)


    interText1 = Entry(Point(9, 8), 5)
    interText1.setText("0.0")
    interText1.draw(win)
    interText2 = Entry(Point(9, 7), 5)
    interText2.setText("0.0")
    interText2.draw(win)

    outputText1 = Text(Point(9, 6), "")
    outputText1.draw(win)
    outputText2 = Text(Point(9, 5), "")
    outputText2.draw(win)


    win.getMouse()
    Rc = float(interText1.getText())
    Ly = float(interText2.getText())



    RCircle = Circle(Point(0.0, 0.0), Rc)
    RCircle.draw(win)
    RCircle.setFill("yellow")
    Lline = Line(Point(-8, Ly), Point(8, Ly))
    Lline.draw(win)

    Po1_x = -math.sqrt(Rc * Rc - Ly * Ly )
    Po1_y = Ly 
    Po2_x = math.sqrt(Rc * Rc- Ly * Ly )
    Po2_y = Ly
    
    Po1 = Circle(Point(Po1_x, Po1_y), 0.1)
    Po1.draw(win)
    Po1.setFill("red")
    Po1.setOutline("red")

    Po2 = Circle(Point(Po2_x, Po2_y), 0.1)
    Po2.draw(win)
    Po2.setFill("red")
    Po2.setOutline("red")

    outputText1.setText(round(Po1_x, 2))
    outputText2.setText(round(Po2_x, 2))


    Text(Point(0, -9), "Click angin to quit.").draw(win)
    win.getMouse()

# intersection()


def line_information():
    win = GraphWin("Line information.", 640, 480)
    win.setCoords(-32, -24, 32, 24)
    # win.setFill("white")

    Text(Point(-20, 22), "Please click twice in the window.").draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()

    p1c = Circle(p1, 0.3)
    p1c.setFill("red")
    p1c.setOutline("red")

    p2c = Circle(p2, 0.3)
    p2c.setFill("red")
    p2c.setOutline("red")


    ll = Line(p1, p2)
    ll.setOutline("yellow")
    ll.draw(win)

    p1c.draw(win)
    p2c.draw(win)

    dx = p1.getX() - p2.getX()
    dy = p1.getY() - p2.getY()
    dx1 = p1.getX() + p2.getX()
    dy1 = p1.getY() + p2.getY()    

    p3c = Circle(Point(dx1/2, dy1/2), 0.3)
    p3c.setFill("red")
    p3c.setOutline("red")
    p3c.draw(win)

    Sl = float(dx / dy)

    length = math.sqrt(dx*dx + dy*dy)

    win.getMouse()


    Text(Point(12, 20), "Midpoint coordinates:").draw(win)
    outputText1 = Text(Point(22.3, 20), "").draw(win)
    outputText11 = Text(Point(27,20), "").draw(win)
    Text(Point(15, 17), "Slope of line segment:").draw(win)
    outputText2 = Text(Point(25, 17), "").draw(win)
    Text(Point(15, 14), "Length of line segment:").draw(win)       
    outputText3 = Text(Point(25, 14), "").draw(win)

    outputText1.setText(round(dx1/2, 2))
    outputText11.setText(round(dy1/2, 2))
    outputText2.setText(round(Sl, 2))
    outputText3.setText(round(length, 2))


    Text(Point(0, -22), "Click angin to quit.").draw(win)
    win.getMouse()


# line_information()

def rectangle_information():

    win = GraphWin("Rectangle information.", 640, 640)
    win.setCoords(-32, -32, 32, 32)

    Text(Point(-20, 28), "Please click twice in the window.").draw(win)   

    p1 = win.getMouse()
    p2 = win.getMouse()

    Rec = Rectangle(p1, p2)
    Rec.setFill("cyan")
    Rec.setOutline("cyan")
    Rec.draw(win)

    p1_x = p1.getX()
    p1_y = p1.getY()
    p2_x = p2.getX()
    p2_y = p2.getY()


    aL = abs(p1_x - p2_x)
    bL = abs(p1_y - p2_y)


    A = aL * bL 
    S = 2*(aL + bL)

    Text(Point(19.2, 28), "Area of rectangle:").draw(win)
    outputText1 = Text(Point(28, 28), "").draw(win)
    Text(Point(14, 26), "The circumference of a rectangle:").draw(win)
    outputText2 = Text(Point(28, 26), "").draw(win)

    outputText1.setText(round(A, 2))
    outputText2.setText(round(S, 2))


    Text(Point(0, -28), "Click angin to quit.").draw(win)
    win.getMouse()


# rectangle_information()


def triangle_information():

    win = GraphWin("Triangle information.", 640, 640)
    win.setCoords(-32, -32, 32, 32)

    Text(Point(-20, 28), "Please click three in the window.").draw(win)

    p1 = win.getMouse()
    p1_x = p1.getX()
    p1_y = p1.getY()
    p2 = win.getMouse()
    p2_x = p2.getX()
    p2_y = p2.getY()
    p3 = win.getMouse()
    p3_x = p3.getX()
    p3_y = p3.getY()

    dxa = p1_x - p2_x
    dya = p1_y - p2_y
    a = math.sqrt(dxa*dxa + dya*dya)

    dxb = p1_x - p3_x
    dyb = p1_y - p3_y
    b = math.sqrt(dxb*dxb + dyb*dyb)

    dxc = p3_x - p2_x
    dyc = p3_y - p2_y
    c = math.sqrt(dxc*dxc + dyc*dyc)

    S1 = (a+b+c)/2
    A1 = math.sqrt(S1*(S1-a)*(S1-b)*(S1-c))

    triangle_I = Polygon(p1, p2, p3)
    triangle_I.setFill("gold")
    triangle_I.setOutline("gold")
    triangle_I.draw(win)


    Text(Point(19.2, 28), "Area of triangle:").draw(win)
    outputText1 = Text(Point(28, 28), "").draw(win)
    Text(Point(14, 26), "The circumference of a triangle:").draw(win)
    outputText2 = Text(Point(28, 26), "").draw(win)

    outputText1.setText(round(A1, 2))
    outputText2.setText(round(S1, 2))

    Text(Point(0, -28), "Click angin to quit.").draw(win)
    win.getMouse()

# triangle_information()


def room_five():

    win = GraphWin("Triangle information.", 640, 640)
    win.setCoords(-32, -32, 32, 32)

    Text(Point(-20, 28), "Please click five in the window.").draw(win)

    p1 = win.getMouse()
    p1_x = p1.getX()
    p1_y = p1.getY()    
    p2 = win.getMouse()
    p2_x = p2.getX()
    p2_y = p2.getY()  
    length1 = abs(p2_x - p1_x)/5   

    room1 = Rectangle(p1, p2)
    room1.setFill("white")
    room1.setOutline("white")
    room1.draw(win)
 
    p3 = win.getMouse()
    p3_x = p3.getX()
    p3_y = p3.getY()   

    room2 = Rectangle(Point(p3_x - length1/2, p1_y), Point(p3_x + length1/2, p3_y))
    room2.setFill("yellow")
    room2.setOutline("yellow")
    room2.draw(win)

    p4 = win.getMouse()
    p4_x = p4.getX()
    p4_y = p4.getY()   

    room3 = Rectangle(Point(p4_x - length1/4, p4_y + length1/4), Point(p4_x + length1/4, p4_y - length1/4))
    room3.setFill("red3")
    room3.setOutline("red3")
    room3.draw(win)

    p5 = win.getMouse()

    room4 = Polygon(Point(p1_x, p2_y), p2, p5)
    room4.setFill("gold")
    room4.setOutline("gold")
    room4.draw(win)


    Text(Point(0, -28), "Click angin to quit.").draw(win)
    win.getMouse()

# room_five()


def username():
    # username.py
    #   Simple string processing program to generate username.

    print("This program generates computer username.\n")

    # get user's first and last names
    first = input("Pelease enter your first name (all lowercase): ")
    last = input("Pelease enter your last name (all lowercase): ")
    
    # concatenate first initial with 7  chars of the last name.
    uname = first[0] + last[:7]

    # output the username
    print("Your username is: ", uname)

# username()


def month_str():
    # month.py
    #   A program to print the abbreviation of a mnth, given its unumber
    #  month is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

    n = int(input("Enter a month number (1-12): "))

    # compute starting position of month n in months
    pos = (n-1)*3

    # Grab the appropriate slice from months
    monthAbbrev = months[pos:pos+3]

    # print the result 
    print("The month abbreviation is", monthAbbrev + ".")

# month_str()


def month_list():
    # A program to print the month abbreviation, given its number.

    # month is a list used as a lookup table
    months = ["Jan", "Feb", "Mar", "Apr", "May",
     "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # months = ["January", "February", "March", "April", 
    # "May", "June", "July", "August", "September", "October", "November", "December"]
    
    n = int(input("Enter a month number (1-12): "))

    print("The month abbreviation is", months[n-1] + ".")


# month_list()



def message_Unicode():
    # test2numbers.py
    #   A program to convert a textual message into a sequence of
    #       numbers, utilizing the underlying Unicode encoding.

    print("This program convert a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message.\n")

    # Get the message to encode
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes: ")

    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")

    print() # blank line before prompt

# message_Unicode()


def Unicode_message():
    # nmbers2text.py
    #   A program to convert a swquence of Unicode numbers into
    #       a string of text.

    print("This prgram converts a sequence of Unicode numbers into")
    print("the string of the txet that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded messages: ")

    # Loop through each substring and build Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr)            # convert digits to a number
        message = message + chr(codeNum) # concatentate character to message
    print("\nThe decoded message is: ", message)

# Unicode_message()


def Unicode_messageList():
    # nmbers2text2.py
    #   A program to convert a swquence of Unicode numbers into
    #       a string of text. Efficient version using a list accumulator.

    print("This prgram converts a sequence of Unicode numbers into")
    print("the string of the txet that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded messages: ")

    # Loop through each substring and build Unicode message
    # message = ""
    chars = []
    for numStr in inString.split():
        codeNum = int(numStr)            # convert digits to a number
        # message = message + chr(codeNum) # concatentate character to message
        chars.append(chr(codeNum))       # accumulate new character
    message = "".join(chars)
    print("\nThe decoded message is: ", message)

# Unicode_messageList()



def change2():
    # change2.py
    #   A program to calculate the value of same change in dollars
    #   This version represents the total cash in cents. 

    print("Change Counter\n")
    print("Please enter the count of each coin type. ")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    total = quarters*25 + dimes*10 + nickels*5 + pennies

    print("The total value of your change is ${0}.{1:0>2}".format(total//100, total%100))


# change2()



def printfile():
    #   printfile.py
    #   Print a file to the screen. 

    fname = input("Enter filename: ")
    infile = open(fname, "r")
    date = infile.read()
    print(date)

# printfile()

def userfile():
    # userfile.py 
    #   Program to create a file of usernames in batch mode. 

    print("This program creates a file of usernames from a ")
    print("file of names.")

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the userna
        uname = (first[0] + last[:7]).lower()
        # write it to the output file
        print(uname, file=outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

# userfile()





def datecovert():
    # Coverts a date in form "mm/dd/yyyy" to "month day, year"

    # get the date
    dateStr = input("Enter a date(mm/dd/yyyy): ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # months = ["Jan", "Feb", "Mar", "Apr", "May",
     # "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # convert monthStr to the month name 
    months = ["January", "February", "March", "April", 
    "May", "June", "July", "August", "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]
    # n = int(input("Enter a month number (1-12): "))

    print("The month abbreviation is {0} {1}, {2}".format(monthStr, dayStr, yearStr))


# datecovert()


def fractionGrade():
    fraction = input("Input fraction(0-5): ")
    grade = ["0-F", "1-F", "2-D", "3-C", "4-B", "5-A"]
    fg = float(fraction)

    print("This fraction grade is {0}".format(grade[int(fg)]))


# fractionGrade()


def fractionGrade1():
    fraction = input("Input fraction(0-100): ")
    grade = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A"]
    fg = float(fraction)//10

    print("This fraction grade is {0}".format(grade[int(fg)]))


# fractionGrade1()


def testll():

    sentence = input("Input your convert sentence: ")
    sT = sentence.split(" ")

    Ch = ""
    for ch in sT:
        cH = ch.capitalize()
        print(cH)
        Ch = Ch + cH[0]


    print("Convert sentence: ", Ch)

# testll()

def namenumber():

    name = input("Input your convert name: ")


    Nn = 0
    for nameN in name:
        nN = int(ord(nameN)-96)
        print(nN)
        Nn = Nn + nN


    print("Convert number: ", Nn)

# namenumber()

def namenumber1():

    names = input("Input your convert names: ")
    name = "".join(names.split())

    Nn = 0
    for nameN in name.lower():
        nN = int(ord(nameN)-96)
        print(nN)
        Nn = Nn + nN


    print("Convert number: ", Nn)

# namenumber1()


def kasakey():

    message = input("Input your need convert message: ")
    key = 30

    messagen = ""
    for ch in message:
        print(ch)
        messagen = messagen + chr(ord(ch) + key)

    print(messagen)

    messagenc = ""
    for ch in messagen:
        messagenc = messagenc + chr(ord(ch) - key)

    print(messagenc)



# kasakey()


def kasakey1():

    message = input("Input your need convert message: ")
    # key = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ."
    key = 1


    messagen = ""
    for ch in message:
        print(ch)
        if ord(ch) == 122:
            messagen = messagen + chr(ord(ch) - 25)
        else: messagen = messagen + chr(ord(ch) + key)
    print(messagen) 

    messagenc = ""
    for ch in messagen:
        if ord(ch) == 97:
            messagenc = messagenc + chr(ord(ch) + 25)
        else: messagenc = messagenc + chr(ord(ch) - key)

    print(messagenc)



# kasakey1()

def number_sentence():
    message = input("Input your's needs statistical sentence: ")

    Ch = ""
    for ch in message.split():
        Ch = Ch + ch[0]

    nuS = len(Ch)

    print("Your input {0} word.".format(nuS))

# number_sentence()



def number_word():
    message = input("Input your's needs statistical sentence: ")

    Ch1 = 0
    Ch = ""
    for ch in message.split():
        Ch1 = Ch1 + len(ch)
        Ch = Ch + ch[0]

    nuS = Ch1/len(Ch)

    print("Your input {0:0} word. Average word length {1:0.02f}.".format(len(Ch),  nuS))

# number_word()



def chaos1():
    # chaos.py
    # A simple program illustrating chaotic behavior. 

    print("This program illustrating a chaotic function.")
    x, y = map(float, input("Enter two numbers between 0 and 1 : ").split())
    n = int(input("Number of input cycles: "))

    print("input {0:^15} {1:^15}".format(x, y))
    print("-----------------------------------------------")
    for i in range(n):
        x = 3.9 * x *(1 - x)
        y = 3.9 * y *(1 - y)
        print("{2}     {0:^15.06f} {1:^15.06f}".format(x, y, i+1))



# chaos1()


from tkinter.filedialog import askopenfilename, asksaveasfilename

def number_word1():

    infilename = askopenfilename()
    infile = open(infilename, "r")
    infile1 = open(infilename, "r")


    # line = infile.readline()
    i = 0
    # line = ""
    for line in infile:
        # print(line)
        i = i + 1
    # print("This document has a total of {0} line".format(i))



    Ch1 = 0
    Ch = ""
    # infile2 = infile1.read()
    for ch in infile1.read().split():
         Ch1 = Ch1 + len(ch)
         Ch = Ch + ch[0]
    # print("This document has a total of {0} words and {1} characters..".format(len(Ch),  Ch1))


    # for1()
    # for2()
    # CH = len(Ch)
    # nuS = Ch1/len(Ch)
    infile.close()

    print("This document has a total of {0} line, {1} words and {2} characters..".format(i, len(Ch),  Ch1))

# number_word1()


from tkinter.filedialog import askopenfilename, asksaveasfilename
from graphics import *

def student_G():

    infilename = askopenfilename()
    infile = open(infilename, "r")
    # infile1 = open(infilename, "r")

    st_Nu = int(infile.readline())

    win = GraphWin("student fraction.", 640, 200 + 40*st_Nu)

    # fileL = infile.read().split()
    i = 0
    for ch in infile:

        Ch = ch.split()
        Text(Point(320, 40), "Total {0} students.".format(st_Nu)).draw(win)
        Text(Point(80, 80 + i*40), "{0:<20}".format(Ch[0])).draw(win)
        Text(Point(130 + 2*float(Ch[1]), 80 + i*40), "{:<3}".format(Ch[1])).draw(win)
        Tg = Rectangle(Point(110, 70 + i*40), Point(110 + 2*float(Ch[1]), 90 + i*40))
        Tg.setFill("yellow")
        Tg.setOutline("yellow")
        Tg.draw(win)
        i = i + 1


    Text(Point(320, 120 + 40*st_Nu), "Click angin to quit.").draw(win)
    win.getMouse()
    infile.close()

# student_G()



from tkinter.filedialog import askopenfilename, asksaveasfilename
from graphics import *

def student_GN():

    infilename = askopenfilename()

    infile1 = open(infilename, "r")
    infile = open(infilename, "r")
    win = GraphWin("student fraction.", 640, 480)

    # i = 0
    # for line in infile1:
        # print(line)
    for i in range(11):

        # i = i + 1
        # print(infile.read())
        c = infile.read().split().count(str(i))
        # print(c)
        Text(Point(115 + i*40, 320), "{:<3}".format(i)).draw(win)
        Text(Point(115 + i*40, 290 - 30*float(c)), "{:<3}".format(c)).draw(win)
        Tg = Rectangle(Point(100 + i*40, 300), Point(120 + i*40, 300 - 30*float(c)))
        Tg.setFill("yellow")
        Tg.setOutline("yellow")
        Tg.draw(win)
        infile = open(infilename, "r")
        # infile1 =open(infilename, "r")   

    Text(Point(320, 440), "Click angin to quit.").draw(win)
    win.getMouse()
    infile.close()

# student_GN()







