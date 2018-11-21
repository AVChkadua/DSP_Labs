import os
import sys

import matplotlib.pyplot as plt
import numpy as np

import commons


def signal(x):
    return 1.3 * np.cos(2 * np.pi * 26885.46875 * x + np.radians(120))


def plot_graph(part):
    if not 0.0 < part <= 100.0:
        print("Invalid percentage")
        exit(1)
    t = np.arange(0.0, 0.1 * part / 100, 0.00001)
    func = 1.3 * np.cos(2 * np.pi * 26885.46875 * t + np.radians(120))
    fig, ax = plt.subplots()
    plt.plot(t, func)
    ax.set(xlabel="time (ms)", ylabel="voltage (V)", title="Signal")
    plt.show()


def output_to_csv(filename):
    file = commons.open_file(filename)

    x_range = np.arange(0.0, 0.1, 0.00001)
    values = signal(x_range)
    for i in range(0, 10000):
        x = "{0:.5f}".format(x_range[i])
        y = "{0:.5f}".format(values[i])
        file.write(f"{x}\t{y}\n")

    mean = "{0:.5f}".format(np.mean(values))
    print(f"Mean value is {mean}")
    file.close()
    exit(0)


if len(sys.argv) < 2:
    print("Input command ('show' or 'csv')")
    exit(1)
if sys.argv[1] == "show":
    if len(sys.argv) < 3:
        print("Input the percentage of the whole time frame to generate (example: 50 will generate 50000 ms of signal)")
        exit(1)
    plot_graph(float(sys.argv[2]))
elif sys.argv[1] == "csv":
    if len(sys.argv) < 3:
        print("Input file for output")
        exit(1)
    output_to_csv(sys.argv[2])
