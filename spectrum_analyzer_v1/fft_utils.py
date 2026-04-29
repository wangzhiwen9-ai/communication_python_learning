import numpy as np

def compute_spectrum(signal,sampling_rate):
    """


    :param signal: Input signal
    :param sampling_rate: Sampling rate (Hz)
    :return:
         frequencies:Frequency axis array (positive frequencies only)
         magnitude:Magnitude spectrum ( positive frequencies only)
    """
    n = len(signal)
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(n,d=1/sampling_rate)

    #Take only positive frequencies
    half_n = n//2
    frequencies = freqs[:half_n]
    magnitude = np.abs(fft_result)[:half_n]

    return frequencies ,magnitude

def find_peak_frequency(frequencies,magnitude):

    """
    Find the dominant frequency peak in the spectrum
    :return:
         peak_freq:Frequency of the peak
         peak_mag:Magnitude of the peak
    """
    peak_idx = np.argmax(magnitude)
    return frequencies[peak_idx],magnitude[peak_idx]

if __name__ == "__main__":
    t = np.linspace(0,1,1000)
    test_signal = np.sin(2*np.pi*50*t)
    freqs,mag = compute_spectrum(test_signal,1000)
    peak_freq,peak_mag = find_peak_frequency(freqs,mag)
    print(f"Test:detected peak frequency:{peak_freq:.2f}Hz")