import numpy as np
import matplotlib.pyplot as plt

#Parameters

freq1 = 5
freq2 = 12
fs = 200
duration = 1

#Time axis
t = np.linspace(0,duration,int(fs*duration),endpoint=False)

#Composite signal:5Hz amplitude 1 +12Hz amplitude 0.5
signal = np.sin(2*np.pi*freq1*t)+0.5*np.sin(2*np.pi*freq2*t)

#FFT
fft_result = np.fft.fft(signal)
n = len(signal)
freqs = np.fft.fftfreq(n,d=1/fs)

#Positive frequencies only
half_n = n//2
pos_freqs = freqs[:half_n]
magnitude = np.abs(fft_result)[:half_n]

#Plot
plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
plt.plot(t,signal)
plt.title("Time Domain:5Hz+12Hz Composite")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(pos_freqs,magnitude)
plt.title("Frequency Domain (Magnitude Spectrum)")
plt.xlabel("Frequency(Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

#Annotate peaks
plt.annotate("5Hz",xy=(5,np.max(magnitude[pos_freqs==5])),xytext=(5, np.max(magnitude)*0.8),arrowprops=dict(arrowstyle="->"))
plt.annotate("12Hz",xy=(12,np.max(magnitude[pos_freqs==12])),xytext=(12, np.max(magnitude)*0.6),arrowprops=dict(arrowstyle="->"))

plt.tight_layout()
plt.show()
