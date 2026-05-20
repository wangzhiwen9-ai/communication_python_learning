"""BPSK (Binary Phase Shift Keying) Modulation
-Generate random bit stream
-Modulate bits onto carrier using phase shift (0° for bit 1,180° for bit 0)
-Visualize bit stream,reference carrier,and BPSK signal
-Observe phase transitions at bit boundaries
-Compare BPSK with ASK and FSK
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_bits(num_bits,seed=42):
    """Generate random bit stream """
    np.random.seed(seed)
    return np.random.randint(0,2,num_bits)

def bpsk_modulate(bits,bit_rate,carrier_freq,sampling_rate,duration):
    """
    BPSK Modulation
    :param bits: Bit stream (list or array of 0s and 1s)
    :param bit_rate: Bit per seconds
    :param carrier_freq: Carrier frequency
    :param sampling_rate: Sampling rate
    :param duration: Signal duration (seconds)
    :return:
        t: Time
        bpsk_signal: BPSK modulated signal
        carrier: Reference carrier
    """
    t = np.linspace(0,duration,int(sampling_rate*duration),endpoint=False)
    carrier = np.sin(2*np.pi*carrier_freq*t)

    bpsk_signal = np.zeros_like(t)
    samples_per_bit = int(sampling_rate/bit_rate)

    for i,bit in enumerate(bits):
        start = i * samples_per_bit
        end = (i+1) * samples_per_bit
        if bit == 1:
            bpsk_signal[start:end] = carrier[start:end]  # 0° phase
        else:
            bpsk_signal[start:end] = -carrier[start:end]  #180 phase

    return t,bpsk_signal,carrier

def plot_bpsk(bits,t,bpsk_signal,carrier,bit_rate,carrier_freq,sampling_rate):
     """Plot BPSK modulation signal """
     plt.figure(figsize=(14,12))

     #Bit stream
     plt.subplot(4,1,1)
     bit_waveform = np.repeat(bits,20)
     plt.plot(np.linspace(0,len(bits)/bit_rate,len(bit_waveform)),bit_waveform,drawstyle="steps-post")
     plt.title("Bit stream")
     plt.xlabel("Time(s)")
     plt.ylabel("Amplitude")
     plt.ylim(-0.5,1.5)
     plt.grid(True)

     #Referency carrier
     plt.subplot(4,1,2)
     show_samples = int(0.3*sampling_rate)
     plt.plot(t[:show_samples],carrier[:show_samples])
     plt.title(f"Reference Carrier({carrier_freq} Hz)")
     plt.xlabel("Time(s)")
     plt.ylabel("Amplitude")
     plt.grid(True)

     #BASK signal
     plt.subplot(4,1,3)
     show_samples = int(0.5*sampling_rate)
     plt.plot(t[:show_samples],bpsk_signal[:show_samples])
     for i in range(int(0.5*bit_rate)+1):
         plt.axvline(x=i / bit_rate,color="r",linestyle='--',alpha=0.5,linewidth=0.5)
     plt.title("BPSK Modulation Signal")
     plt.xlabel("Time(s)")
     plt.ylabel("Amplitude")
     plt.grid(True)

     # Phase transition
     plt.subplot(4,1,4)
     samples_per_bit = int(sampling_rate/bit_rate)
     boundary_samples = samples_per_bit
     show_range = slice(boundary_samples-50,boundary_samples+50)
     plt.plot(t[show_range],bpsk_signal[show_range],"b-o",markersize = 3)
     plt.axvline(x=t[samples_per_bit],color="r",linestyle="--",linewidth=2,label="Bit Boundary")
     plt.title("Phase Transition at Bit Boundary (180 Phase Jump")
     plt.xlabel("Time(s")
     plt.ylabel("Amplitude")
     plt.legend()
     plt.grid(True)

     plt.tight_layout()
     plt.show()

def demodulate_bpsk(bpsk_signal,carrier,samples_per_bit):
    """Simple BPSK demodulation using correlation """
    bits = []
    for i in range(len(bpsk_signal)//samples_per_bit):
        start =i * samples_per_bit
        end =(i + 1) * samples_per_bit
        correlation = np.sum(bpsk_signal[start:end]*carrier[start:end])
        bits.append(1 if correlation>0 else 0)
    return bits

#Main execution
if __name__ == "__main__":
    #Paramaters
    BIT_RATE = 10
    CARRIER_FREQ = 100
    SAMPLING_RATE = 8000
    DURATION = 1

    #Generate bits
    bits = generate_bits(int(BIT_RATE*DURATION))
    print(f"Bit stream: {bits}")

    #Modulation
    t,bpsk_signal,carrier = bpsk_modulate(bits,BIT_RATE,CARRIER_FREQ,SAMPLING_RATE,DURATION)

    #Plot
    plot_bpsk(bits,t,bpsk_signal,carrier,BIT_RATE,CARRIER_FREQ,SAMPLING_RATE)

    #Verify demodulation
    samples_per_bit = int(SAMPLING_RATE/BIT_RATE)
    detected_bits = demodulate_bpsk(bpsk_signal,carrier,samples_per_bit)

    print(f"Original bits:{bits[:20]}")
    print(f"Detected bits:{detected_bits[:20]}")
    print(f"Correct:{np.array_equal(bits[:20],detected_bits[:20])}")


















































