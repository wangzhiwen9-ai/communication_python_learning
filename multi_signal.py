#Function with default parameters & multi-signal plot

import numpy as np
import matplotlib.pyplot as plt

def generate_sine(freq,duration=1,fs=1000):
    """
    Generate sine wave with default duration=1,fs=1000
    """
    t = np.linspace(0,duration,int(fs*duration))
    return t,np.sin(2*np.pi*freq*t)

#Plot 3 different frequency signals
plt.figure(figsize=(10,6))
freqs = [50,100,200]
for f in freqs:
    t,sig = generate_sine(f)
    plt.plot(t,sig,label=f"{f} Hz",linewidth=1.5)

plt.title("Multi-frequency Sine Signal")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.savefig("multi_signal.png",dpi=300,bbox_inches="tight")
plt.show()
