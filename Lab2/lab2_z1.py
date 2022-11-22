import math

class Punkt:

    def __init__(self, x, y):
        self._x, self._y = x, y

    def move(self, deltaX, deltaY):
        self._x += deltaX; self._y = deltaY

    def __str__(self):
        return f"<{self._x}, {self._y}>"

    @staticmethod
    def distance(x, y):

        distance = math.sqrt((x._x - y._x)** 2 + (y._x - y._y)** 2)
        return distance

class NazwanyPunkt(Punkt):

    def __init__(self, x, y, nazwa):
        Punkt.__init__(self, x, y)
        self._nazwa = nazwa

def main():
    a = Punkt(0, 0)
    b = NazwanyPunkt(2, 4, "nazwany")
    print(a)
    print(b)
    print(Punkt.distance(a, b))

main()

    