"""FSK (Frequency Shift Keying) Modulation
- Generate random bit stream
- Modulate bits onto carrier using different frequencies
- Visualize bit stream ,carrier ,and modulated signal
- Compare FSK vs ASK
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_bits(num_bits,seed=42):
    """Generate random bit stream"""
    np.random.seed(seed)
    return np.random.randint(0,2,num_bits)

def fsk_modulate(bits,bit_rate,f0,f1,sampling_rate,duration):
    """
    FSK Modulation

    :param bits:Bit stream (list or array of 0s and 1s)
    :param bit_rate: Bits per second
    :param f0: Frequency of bit 0 (Hz)
    :param f1: Frequency of bit 1 (Hz)
    :param sampling_rate: Sampling rate (Hz)
    :param duration: Signal duration (seconds)
    :return:
        t:Time axis
        fsk_signal:FSK modulate signal
    """

    t = np.linspace(0,duration,int(sampling_rate*duration),endpoint=False)
    fsk_signal = np.zeros_like(t)
    samples_per_bit = int(sampling_rate/bit_rate)

    for i,bit in enumerate(bits):
        start = i * samples_per_bit
        end = (i+1) *samples_per_bit
        t_segment = t[start:end] - t[start]

        if bit == 1:
            fsk_signal[start:end] = np.sin(2*np.pi*f0*t_segment)
        else:
            fsk_signal[start:end] = np.sin(2*np.pi*f1*t_segment)


    return t, fsk_signal

def plot_fsk(bits,t,fsk_signal,bit_rate,f0,f1,sampling_rate):
    """Plot FSK modulation results"""
    plt.figure(figsize=(14,10))

    # Bit stream
    plt.subplot(4,1,1)
    bit_waveform = np.repeat(bits,20)
    plt.plot(np.linspace(0,len(bits)/bit_rate,len(bit_waveform)),bit_waveform,drawstyle='steps-post')
    plt.title("Bit stream")
    plt.xlabel("Time（s)")
    plt.ylabel("Amplitude")
    plt.ylim(-0.5,1.5)
    plt.grid(True)

    # F0 carrier
    plt.subplot(4,1,2)
    show_samples = int(0.3 * sampling_rate)
    t_short = t[:show_samples]
    carrier0 = np.sin(2*np.pi*f0*t_short)
    plt.plot(t_short,carrier0)
    plt.title(f"Carrier of Bit 0 (f0={f0}Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    # F1 carrier
    plt.subplot(4,1,3)
    carrier1 = np.sin(2*np.pi*f1*t_short)
    plt.plot(t_short,carrier1)
    plt.title(f"Carrier of Bit 1 (f1={f1}Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    # FSK signal
    plt.subplot(4,1,4)
    show_samples = int(0.5 * sampling_rate)
    plt.plot(t[:show_samples],fsk_signal[:show_samples])
    for i in range(int(0.5*bit_rate)+1):
        plt.axvline(x=i / bit_rate,color="r",linestyle="--",alpha=0.5,linewidth=0.5)
    plt.title("FSK Modulated Signal")
    plt.xlabel("Time(s）")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    # parameters
    BIT_RATE = 10
    F0 = 50
    F1 = 200
    SAMPLING_RATE = 8000
    DURATION = 1

    # Generate bits
    bits = generate_bits(int(BIT_RATE*DURATION))
    print(f"Bit stream: {bits}")

    # Modulate
    t,fsk_signal = fsk_modulate(bits,BIT_RATE,F0,F1,SAMPLING_RATE,DURATION)

    # Plot
    plot_fsk(bits,t,fsk_signal,BIT_RATE,F0,F1,SAMPLING_RATE)




