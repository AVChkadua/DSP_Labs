import os
import sys

import matplotlib.pyplot as plt
import numpy as np


def plot_graph(part):
    if not 0.0 < part <= 100.0:
        print("Invalid percentage")
        exit(1)
    t = np.arange(0.0, 0.1 * part / 100, 0.00001)
    noise = np.random.uniform(-1, 1, len(t))
    fig, ax = plt.subplots()
    plt.plot(t, noise)
    ax.set(xlabel="time (ms)", ylabel="voltage (V)", title="Lab #2 signal")
    plt.show()


def output_to_csv(filename):
    file = None
    if os.path.isfile(filename):
        print(f"File {filename} exists, overwrite? (y/N)")
        overwrite = input().lower()
        while (overwrite != "y") & (overwrite != "n") & (overwrite != ""):
            print("Input \"y\" or \"n\" (case-insensitive)")
            overwrite = input().lower()
        if (overwrite == "n") | (overwrite == ""):
            print("File will not be overwritten, exiting")
            exit(0)
        else:
            print(f"Overwriting file {filename}")
            file = open(filename, "w")
    else:
        file = open(filename, "w")

    if file is None:
        print("file is None, exiting...")
        exit(1)

    sum = 0
    for t in np.arange(0.0, 0.1, 0.00001):
        value = np.random.uniform()
        x = "{0:.5f}".format(t)
        y = "{0:.5f}".format(value)
        file.write(f"{x}\t{y}\n")
        sum += value

    mean = "{0:.5f}".format(float(sum) / 100000)
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
