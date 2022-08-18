'''import turtle
kame=turtle.Turtle()
kame.shape('turtle')
kame.shapesize(2,2,3)'''
'''def center_circle(target):
    target.penup()
    target.forward(90)
    target.left(90)
    target.pendown()
    target.circle(80)
    target.left(90)
    target.penup()
    target.forward(90)
    target.pendown()'''
def center_circle(target,r=150):
    target.penup()
    target.forward(r)
    target.left(90)
    target.pendown()
    target.circle(80)
    target.left(90)
    target.penup()
    target.forward(r)
    target.pendown()
'''Load like this:
import turtle
kame=turtle.Turtle()
kame.shape('turtle')
import "this_file"
"this_file".center_circle(kame,number) '''    
