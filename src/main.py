from draw import *
import basic
#test
if __name__ == '__main__':
    d = draw(400,400)
    l = basic.lines()
    l.add_point(0,0)
    l.add_point(100,100)
    l.add_point(100,200)
    l.add_point(200,200)
    d.add_primitive(l)
    d.rasterization()
    d.show()