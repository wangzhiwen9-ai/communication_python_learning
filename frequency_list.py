#Basic list operation for frequency values
freqs = []
#Add 5 frequency values
freqs.append(100)
freqs.append(200)
freqs.append(300)
freqs.append(400)
freqs.append(500)

print("All frequency values (Hz):")
for f in freqs:
    print(f"-{f} Hz")

print(f'\nTotal number of frequencies :{len(freqs)}')
