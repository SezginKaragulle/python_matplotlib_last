import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def grafik_1():
    yasListesi = [10,20,30,30,30,40,50,60,70,75]
    kiloListesi = [20,60,80,85,86,87,70,90,95,90]

    numpyYasListesi = np.array(yasListesi)
    numpyKiloListesi = np.array(kiloListesi)

    print(plt.plot(numpyYasListesi,numpyKiloListesi,"g"))
    plt.xlabel("Yas")
    plt.ylabel("Kilo")
    plt.title("Kilo'nun Yaşa Göre Değişim Grafiği")
    plt.show()

def grafik_2():
    numpyDizisi1 = np.linspace(0,10,20)
    numpyDizisi2 = numpyDizisi1 ** 3

    plt.plot(numpyDizisi1,numpyDizisi2,"b*-")
    plt.show()

def grafik_3():
    numpyDizisi1 = np.linspace(0,10,20)
    numpyDizisi2 = numpyDizisi1 ** 3
    plt.subplot(1,2,1)
    plt.plot(numpyDizisi1,numpyDizisi2,"r*-")
    plt.subplot(1,2,2) # 1 sıra olacak, 2 kolon olacak, şu an 2. grafiği çiziyorum
    plt.plot(numpyDizisi2,numpyDizisi1,"g--")
    plt.show()


def grafik_4():
    numpyDizisi1 = np.linspace(0,10,20)
    numpyDizisi2 = numpyDizisi1 ** 3
    benimFigure = plt.figure()
    figureAxes = benimFigure.add_axes([0.1,0.1,0.3,0.3])
    figureAxes.plot(numpyDizisi1,numpyDizisi2,"g")
    figureAxes.set_xlabel("X Ekseni Veri İsmi")
    figureAxes.set_ylabel("Y Ekseni Veri İsmi")
    figureAxes.set_title("Grafik Başlığı")
    plt.show()

def grafik_5():

    numpyDizisi1 = np.linspace(0,10,20)
    numpyDizisi2 = numpyDizisi1 ** 3
    figure2 = plt.figure()

    eksen1 = figure2.add_axes([0.1,0.1,0.9,0.9])
    eksen2 = figure2.add_axes([0.2,0.5,0.3,0.3])

    eksen1.plot(numpyDizisi1,numpyDizisi2,"g")
    eksen1.set_xlabel("X Ekseni")
    eksen1.set_ylabel("Y Ekseni")
    eksen1.set_title("Ana Grafik Başlık")

    eksen2.plot(numpyDizisi2,numpyDizisi1,"b")
    eksen2.set_xlabel("X Ekseni Küçük")
    eksen2.set_ylabel("Y Ekseni Küçük")
    eksen2.set_title("Küçük Grafik Başlık")
    plt.show()


def grafik_6():
    numpyDizisi1 = np.linspace(0,10,20)
    numpyDizisi2 = numpyDizisi1 ** 3
    (benimFigure, benimEksenler) = plt.subplots(nrows=1,ncols=2)
    type(benimEksenler)

    for eksen in benimEksenler:
        eksen.plot(numpyDizisi1,numpyDizisi2,"g")
        eksen.set_xlabel("X Ekseni")

    plt.tight_layout()
    plt.show()

def grafik_7():
    numpyDizisi1 = np.linspace(0,10,20)
    numpyDizisi2 = numpyDizisi1 ** 3
    yeniFigur = plt.figure()

    yeniEksen = yeniFigur.add_axes([0.1,0.1,0.9,0.9])

    yeniEksen.plot(numpyDizisi1,numpyDizisi1 ** 2,label = "numpyDizisi ** 2")
    yeniEksen.plot(numpyDizisi1, numpyDizisi1 ** 3, label= "numpyDizisi **3 ")
    yeniEksen.legend(loc=6)
    # yeniFigur.savefig("benimfigur.png", dpi=200)
    plt.show()




