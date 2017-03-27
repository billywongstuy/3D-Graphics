from display import *
from matrix import *
from math import *

cos = math.cos
sin = math.sin
pi = math.pi

def add_box( points, x, y, z, width, height, depth ):
    print x,y,z
    for w in range(0,2,1):
        print w
        for h in range(-1,1,1):
            for d in range(-1,1,1):
                add_point( points, x+w*width, y+h*height, z+d*depth )
    #x,y,z
    #x,-h,z
    #w,-h,z
    #w,h,z

    #x,y,-d
    #x,-h,-d
    #w,-h,-d
    #w,h,-d

    #12 sides
    
def add_sphere( points, cx, cy, cz, r, step ):
    pts = generate_sphere( points, cx, cy, cz, r, step )
    length = len(pts)
    index = 1
    while index < length:
        prev = pts[index-1]
        curr = pts[index]
        add_edge(points,prev[0],prev[1],prev[2],curr[0],curr[1],curr[2])
        index += 1
    
    
def generate_sphere( points, cx, cy, cz, r, step ):
    '''
    points
    for rot 0 to 1:
        for circ to 1:
            x = rcos(circ*pi) + cx
            y = rsin(circ*pi) * cos(rot*2pi) + cy
            z = rsin*circ*pi) * sin(rot*2pi) + cz
    '''

    pts = []
    rot = 0
    while rot < 1:
        circ = 0
        while circ < 1:
            x = r*cos(circ*2*pi) + cx
            y = r*sin(circ*2*pi) * cos(rot*pi) + cy
            z = r*sin(circ*2*pi) * sin(rot*pi) + cz
            pts.append([x,y,z,1.0])
            circ += step
        rot += step
    return pts


def add_torus( points, cx, cy, cz, r0, r1, step ):
    pts = generate_torus( points, cx, cy, cz, r0, r1, step )
    length = len(pts)
    index = 1
    while index < length:
        prev = pts[index-1]
        curr = pts[index]
        add_edge(points,prev[0],prev[1],prev[2],curr[0],curr[1],curr[2])
        index += 1
            
def generate_torus( points, cx, cy, cz, r0, r1, step ):
    pts = []
    rot = 0
    #r1 is big radius
    #r0 is small radius
    while rot < 1:
        circ = 0
        while circ < 1:
            x = cos(rot*2*pi)*(r0*cos(rot*2*pi)+r1) + cx
            y = r0*sin(circ*2*pi) + cy
            z = -sin(rot*2*pi)*(r0*cos(circ*2*pi)+r1) + cz
            pts.append([x,y,z,1.0])
            circ += step
        rot += step
    return pts

def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    t = step

    while t <= 1.00001:
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t+= step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    t = step
    while t <= 1.00001:
        x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]
                
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t+= step

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
