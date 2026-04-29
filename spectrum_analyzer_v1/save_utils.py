import os
import numpy as np
import matplotlib.pyplot as plt

def save_signal_to_csv(t, signal, filename):
    """
    Save signal data to CSV file

    Args:
        t: Time axis
        signal: Signal data
        filename: Output file path
    """
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    data = np.column_stack((t, signal))
    np.savetxt(filename, data, delimiter=',', header='time,signal', comments='')
    print(f"Data saved: {filename}")

def save_plot(t, clean_signal, noisy_signal, frequencies, magnitude,
              peak_freq, snr_db, filename):
    """
    Generate and save time-domain and frequency-domain plots
    """
    plt.figure(figsize=(14, 10))

    # Time domain - clean signal
    plt.subplot(2, 2, 1)
    plt.plot(t[:200], clean_signal[:200])
    plt.title('Clean Signal (Time Domain)')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Time domain - noisy signal
    plt.subplot(2, 2, 2)
    plt.plot(t[:200], noisy_signal[:200])
    plt.title(f'Noisy Signal (Time Domain) - SNR = {snr_db} dB')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Frequency domain - spectrum
    plt.subplot(2, 2, 3)
    plt.plot(frequencies, magnitude)
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.xlim(0, 200)

    # Annotate the peak
    plt.annotate(f'{peak_freq:.1f} Hz',
                 xy=(peak_freq, np.max(magnitude)),
                 xytext=(peak_freq, np.max(magnitude) * 0.8),
                 arrowprops=dict(arrowstyle='->'))

    # Info panel
    plt.subplot(2, 2, 4)
    plt.axis('off')
    info_text = f"""
    Spectrum Analyzer v1 - Results

    === Parameters ===
    Detected frequency: {peak_freq:.1f} Hz
    Sampling rate: {len(t)/t[-1]:.0f} Hz
    Duration: {t[-1]:.2f} sec
    SNR: {snr_db} dB

    === Detection ===
    Peak frequency: {peak_freq:.2f} Hz
    Peak magnitude: {np.max(magnitude):.3f}

    === Output ===
    Plot saved: {filename}
    """
    plt.text(0.1, 0.5, info_text, fontsize=12, verticalalignment='center')
    plt.title('Analysis Report')

    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.show()
    print(f"Plot saved: {filename}")


















