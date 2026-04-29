"""
Spectrum Analyzer v1
Function : Generate sine signal -> Add noise -> FFT analysis -> Save results
"""

import os
from signal_generator import generator_sine_wave
from noise_utils import add_awgn,calculate_mse,calculate_snr
from fft_utils import compute_spectrum,find_peak_frequency
from save_utils import save_signal_to_csv,save_plot

#====================== User Parameters =======================
#modify these values to test different scenarios
FREQUENCY = 50     #Signal frequency (Hz）
DURATION= 1       #Signal duration (Seconds)
SAMPLING_RATE= 1000       #Sampling rate (Hz)
SNR_DB = 10       #Signal-to-Noise Ratio（dB)

#Output file names
OUTPUT_CSV = "output/signal_data.csv"
OUTPUT_PLOT = "output/spectrum_analysis.png"

#====================== Main program ========================
def main():
    print("="*50)
    print("Spectrum Analyzer v1")
    print("="*50)

    #1.Generate clean signal
    print(f"\n[1/6] Generating signal...")
    print(f"    Frequency:{FREQUENCY} Hz")
    print(f"    Duration:{DURATION} Seconds ")
    print(f"    Sampling rate:{SAMPLING_RATE}")
    t,clean_signal = generator_sine_wave(FREQUENCY,DURATION,SAMPLING_RATE)
    print(f"    Signal length:{len(clean_signal)} samples")

    #2.Add AWGN noise
    print(f"\n[2/6] Adding AWGN noise...")
    print(f"    Target SNR:{SNR_DB} dB")
    noisy_signal,noise,actual_snr = add_awgn(clean_signal,SNR_DB)
    print(f"    Actual SNR:{actual_snr:.2f} dB")

    #3.Calculate evaluation metrics
    print(f"\n[3/6]Calculating metrics...")
    mes = calculate_mse(clean_signal,noisy_signal)
    snr = calculate_snr(clean_signal,noisy_signal)
    print(f"    MES:{mes:.6f}")
    print(f"    SNR:{snr:.2f}")

    #4.Perform FFT analysis
    print(f"\n[4/6]Performing FFT analysis...")
    frequencies,magnitude = compute_spectrum(noisy_signal,SAMPLING_RATE)
    peak_freq,peak_mag = find_peak_frequency(frequencies,magnitude)
    print(f"    Detected peak frequencies:{peak_freq:.2f}")
    print(f"    Peak magnitude:{peak_mag:.4f}")

    #5.Save data to CSV
    print(f"\n[5/6]Saving data...")
    os.makedirs("output",exist_ok=True)
    save_signal_to_csv(t,noisy_signal,OUTPUT_CSV)

    #6.Generate and save plot
    print(f"\n[6/6]Generating plots")
    save_plot(t,clean_signal,noisy_signal,frequencies,magnitude,peak_freq,SNR_DB,OUTPUT_PLOT)

    print("\n" + "=" * 50)
    print("GOOD! Analysis complete!")
    print(f"    Data file:{OUTPUT_CSV}")
    print(f"    Plot file:{OUTPUT_PLOT}")
    print("="*50)

if __name__ == "__main__":
    main()












