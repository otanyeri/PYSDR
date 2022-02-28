import numpy as np
import math
import tkinter
from tkinter import messagebox
from pylab import *
from rtlsdr import *
from tkinter import *
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import numpy as np

window = Tk()
globalfrequency = None
globalamplitude = None
globalfrequencyCount = 0
try:
    sdr = RtlSdr()
except:
    messagebox.showerror(title="Error!", message="SDR Radio not Present")
    exit()

"""" TKinter GUI
window.title("SDR SI")
window.geometry("240x160")
lblTFStart =tkinter.Label(window,text="Fstart(MHz)", relief=RAISED)
TFStart = tkinter.Entry(window)
TFStart.insert(END, "330")

lblTFStop =tkinter.Label(window, text="Fstop(MHz)",relief=RAISED)
TFStop = tkinter.Entry(window)
TFStop.insert(END,"332")
"""

def doIt():
    global globalfrequency
    global globalamplitude
    global globalfrequencyCount
    getFreqs()
    fsta= fstart
    fsto= fstop
    N=(fsto-fsta)
    farray = np.linspace(fsta,fsto,int(N))
    globalfrequencyCount =0
    for f in farray:
        conf(f)
        a,f = getData()
        if globalfrequencyCount ==0:
            globalfrequency = f
            globalamplitude = a
            globalfrequencyCount= globalfrequencyCount+1
        else:
            for elements in range(len(f)):

                if max(globalfrequency) < f[elements]:
                    globalfrequency = np.append(globalfrequency,f[elements])
                    globalamplitude = np.append(globalamplitude,a[elements])

    for i in range(len(globalamplitude)):
        globalamplitude[i]=10*math.log10(globalamplitude[i])
    plt.clf()
    plt.plot(globalfrequency,(globalamplitude))
    plt.ylabel('some numbers')
    plt.show()
    #f = numpy

def fancyPrint(title, text):
    input = text
    print("========="+str(title)+"=========")
    print(str(input))
    print("==================")

# configure device
def conf(fc):
    f=fc
    print ("center frequency "+ str(int(f)))
    sdr.sample_rate = 2.4e6
    setfreq= f
    sdr.center_freq = f*1000000
    sdr.gain = "auto"
def getData():
    samples = sdr.read_samples(256*1024)
    #sdr.close()
    #print("Samples Read")
    #print("=============")
    #print(samples)
    # use matplotlib to estimate and plot the PSD
    [a,f] = psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
    #xlabel('Frequency (MHz)')
    #ylabel('Relative power (dB)')
    #print ("amps ")
    #printLine()
    #print(str(a))
    #print("freqs ")
    #printLine()
    #print(str(f))
    return a,f
def printLine():
    print("===============")
""" Tkinter GUI pack
lblTFStart.pack()
TFStart.pack()
lblTFStop.pack()
TFStop.pack()
B = tkinter.Button(window,text="Do It", command=doIt)
B.pack()
"""
fstart =100
fstop =100
def getFreqs():
    global fstart
    global fstop
    print("Started Working on it!")
    fstart = int(TFStart.get())
    print("Fstart ==========" +str(fstart))
    fstop= int(TFStop.get())
    print("Fstop =========="+str(fstop))
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("UI.ui", self)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()
    """"
    scene = QtWidgets.QGraphicsScene()
    view = QtWidgets.QGraphicsView(scene)

    figure = Figure()
    axes = figure.gca()
    axes.set_title("My Plot")
    x = np.linspace(1, 10)
    y = np.linspace(1, 10)
    y1 = np.linspace(11, 20)
    axes.plot(x, y, "-k", label="first one")
    axes.plot(x, y1, "-b", label="second one")
    axes.legend()
    axes.grid(True)

    canvas = FigureCanvas(figure)
    proxy_widget = scene.addWidget(canvas)
    # or
    # proxy_widget = QtWidgets.QGraphicsProxyWidget()
    # proxy_widget.setWidget(canvas)
    # scene.addItem(proxy_widget)

    view.resize(800, 600)
    view.show()
    """
    sys.exit(app.exec_())

