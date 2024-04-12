"""More OOP Practice."""


__author__ = "730484781"

from lessons.CQ08.point import Point

point1: Point = Point(2.2, 1.1)
point1.scale_by(3)
point2: Point = point1.scale(4)


print(point1.x)
print(point2.x)