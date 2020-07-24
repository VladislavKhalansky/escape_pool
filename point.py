import math


class Point:
    """ Класс материальных точек на плоскости. """
    def __init__(self, x, y, speed=0):
        self.x = x
        self.y = y
        self.speed = speed

    def __repr__(self):
        return '   x: ' + str(self.x) + ' y: ' + str(self.y)

    def distance(self, target):
        """ Расстояние между двумя точками. """
        x = self.x - target.x
        y = self.y - target.y
        distance = math.sqrt(x ** 2 + y ** 2)
        return distance

    def move(self, target):
        """ Перемещает точку по вектору с указанной скоростью. """
        x = self.x - target.x
        y = self.y - target.y
        z = math.sqrt(x ** 2 + y ** 2)
        self.x += x / z * self.speed
        self.y += y / z * self.speed
    
    def show_side(self, size):
        """ Определяет, на какой стороне квадрата
            с указанной стороной находится точка. """
        side = ['up', 'down', 'left', 'right']
        if (self.x != 0 and self.x != size)\
                and (self.y != 0 and self.y != size):
            return 'DetectSideError'
        elif self.y == 0:
            return side[0]
        elif self.y == size:
            return side[1]
        elif self.x == 0:
            return side[2]
        elif self.x == size:
            return side[3]


class Chaser:
    """ Класс догоняющего по периметру. Зачем? """
    def __init__(self, x, y, _speed):
        self.point = Point(x, y, _speed)

    def move_set(self, size, right):
        """ Движение по или против часовой стрелки. Вправо, если right=True. """
        if right:
            if self.point.x == size and self.point.y < size:
                self.point.y += self.point.speed
            elif self.point.y == size and self.point.x > 0:
                self.point.x -= self.point.speed
            elif self.point.x == 0 and self.point.y > 0:
                self.point.y -= self.point.speed
            elif self.point.y == 0:
                self.point.x += self.point.speed
        if not right:
            if self.point.x == size and self.point.y > 0:
                self.point.y -= self.point.speed
            if self.point.y == size and self.point.x < size:
                self.point.x += self.point.speed
            if self.point.x == 0 and self.point.y < size:
                self.point.y += self.point.speed
            if self.point.y == 0:
                self.point.x -= self.point.speed

    def de_way(self, end: Point, size):
        """ Определяет, в какую сторону расстояние до точки меньше."""
        right = Chaser(self.point.x, self.point.y, self.point.speed)
        right.move_set(size, right=True)
        dist_right = right.point.distance(end)
        left = Chaser(self.point.x, self.point.y, self.point.speed)
        left.move_set(size, right=False)
        dist_left = left.point.distance(end)
        if dist_right < dist_left or self.point.distance(end) > size // 2:
            return True
        else:
            return False

    def chaser_ai_core(self, target: Point, size):
        """ Magic. """
        flag = self.de_way(target, size)
        self.move_set(size, flag)
