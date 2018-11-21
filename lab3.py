import os
import sys

import matplotlib.pyplot as plt
import numpy as np


def plot_graph(signal_noise_sum, part):
    if not 0.0 < part <= 100.0:
        print("Invalid percentage")
        exit(1)
    num_elems = int(np.floor(10000 * part / 100))
    t = np.arange(0.0, 0.1 * part / 100, 0.00001)
    fig, ax = plt.subplots()
    plt.plot(t, signal_noise_sum[0:num_elems])
    ax.set(xlabel="time (ms)", ylabel="voltage (V)", title="Signal + noise")
    plt.show()


def read_csv(signal, noise):
    signal_file = None
    noise_file = None
    if not os.path.isfile(signal):
        print(f"{signal} is not a file, exiting...")
        exit(1)
    else:
        signal_file = open(signal)

    if not os.path.isfile(noise):
        print(f"{noise} is not a file, exiting...")
        exit(1)
    else:
        noise_file = open(noise)

    amp_rel = 10 ** (8 / 20)
    signal_values = list(map(lambda line: float(line.split("\t")[1]), signal_file.readlines()))
    noise_values = list(map(lambda line: float(line.split("\t")[1]) / amp_rel, noise_file.readlines()))

    return np.sum([signal_values, noise_values], 0)


if len(sys.argv) < 4:
    print("Usage: python3 lab3.py <signal_file> <noise_file> <part_to_show>")
    exit(1)
plot_graph(read_csv(sys.argv[1], sys.argv[2]), float(sys.argv[3]))
