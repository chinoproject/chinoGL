from draw import *
import basic
#test
if __name__ == '__main__':
    d = draw(1000,1000)
    l = basic.ellipse(400,400,300,200)
    d.add_primitive(l)
    d.rasterization()
    d.show()