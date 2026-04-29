# Spectrum Analyzer v1

A python tool for signal generation,AWGN noise addition ,and frequency spectrum analysis.

## Features

- Generate sine wave with configurable frequency,duration,sampling rate
- Add AWGN (Additive While Gaussian Noise) whit specified SNR (dB)
- Perform FFT and display magnitude spectrum 
- Automatically detect dominant frequency peak
- Save signal data to CSV file
- Export time-domain and frequency-domain plots

![Spectrum Analysis](output/spectrum_analysis.png)
 
## Installation 
'''bash

pip install numpy matplotlib

## Usage 
- Run the main program 

'''bash

python spectrum_analyzer.py

- Modify parameters in spectrum_analyzer.py

FREQUENCY = 50     #Signal frequency (Hz）

DURATION= 1       #Signal duration (Seconds)

SAMPLING_RATE= 1000       #Sampling rate (Hz)

SNR_DB = 10       #Signal-to-Noise Ratio（dB)

# Output 
- output/signal_date.csv - Time and amplitude data 
- output/spectrum_analysis.png - Visualization plots (clean/noisy clean,spectrum,analysis report)

# Project Structure 
spectrum_analyzer_v1/

|-- signal_generator.py    #Sine wave generation

|-- noise_utils.py     #AWGN and metrics (MSE,SNR)

|-- fft_utils.py    #FFT and peak detection

|-- save_utils.py   # CSV export and plotting 

|-- spectrum_analyzer.py   #Main entry point 

|--__init__.py

|__output/  #Generated files 

# Sample Output 
****============**===============**=======================
Spectrum Analyzer v1
==================================================****

[1/6] Generating signal...
    Frequency:50 Hz
    Duration:1 Seconds 
    Sampling rate:1000
    Signal length:1000 samples

[2/6] Adding AWGN noise...
    Target SNR:10 dB
    Actual SNR:10.19 dB

[3/6]Calculating metrics...
    MES:0.047914
    SNR:10.19

[4/6]Performing FFT analysis...
    Detected peak frequencies:50.00
    Peak magnitude:497.0980

[5/6]Saving data...
Data saved: output/signal_data.csv

[6/6]Generating plots
Plot saved: output/spectrum_analysis.png

**==================================================**
GOOD! Analysis complete!
    Data file:output/signal_data.csv
    Plot file:output/spectrum_analysis.png
**==================================================**

# Dependencies 
- Python 3.8+
- numpy
- matplotlib

# License
Educational use only.