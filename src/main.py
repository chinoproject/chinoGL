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
    r.move(150,200)
    r.scale(0.4,0.5,100,100)
    d.add_primitive(l)
    d.add_primitive(r)
    d.rasterization()
    d.show()