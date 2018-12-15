import csv
import os
from sys import argv

import matplotlib.pyplot as plt
import numpy as np
from numpy import array
from numpy.fft import fft

if len(argv) < 1:
    print("Input file")
    exit(1)
if not os.path.isfile(argv[1]):
    print(f"{argv[1]} is not a file, exiting...")
    exit(1)
t, x, noise = range(0, 8192), [], []
amp_rel = 10 ** (8 / 20)
with open(argv[1]) as input1, open(argv[2]) as input2:
    for row in csv.reader(input1, delimiter="\t"):
        x.append(float(row[1]))
    for row in csv.reader(input2, delimiter="\t"):
        noise.append(float(row[1]) / amp_rel)

signal_trans = array(fft(x, 8192))
noise_trans = array(fft(noise, 8192))
sum_trans = array(fft(np.sum([x, noise], 0), 8192))
abs_signal_trans, abs_noise_trans, abs_sum_trans = array(np.abs(signal_trans)), array(np.abs(noise_trans)), \
                                                   array(np.abs(sum_trans))
_, ax = plt.subplots()
ax.set(xlabel="отсчёты", ylabel="амплитуда", title="Fourier")
plt.plot(t, abs_signal_trans)
plt.plot(t, abs_noise_trans)
plt.plot(t, abs_sum_trans, alpha=0.4)
plt.legend(["БПФ сигнала", "БПФ шума", "БПФ суммы"])
plt.show()

t_max = 0
for i in range(1, 8192):
    if abs_signal_trans[i] - abs_signal_trans[t_max] > 0.00000005:
        t_max = i
print(f"Signal frequency is {t_max * 100_000 / 8192}")

print(f"SNR is {np.sum(array(abs_signal_trans[:4096]) ** 2) / np.sum(array(abs_noise_trans[:4096]) ** 2)}")
