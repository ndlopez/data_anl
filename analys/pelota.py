'''Show a ball bouncing off the of the window'''
from graphics import *
import time,random
def bounceInbox(shape,dx,dy,xLow,xHigh,yLow,yHigh):
    delay=.005
    for i in range(600):
        shape.move(dx,dy)
        center=shape.getCenter()
        x=center.getX()
        y=center.getY()
        if x < xLow:
            dx=-dx
        elif x>xHigh:
            dx=-dx
        if y <yLow:
            dy=-dy
        elif y>yHigh:
            dy=-dy
        time.sleep(delay)

def getRandompoint(xLow,xHigh,yLow,yHigh):
    x=random.randrange(xLow,xHigh+1)
    y=random.randrange(yLow,yHigh+1)
    return Point(x,y)
def makeDisk(center,radius,win):
    disk=Circle(center,radius)
    disk.setOutline("red")
    disk.setFill("red")
    disk.draw(win)
    return disk
def bounceBall(dx,dy):
    win=GraphWin('Ball bounce',190,190)
    win.yUp()#GraphWin has no object yUp!
    radius=10
    xLow=radius
    xHigh=win.getWidth()-radius
    yLow=radius
    yHigh=win.getHeight()-radius
    center=getRandompoint(xLow,xHigh,yLow,yHigh)
    ball=makeDisk(center,radius,win)
    bounceInbox(ball,dx,dy,xLow,xHigh,yLow,yHigh)
    win.close()

bounceBall(3,5)

                
