
'''
    basic.py:基本的图元
'''
from math import sin,cos
def setPixel(canvas,point,color):
    for i in range(1,4):
        pixel = canvas[:,:,:i]
        shape = pixel.shape
        if shape[0] - point[1] == shape[0]:
            x = shape[0] - 1
        else:
            x = shape[0] - point[1]

        pixel[x][point[0]] = color[i - 1]


class primitive:
    def __init__(self):
        self.points = []
    def rasterization(self,canvas):
        for point in self.points:
            setPixel(canvas,point,self.color)
    def move(self,tx,ty):
        for i in range(len(self.points)):
            self.points[i][0] += tx
            self.points[i][1] += ty
    def rotate(self,tx,ty,theta):
        points = []
        for i in range(len(self.points)):
            self.points[i][0] = round(tx + (self.points[i][0] - tx)*cos(theta) - (self.points[i][1] - ty)*sin(theta))
            self.points[i][1] = round(ty + (self.points[i][0] - tx)*sin(theta) + (self.points[i][1] - ty)*cos(theta))

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
        self.calc_point(x0,y0,xend,yend)
        #计算点
    def calc_point(self,x0,y0,xend,yend):
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
                self.points.append([x,x])
                x += 1
            return
        elif k == 0:
            x,y = x0,y0
            while x < xend:
                self.points.append([x,y])
                x += 1
            return
        elif k == -1:
            y,x = x0,y0
            while y < yend:
                self.points.append([x,y])
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
            self.points.append([x,y])

class lines(line):
    #多条直线
    def __init__(self,color=(255,255,255),size=1):
        self.xy_list = []
        self.points = []
        self.size = 1
        self.mode = 0
        self.color = color
    def rasterization(self,canvas):
        if len(self.xy_list) >= 2:
            for i in range(len(self.xy_list) - 1):
                self.calc_point(self.xy_list[i][0],self.xy_list[i][1],self.xy_list[i+1][0],self.xy_list[i+1][1])
        else:
            return
        for point in self.points:
            setPixel(canvas,point,self.color)
    def set_mode(self,mode):
        self.mode = mode
    def add_point(self,x,y,z=0):
        self.xy_list.append((x,y))

class cricle(primitive):
    #圆
    def __init__(self,x,y,r,color=(255,255,255),size=1):
        self.x = x
        self.y = y
        self.r = r
        self.size = size
        self.color = color
        self.points = []
        self.__calc_point(self.r,self.x,self.y)
    def __calc_point(self,r,x0,y0):
        x = 0
        y = r
        p = 5/4 - r
        while x <= y:
            x += 1
            if p < 0:
                p += 2*x + 1
            else:
                p += 2 * (x - (y + 0.1)) + 1
                y -= 1
            #print(y0,y)
            self.__cricPoints(x0,y0,x,y)
        
        #处理在XY轴上的点
        self.points.append((x0,y0 + r))
        self.points.append((x0,y0 - r))
        self.points.append((x0 + r,y0))
        self.points.append((x0 - r,y0))

    def __cricPoints(self,x0,y0,x,y):
        self.points.append((x0 + x,y0 + y))
        self.points.append((x0 - x,y0 + y))
        self.points.append((x0 + x,y0 - y))
        self.points.append((x0 - x,y0 - y))
        self.points.append((x0 + y,y0 + x))
        self.points.append((x0 - y,y0 + x))
        self.points.append((x0 + y,y0 - x))
        self.points.append((x0 - y,y0 - x))

class ellipse(primitive):
    #椭圆
    def __init__(self,centerx,centery,x,y,color=(255,255,255),size=1):
        self.centerx = centerx
        self.centery = centery
        self.x = x
        self.y = y
        self.size = size
        self.points = []
        self.color = color
        self.__calc_point(x,y,centerx,centery)

    def __calc_point(self,rx,ry,centerx,centery):
        rx2 = rx**2
        ry2 = ry**2
        tworx2 = 2 * rx2
        twory2 = 2 * ry2
        x = 0
        y = ry
        px = 0
        py = tworx2 * y

        p = round(ry2 - rx2*ry + 0.25*rx2)
        while px < py:
            x += 1
            px += twory2
            if p < 0:
                p += ry2 + px
            else:
                y -= 1
                py -= tworx2
                p += ry2 + px - py
            self.__plotPoint(centerx,centery,x,y)
        p = round(ry2*(x+0.5)**2 + rx2*(y-1)**2 - rx2*ry2)
        while y > 0:
            y -= 1
            py -= tworx2
            if p > 0:
                p += rx2 - py
            else:
                x += 1
                px += twory2
                p += rx2 - py + px
            self.__plotPoint(centerx,centery,x,y)
    
        self.points.append((centerx,centery + ry))
        self.points.append((centerx,centery - ry))

    def __plotPoint(self,centerx,centery,x,y):
        self.points.append((centerx + x,centery + y))
        self.points.append((centerx - x,centery + y))
        self.points.append((centerx + x,centery - y))
        self.points.append((centerx - x,centery - y))