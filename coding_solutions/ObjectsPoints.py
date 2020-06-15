class Point:
 def __init__(self,a,b):
      self.x = a
      self.y = b
 def translate(self,deltax,deltay):
     self.x += deltax
     self.y += deltay 


p=Point(3,2)
p.translate(5,3)
print(p.x,p.y)
