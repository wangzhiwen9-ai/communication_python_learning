#Save and load signal data to CSV
import numpy as np

from signal_generator_v2 import generate_sine

#Generate test signal
t,sig = generate_sine(freq=50,duration=1,fs=1000)
#Stack time and signal into 2D array
data = np.stack([t,sig],axis=1)

#Save to CSV
np.savetxt("signal_data.csv",data,delimiter=",",header="time(s),amplitude")
print("Signal saved to signal_data.csv")

#Load from CSV
load_data = np.loadtxt("signal_data.csv",delimiter=",",skiprows=1)
print(f"Loaded data shape {load_data.shape}")
print(f"First 5 rows:\n{load_data[:5]}")