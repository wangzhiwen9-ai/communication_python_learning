#condition judgment & SNR quality check
snr = int(input("Please enter SNR Value(dB):"))
if snr > 20:
    print("Signal quality :Excellent")
elif snr >= 10:
    print("Signal quality:Good")
else:
    print("signal quality:Poor")