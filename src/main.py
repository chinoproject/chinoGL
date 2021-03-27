from draw import *
import basic
#test
if __name__ == '__main__':
    d = draw(400,400)
    cric = basic.cricle(100,100,50)
    d.add_primitive(cric)
    d.rasterization()
    d.show()