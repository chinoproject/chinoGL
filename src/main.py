from draw import *
import basic
#test
if __name__ == '__main__':
    d = draw(400,400)
    l = basic.line(100,100,200,300)
    d.add_primitive(l)
    d.rasterization()
    d.show()