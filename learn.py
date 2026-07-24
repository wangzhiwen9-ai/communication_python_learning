import numpy as np
import matplotlib.pyplot as plt

freq = 5 # Frequency of Sine wave1 and Sine wave2 (Hz)
duration = 0.5 #Signal duration (seconds)
sampling_rate = 1000 #Sampling Rate (Hz)
bit_rate = 10

bits =[1,0,1,1,0]

t1  = np.linspace(0,duration,int(duration*sampling_rate),endpoint=False)
sine_wave1 = np.sin(2*np.pi*freq*t1)

t2 = np.linspace(0,duration,int(duration*sampling_rate),endpoint=False)
sine_wave2 =np.sin(2*np.pi*freq*t2 + np.pi)

t3 = np.linspace(0,duration,int(duration*sampling_rate))
psk_signal = np.zeros_like(t3)
samples_per_bit = int(sampling_rate/bit_rate)

for bit in bits:
    if bit==1:
        psk_signal =sine_wave1
    else:
        psk_signal = sine_wave2

plt.figure(figsize=(14,10))
plt.subplot(3,1,1)
plt.plot(t1,sine_wave1)
plt.title("Sine wave1")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t2,sine_wave2)
plt.title("Sine wave2")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.subplot(3,1,3)
plt.plot(t3,psk_signal)
plt.grid(True)



