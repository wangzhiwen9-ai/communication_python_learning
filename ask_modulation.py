"""
ASK (Amplitude shift Keying) Modulation
- Generate random bit stream
- Modulate bits onto a carrier wave using amplitude variation
- Visualize bit stream,carrier,and modulated signal
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_bits(num_bits,seed=42):
    """Generate random bit stream"""
    np.random.seed(seed)
    return np.random.randint(0,2,num_bits)

def ask_modulate(bits,bit_rate,carrier_freq,sampling_rate,duration):
    """
    ASK Modulation
    :param bits: bit streams (list or array of 0s and 1s)
    :param bit_rate: Bits per second
    :param carrier_freq: Carrier frequency (Hz)
    :param sampling_rate: Sampling rate (Hz)
    :param duration: signal duration (seconds)
    :return:
        t:Time axis
        ask_signal:ASK modulated signal
        carrier:Carrier wave
    """
    t = np.linspace(0,duration,int(sampling_rate*duration),endpoint=False)
    carrier = np.sin(2*np.pi*carrier_freq*t)

    ask_signal = np.zeros_like(t)
    samples_per_bit = int(sampling_rate/bit_rate)

    for i,bit in enumerate(bits):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit
        if bit == 1:
            ask_signal[start:end] = carrier[start:end]

    return t,ask_signal,carrier

def plot_ask(bits,t,carrier,ask_signal,sampling_rate,bit_rate):
    """Plot ASK modulation results"""

    # Bit stream
    plt.subplot(4,1,1)
    bit_duration = 1 / bit_rate
    bit_time = np.linspace(0,len(bits)*bit_duration,len(bits)*10)
    bit_waveform = np.repeat(bits,10)
    plt.plot(np.linspace(0,len(bits)*bit_duration,len(bit_waveform)),bit_waveform,drawstyle='steps-post')
    plt.title("Bit Stream")
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude")
    plt.ylim(-0.5,1.5)
    plt.grid(True)

    #Carrier (first 0.2 seconds)
    plt.subplot(4,1,2)
    show_samples = int(0.2*sampling_rate)
    plt.plot(t[:show_samples],carrier[:show_samples])
    plt.title("Carrier signal")
    plt.xlabel("Time（s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    #ASK signal (first 0.5 seconds)
    plt.subplot(4,1,3)
    show_samples = int(0.5*sampling_rate)
    plt.plot(t[:show_samples],ask_signal[:show_samples])
    plt.title("ASK Modulation Signal")
    plt.xlabel("Time（s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    #ASK with bit boundaries
    plt.subplot(4,1,4)
    plt.plot(t[:show_samples],ask_signal[:show_samples])
    for i in range(len(bits) + 1):
        plt.axvline(x=i/bit_rate,color ="r",linestyle="--",alpha=0.5,linewidth=0.5)
    plt.title("ASK Signal with Bit Boundaries")
    plt.xlabel("Time（s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ =="__main__":
    #parameters
    BIT_RATE = 10
    CARRIER_FREQ = 100
    SAMPLING_RATE = 8000
    DURATION = 1

    #Generate bits
    bits = generate_bits(int(BIT_RATE*DURATION))
    print(f"Bit steam:{bits}")

    #Modulate
    t,ask_signal,carrier=ask_modulate(bits,BIT_RATE,CARRIER_FREQ,SAMPLING_RATE,DURATION)

    #Plot
    plot_ask(bits,t,carrier,ask_signal,SAMPLING_RATE,BIT_RATE)







