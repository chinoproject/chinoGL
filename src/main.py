from draw import *
import basic
#test
if __name__ == '__main__':
    d = draw(1000,1000)
    l = basic.line(0,0,200,200)
    l.move(100,100)
    d.add_primitive(l)
    d.rasterization()
    d.show()