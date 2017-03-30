from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
ident(transform)

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print



def herm(x0, y0, x1, y1, rx0, ry0, rx1, ry1):
    return ('hermite\n%d %d %d %d %d %d %d %d\n' % (x0,y0,x1,y1,rx0,ry0,rx1,ry1))
def bez(x0, y0, x1, y1, x2, y2, x3, y3):
    return ('bezier\n%d %d %d %d %d %d %d %d\n' % (x0,y0,x1,y1,x2,y2,x3,y3))
def line(x0,y0,z0,x1,y1,z1):
    return ('line\n%d %d %d %d %d %d\n' % (x0,y0,z0,x1,y1,z1))
def circ(x,y,z,r):
    return ('circle\n%d %d %d %d\n' % (x,y,z,r))
def sphere(x,y,z,r):
    return ('sphere\n%d %d %d %d\n' % (x,y,z,r))
def torus(x,y,z,sm,bg):
    return ('torus\n%d %d %d %d %d\n' % (x,y,z,sm,bg))
def box(x,y,z,w,h,d):
    return ('box\n%d %d %d %d %d %d\n' % (x,y,z,w,d,h))
def scale(x,y,z):
    return 'scale\n%f %f %d\n' % (x,y,z)
def move(x,y,z):
    return 'move\n%f %f %f\n' % (x,y,z)
def rot(a,t):
    return 'rotate\n%s %s\n' % (a,t)
def save_write(f):
    return 'save\n%s\n' % (f)
def col(r,g,b):
    return 'color\n%d %d %d\n' % (r,g,b)

#color = [199,192,216]

def setup_script():
    f = open('script','w')
    f.write(col(78,8,136))
    f.write(sphere(0,0,0,150))
    f.write(sphere(0,0,0,200))
    f.write(box(-150,150,150,300,300,300))
    f.write(box(200,200,0,50,50,50))
    f.write(torus(-25,150,0,25,150))
    

    
        
    f.write('ident\n')
    f.write(rot('x',45))
    f.write(rot('y',45))
    f.write(move(250,250,0))
    f.write('apply\n')
    
    f.write('save\nthing.png\n')
    f.close()


setup_script()


parse_file( 'dwscript', edges, transform, screen, color )
