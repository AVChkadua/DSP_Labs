import matplotlib.pyplot as plt
import numpy as np
import os
import sys


def signal(x):
    return 1.3 * np.cos(2 * np.pi * 26885.46875 * x + np.radians(120))


def plot_graph(part):
    if not 0.0 < part <= 100.0:
        print("Invalid percentage")
        exit(1)
    t = np.arange(0.0, 0.1 * part / 100, 0.000001)
    func = 1.3 * np.cos(2 * np.pi * 26885.46875 * t + np.radians(120))
    fig, ax = plt.subplots()
    plt.plot(t, func)
    ax.set(xlabel="time (ms)", ylabel="voltage (V)", title="Lab #1 signal")
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

    t = 0
    freq = 1 / 100000

    if file is None:
        print("file is None, exiting...")
        exit(1)

    sum = 0
    while t <= 0.1:
        value = signal(t)
        x = "{0:.5f}".format(t)
        y = "{0:.5f}".format(value)
        file.write(f"{x}\t{y}\n")
        sum += value
        t += freq

    mean = "{0:.5f}".format(float(sum) / (0.1 / 0.000001))
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
