import numpy as np

def add_awgn(signal,snr_db,seed=42):
    """
    Add Additive white Gaussian Noise (AWGN)
    :param signal: Input signal
    :param snr_db: Signal-to-Noise Ratio (dB)
    :param seed: Random seed for reproducibility
    :return:
         noisy_signal : Signal with added noise
         noise : The noise itself
         actual_snr : Actual SNR after add noise
    """
    if seed is not None:
        np.random.seed(seed)

    signal_power = np.mean(signal**2)
    noise_power = signal_power/(10**(snr_db/10))
    noise = np.sqrt(noise_power)*np.random.randn(len(signal))
    noisy_signal = signal + noise

    actual_noise_power = np.mean(noise**2)
    actual_snr = 10*np.log10(signal_power/actual_noise_power)

    return noisy_signal,noise,actual_snr

def calculate_mse(original,denoised):
    """Calculate Mean Squared Error(MSE)"""
    return np.mean((original - denoised)**2)

def calculate_snr(original,noisy):
    """Calculate Signal-to-Noise Ratio (SNR) in dB"""
    signal_power = np.mean(original**2)
    noise_power = np.mean((original-noisy)**2)
    if noise_power == 0:
        return float('inf')
    return 10*np.log10(signal_power/noise_power)

if __name__ =="__main__":
    test_signal = np.array([1.0,2.0,3.0,4.0,5.0])
    noisy,_,actual_snr=add_awgn(test_signal,snr_db=20)
    print(f"Test:target SNR=20dB,actual_snr:{actual_snr:.2f}dB")















