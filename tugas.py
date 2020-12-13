class Segitiga:

    name = ""  # public
    alas = ""
    tinggi = ""
    luas = ""

    def __init__(self, name):  # method Konstruktor
        self.name = name

    def set_alas(self, alas):  # method
        self.alas = alas

    def set_tinggi(self, tinggi):
        self.tinggi = tinggi

    def set_luas(self, luas):
        self.luas = luas


A05 = Segitiga("Objek Luas Segitiga\n")
A05.set_alas(3)
A05.set_tinggi(22)
A05.luas = 0.5 * A05.alas*A05.tinggi


print("%sPanjang Alas Segitiga adalah : %d\ndengan Tinggi Segitiga adalah : %d\n\ndan Luasnya adalah : %d\n" %
      (A05.name, A05.alas, A05.tinggi, A05.luas))
