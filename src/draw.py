import numpy as np
import basic
from PIL import Image

class draw:
    def __init__(self,width,height,alpha=0):
        self.draw_list = []
        self.canvas = np.array(np.zeros((width,height,3 + alpha))).astype(np.uint8)
        print(self.canvas.shape)
    def add_primitive(self,primitive):
        self.draw_list.append(primitive)
    def save(self,name):
        image = Image.fromarray(self.canvas).convert("RGB")
        image.save(name)
    def rasterization(self):
        for i in self.draw_list:
            i.rasterization(self.canvas)
    def show(self):
        image = Image.fromarray(self.canvas.copy()).convert("RGB")
        image.show()

if __name__ == '__main__':
    d = draw(400,400)
    l = basic.line(100,100,200,200)
    print(l.points)
    d.add_primitive(l)
    d.rasterization()
    d.show()
