import math

class SodaCan:

    def __init__(self, h, r):
        self._h, self._r = h, r
         
    
    def getSurfaceArea(h, r):
        surfaceArea = 2 * math.pi * r * h + 2 * math.pi * r**2
        return surfaceArea

    def getVolume(h, r):
        volume = math.pi * r**2 * h
        return volume
#????????
def main():
    a = SodaCan(10, 2)
    print(a)
    print(SodaCan.getSurfaceArea(10, 2))
    print(SodaCan.getVolume(10, 2))

main()