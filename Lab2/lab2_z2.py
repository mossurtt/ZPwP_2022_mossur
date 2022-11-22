class Adres:

    def __init__(self, ndomu, ulica, 
    nmieszkania = '', miasto = '', kodpocztowy = ''):
        self._ndomu = ndomu
        self._ulica = ulica
        self._nmieszkania = nmieszkania
        self._miasto = miasto
        self._kodpocztowy = kodpocztowy

    def show(self):
        print(self._ulica, self._ndomu, self._nmieszkania)
        print(self._kodpocztowy, self._miasto)

    #def comesBefore(self, other):
        


a = Adres("9", "Karpenka-Karoho", miasto = "Lutsk", kodpocztowy = "43021")
b = Adres("76", "Dabrowskiego", miasto = "Czestochowa", kodpocztowy = "42200")
a.show()