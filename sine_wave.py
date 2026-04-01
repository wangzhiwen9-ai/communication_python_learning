# Day6: Draw first sine wave signal
import numpy as np
import matplotlib.pyplot as plt

# Generate time sequence and sine wave
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Plot and save figure
plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Basic Sine Wave")
plt.grid(True)
plt.savefig("sine_wave.png", dpi=300, bbox_inches="tight")
plt.show()