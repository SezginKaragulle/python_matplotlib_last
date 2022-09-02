import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(0,10,20)
numpyDizisi2 = numpyDizisi1 ** 2

def grafik1():
    numpyDizisi1 = np.linspace(0,10,20)
    numpyDizisi2 = numpyDizisi1 ** 2
    (benimFigur, benimEksen) = plt.subplots()
    benimEksen.plot(numpyDizisi1, numpyDizisi2, color="#3A95A8",alpha=0.3)
    benimEksen.plot(numpyDizisi2,numpyDizisi1,color="#C96F23")
    plt.show()

def grafik2():
    numpyDizisi1 = np.linspace(0,10,20)
    numpyDizisi2 = numpyDizisi1 ** 2
    (yeniFigur, yeniEksen) = plt.subplots()
    yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 2, color="blue", linewidth = 1.0)
    yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 3, color ="yellow", linewidth = 1.0)

    yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 4, color = "#C96F23", linestyle = "-.")
    yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 5, color = "#C96F23", linestyle = ":")
    yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 6, color = "#C96F23", linestyle = "--")

    yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 7, color = "#000000", linestyle = "--", marker = "o",markersize = 8, markerfacecolor="red")
    yeniEksen.plot(numpyDizisi1, numpyDizisi1 + 8, color = "#000000", linestyle = "--", marker = "+",markersize = 4)
    plt.show()

def grafik3():
    plt.scatter(numpyDizisi1,numpyDizisi2)
    plt.show()

def grafik4():
    yeniDizi = np.random.randint(0,100,50)
    plt.hist(yeniDizi)
    plt.show()

def grafik5():
    yeniDizi = np.random.randint(0,100,50)
    plt.boxplot(yeniDizi*2)
    plt.show()

