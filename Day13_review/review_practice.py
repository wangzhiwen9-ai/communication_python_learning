import numpy as np
import matplotlib.pyplot as plt

#Review Generate signal -> Add noise -> FFT ->Save file
freq = 5
duration = 1
fs = 1000
SNR_dB = 10

t = np.linspace(0,duration, int(duration*fs))
signal = np.sin(2*np.pi*freq*t)

#Add Gaussian noise
signal_power = np.mean(signal**2)
noise_power = signal_power/10**(SNR_dB/10)
noise = np.sqrt(noise_power)*np.random.randn(len(signal))
noisy = signal + noise

#Fast Fourier Transform
fft_result = np.fft.fft(noise)
freq = np.fft.fftfreq(len(noisy),d=1/fs)
magnitude = np.abs(fft_result)[:len(noisy)//2]

#Save date to file
with open("day13_review_signal.txt","w")as f:
    for i in range(100):#Only save the first 100 sampling points
        f.write(f"{t[i]},{noisy[i]}")
print("Review finished ! File saved successfully:day13_review_signal.txt")



