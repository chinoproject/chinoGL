from draw import *
import basic
from math import pi
import copy
#test
if __name__ == '__main__':
    d = draw(1000,1000)
    l = basic.line(0,0,200,200)
    l.move(100,100)
    r = copy.deepcopy(l)
    r.rotate(100,100,pi/6)
    d.add_primitive(l)
    d.add_primitive(r)
    d.rasterization()
    d.show()