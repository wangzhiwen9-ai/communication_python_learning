# Day7: Week1 mini project - Signal Generator v1
import numpy as np
import matplotlib.pyplot as plt

# Get user input parameters
freq = float(input("Enter signal frequency (Hz): "))
duration = float(input("Enter signal duration (s): "))
fs = float(input("Enter sampling rate (Hz): "))

# Generate time sequence and sine signal
t = np.linspace(0, duration, int(fs * duration))
sig = np.sin(2 * np.pi * freq * t)

# Plot and save figure
plt.figure(figsize=(10, 4))
plt.plot(t, sig)
plt.title(f"Sine Signal: {freq} Hz, Duration: {duration} s, Sampling Rate: {fs} Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("signal_generator_v1.png", dpi=300, bbox_inches="tight")
plt.show()