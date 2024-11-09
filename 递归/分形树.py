import turtle



def draw_spiral(t,lenline):
    if lenline>0:
        t.forward(lenline)
        t.right(90)
        draw_spiral(t,lenline-5)

def tree(brance_len):
    if brance_len>5:  # 递归的结束条件
        t.forward(brance_len)
        t.right(20)
        tree(brance_len-15)
        t.left(40)
        tree(brance_len-15)
        t.right(20)
        t.backward(brance_len)


t=turtle.Turtle()
t.speed(5)
t.left(90)
t.penup()
t.backward(200)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(100)
t.hideturtle()
turtle.done()