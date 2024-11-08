import turtle

def sierpinski(degree, points):
    color = ['red', 'green', 'blue', 'yellow', 'pink', 'orange', 'purple', 'brown', 'gray', 'white']
    drawTriangle(points, color[degree])
    if degree > 0:
        sierpinski(degree-1,
                   {'left':points['left'],
                    'top':get_mid(points['left'], points['top']),
                    'right':get_mid(points['left'], points['right'])}
                   )
        sierpinski(degree-1,
                   {'left':get_mid(points['left'], points['top']),
                    'top':points['top'],
                    'right':get_mid(points['right'], points['top'])}
                   )
        sierpinski(degree-1,
                   {'left':get_mid(points['left'], points['right']),
                    'top':get_mid(points['right'], points['top']),
                    'right':points['right']
                   }
        )

def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

t = turtle.Turtle()
t.speed(10000)
point = {'left':(-200, -100), 'top':(0, 200), 'right':(200, -100)}
sierpinski(9,point)
turtle.done()