import numpy as np
import matplotlib.pyplot as plt

#parameters
freq = 5
fs = 200
duration = 1

#Time axis
t = np.linspace(0,duration,int(fs*duration))
signal =np.sin(2*np.pi*freq*t)

#FFT
fft_result = np.fft.fft(signal)
n = len(signal)
freqs = np.fft.fftfreq(n,d=1/fs)

#Take positive frequencies only
half_n = n//2
pos_freqs = freqs[:half_n]
magnitude = np.abs(fft_result)[:half_n]

#Plot
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(t,signal)
plt.title(f"Time Domain:{freq}Hz Sine Wave")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(pos_freqs,magnitude)
plt.title("Frequency Domain (Magnitude Spectrum)")
plt.xlabel("Frequency(Hz)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.tight_layout()
plt.show()