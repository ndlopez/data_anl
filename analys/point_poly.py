#testing if a point is inside a polygon
def inside_poly(x,y,points):
    """
    return true if a coordinate (x,y) is inside a polygon
    defined by a list of vertices [(x1,y1),(x2,y2),...,(xN,yN)].
    Ref. http://ariel.com.au/a/python-point-int-poly.html
    """
    n=len(points)
    inside=False
    p1x,p1y=points[0]
    for i in range (1,n+1):
        p2x,p2y=points[i%n]
        if y>min(p1y,p2y):
            if y<=max(p1y,p2y):
                if x<=max(p1x,p2x):
                    if p1y !=p2y:
                        xinter=(y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x==p2x or x<= xinter:
                        inside=not inside
        p1x,p1y=p2x,p2y
    return inside

    
    
