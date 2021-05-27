import math
 
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
p1 = Point2D(x=-1000000000, y=1000000000)    # 점1
p2 = Point2D(x=-1, y=1)    # 점2
 
a = p2.x - p1.x    # 선 a의 길이
b = p2.y - p1.y    # 선 b의 길이
 
c = math.sqrt((a * a) + (b * b))    # (a * a) + (b * b)의 제곱근을 구함
print(c)    # 42.42640687119285