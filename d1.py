import numpy as np
import tkinter
from pylab import *
from rtlsdr import *
from tkinter import *

window = Tk()
try:
    sdr = RtlSdr()
except:
     tkinter.messagebox.showerror(title="Error!", message="SDR Radio not Present")
     exit()


window.title("SDR SI")
window.geometry("240x160")
lblTFStart =tkinter.Label(window,text="Fstart(MHz)", relief=RAISED)
TFStart = tkinter.Entry(window)
TFStart.insert(END, "410")

lblTFStop =tkinter.Label(window, text="Fstop(MHz)",relief=RAISED)
TFStop = tkinter.Entry(window)
TFStop.insert(END,"420")


def doIt():
    getFreqs()
    fsta= fstart
    fsto= fstop
    N=(fsto-fsta)/2
    farray = np.linspace(fsta,fsto,N)
    print(farray)
    conf(f)
    getData()
    f = numpy


# configure device
def conf(fc):
    f=fc
    sdr.sample_rate = 2.4e6
    sdr.center_freq = fc*1000000
    sdr.gain = "auto"
def getData():
    samples = sdr.read_samples(256*1024)
    sdr.close()
    # use matplotlib to estimate and plot the PSD
    psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
    xlabel('Frequency (MHz)')
    ylabel('Relative power (dB)')
    show()

lblTFStart.pack()
TFStart.pack()
lblTFStop.pack()
TFStop.pack()
B = tkinter.Button(window,text="Do It", command=doIt)
B.pack()

fstart =100
fstop =100
def getFreqs():
    global fstart
    global fstop
    print("here!!")
    fstart = int(TFStart.get())
    print(fstart)
    fstop= int(TFStop.get())
    print(fstop)
window.mainloop()
