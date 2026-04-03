#Wrap sine signal into function

import numpy as np
import matplotlib.pyplot as plt

def generate_sine(freq,duration,fs):
    """

    Generate sine wave signal
    :param freq:Signal frequency(Hz)
    :param duration:Signal duration(s)
    :param fs:Sampling rate(Hz)
    :return:time sequence,signal sequence

    """
    t = np.linspace(0,duration,int(fs*duration))
    sig = np.sin(2*np.pi*freq*t)
    return t,sig

#Text function
t,sig = generate_sine(freq=100,duration=1,fs=1000)
plt.figure(figsize=(10,4))
plt.plot(t,sig)
plt.title("100Hz Sine Signal(Function Version")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()