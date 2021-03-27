
'''
    basic.py:基本的图元
'''
def setPixel(canvas,point,color):
    for i in range(1,4):
        pixel = canvas[:,:,:i]
        shape = pixel.shape
        if point == (0,0):
            pixel[shape[0] - 1][0] = color[i - 1]
        else:
            pixel[shape[0] - point[1]][point[0]] = color[i - 1]


class primitive:
    def rasterization(self,canvas):
        pass

class point(primitive):
    #点
    def __init__(self,x,y,color=(255,255,255),size=1):
        self.x = x
        self.y = y
        self.z = 0
        self.size = size
        self.color = color
    def rasterization(self,canvas):
        setPixel(canvas,(self.x,self.y),self.color)

class line(primitive):
    #直线
    def __init__(self,x0,y0,xend,yend,color=(255,255,255),size=1):
        self.x0 = x0
        self.y0 = y0
        self.xend = xend
        self.yend = yend

        self.size = size
        self.points = []
        self.color = color
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
                self.points.append((x,x))
                x += 1
            return
        elif k == 0:
            x,y = x0,y0
            while x < xend:
                self.points.append((x,y))
                x += 1
            return
        elif k == -1:
            y,x = x0,y0
            while y < yend:
                self.points.append((x,y))
                y += 1
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
            setPixel(canvas,point,self.color)

class lines(line):
    #多条直线
    def __init__(self,color=(255,255,255),size=1):
        self.xy_list = []
        self.points = []
        self.size = 1
        self.mode = 0
        self.color = color
    
    def __calc_point(self,x0,y0,xend,yend):
        dx = abs(xend - x0)
        dy = abs(yend - y0)
        p = 2 * dy - dx
        try:
            k = abs((yend-y0)/(xend - x0))
        except:
            k = -1  #垂直直线
        if k < 1 and k > 0:
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
                self.points.append((x,x))
                x += 1
            return
        elif k == 0:
            x,y = x0,y0
            while x < xend:
                self.points.append((x,y))
                x += 1
            return
        elif k == -1:
            y,x = x0,y0
            while y < yend:
                self.points.append((x,y))
                y += 1
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
        if len(self.xy_list) >= 2:
            for i in range(len(self.xy_list) - 1):
                print(i)
                self.__calc_point(self.xy_list[i][0],self.xy_list[i][1],self.xy_list[i+1][0],self.xy_list[i+1][1])
        else:
            return
        print(self.points)
        for point in self.points:
            setPixel(canvas,point,self.color)
    def set_mode(self,mode):
        self.mode = mode
    def add_point(self,x,y,z=0):
        self.xy_list.append((x,y))

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