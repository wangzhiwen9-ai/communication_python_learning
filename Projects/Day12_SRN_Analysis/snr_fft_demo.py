import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import title

#Paramater Setting
freq = 50
fs = 1000
duration = 1
SNR_dB = 10

#Generate clean signal
t = np.linspace(0,duration,int(duration*fs),endpoint=False)
clean_signal = np.sin(2*np.pi*freq*t)


#===============Add Gaussian White Noise===============
#Calculate signal power (mean square value)
signal_power = np.mean(clean_signal**2)

#Calculate noise power according to formula
noise_power = signal_power/10**(SNR_dB/10)

#Generate Gaussian white noise
np.random.seed(42)
noise = np.sqrt(noise_power)*np.random.randn(len(clean_signal))

#Noise signal synthesis
noise_signal = clean_signal+noise

#Verify actual SNR
actual_noise_power = np.mean(noise**2)
actual_snr = 10 *np.log10(signal_power/actual_noise_power)
print(f"Target SNR: {SNR_dB} dB")
print(f"Actual SNR: {actual_snr:.2f} dB")
print(f"Signal Power :{signal_power:.4f}")
print(f"Noise Power :{noise_power:.4f}")


#==============Time-domain Waveform Plotting===============
plt.figure(figsize=(12,8))

#Time-domain - Clean Signal
plt.subplot(2,2,1)
plt.plot(t[:200],clean_signal[:200])
plt.title(f'Clean Signal(Time Domain) - {freq}Hz Sine Wave')
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.grid(True)

#Time-domain - Noise Signal
plt.subplot(2,2,2)
plt.plot(t[:200],noise_signal[:200])
plt.title(f'Noise Signal(Time Domain) - SNR={SNR_dB} dB')
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.grid(True)

#===============Frequency Spectrum Plotting==================
def plot_spectrum(signal,FS,ax,title):
    """Plot frequency spectrum on specified axes"""
    n = len(signal)
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(n,1/FS)

    #Keep only positive frequency components
    half_n = n//2
    pos_freqs = freqs[:half_n]
    magnitude = np.abs(fft_result)[:half_n]

    ax.plot(pos_freqs,magnitude)
    ax.set_title(title)
    ax.set_xlabel("Frequency(Hz)")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    ax.set_xlim(0,200)#Focus on 0~200Hz,observe 50Hz component

#Spectrum - Clean Signal
ax1 = plt.subplot(2,2,3)
plot_spectrum(signal=clean_signal,FS=fs,ax=ax1,title=f"Clean Signal Spectrum - {freq}Hz Signal Tone")

#Specteum - Noisy Signal
ax2 = plt.subplot(2,2,4)
plot_spectrum(signal=noise_signal,FS=fs,ax=ax2,title=f"Noise Signal Spectrum - Raised Noise Floor")

plt.tight_layout()
plt.show()







