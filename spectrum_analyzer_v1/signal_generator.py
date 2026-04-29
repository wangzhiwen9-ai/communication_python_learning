import numpy as np

def generator_sine_wave(frequency,duration,sampling_rate):
    """
    Generate sine wave signal

    :param frequency: Signal frequency (Hz)
    :param duration: Signal duration (seconds)
    :param sampling_rate: Sampling rate (Hz)
    :return:
         t:Times axis array
         signal:sine wave signal
    """
    t = np.linspace(0,duration,int(duration*sampling_rate),endpoint=False)
    signal = np.sin(2*np.pi*frequency*t)
    return t,signal
if __name__ == "__main__":
    t,sig = generator_sine_wave(50,1,100)
    print(f"Generated signal:{len(sig)},time range:[{t[0]:.3f},{t[-1]:.3f}]")