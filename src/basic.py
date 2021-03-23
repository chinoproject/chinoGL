
'''
    basic.py:基本的图元
'''
def setPixel(canvas,point,aisle=1):
    pixel = canvas[:,:,:aisle]
    shape = pixel.shape
    pixel[point[1]][shape[1] - point[0]] = 255

class primitive:
    def rasterization(self,canvas):
        pass

class point(primitive):
    #点
    def __init(self,x,y,z=0,size=1):
        self.x = x
        self.y = y
        self.z = 0
        self.size = size
    def rasterization(self,canvas):
        pass

class line(primitive):
    #直线
    def __init__(self,x0,y0,xend,yend,size=1):
        self.x0 = x0
        self.y0 = y0
        self.xend = xend
        self.yend = yend

        self.size = size
        self.points = []

        #计算点
        dx = abs(xend - x0)
        dy = abs(yend - y0)
        p = 2 * dy - dx
        try:
            k = abs((yend-y0)/(xend - x0))
        except:
            k = -1  #垂直直线

        if k < 1:
            twody = 2 * dy
            twodymiusdx = 2 * (dy - dx)
            if x0 > xend:
                x = xend
                y = yend
                xend = x0
            else:
                x = x0
                y = y0
        elif k > 1:
            twody = 2 * dx
            twodymiusdx = 2 * (dx - dy)
            if y0 > yend:
                y = xend
                x = yend
                xend = y0
            else:
                x,y = x0,y0
                xend,yend=yend,xend
        elif k == 1.0:
            x,y = x0,y0
            while x <= xend:
                self.points.append((x,y))
                x += 1
                y += 1
            return
        elif k == 0:
            x,y = x0,y0
            while x0 < xend:
                self.points.append((x,y))
                x += 1
            return
        elif k == -1:
            y,x = x0,y0
            while x0 < xend:
                self.points.append((x,y))
                x += 1
            return
        self.points.append((x,y))

        while x < xend:
            x += 1
            if p < 0:
                p += twody
            else:
                y += 1
                p += twodymiusdx
            self.points.append((x,y))

    def rasterization(self,canvas):
        for point in self.points:
            setPixel(canvas,point)

class lines(line):
    #多条直线
    def __init(self,size=1):
        self.xy_list = []
        self.points = []
        self.size = 1
    def rasterization(self,canvas):
        pass
    def add_point(self,x,y,z=0):
        pass

class cricle(primitive):
    #圆
    def __init__(self,x,y,r,size=1):
        self.x = x
        self.y = y
        self.r = r
        self.size = size
    def rasterization(self,canvas):
        pass

class ellipse(primitive):
    #椭圆
    def __init__(self,rx,ry,x,y,size=1):
        self.rx = rx
        self.ry = ry
        self.x = x
        self.y = y
        self.size = size
    def rasterization(self,canvas):
        pass