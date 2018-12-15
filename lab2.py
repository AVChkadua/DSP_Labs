import sys

import matplotlib.pyplot as plt
import numpy as np

import commons


def plot_graph():
    t = np.arange(0.0, 0.1, 0.00001)
    noise = np.random.uniform(-1.3, 1.3, len(t))
    fig, ax = plt.subplots()
    plt.plot(t, noise)
    ax.set(xlabel="time (ms)", ylabel="voltage (V)", title="Noise")
    plt.show()


def output_to_csv(filename):

    file = commons.open_file(filename)
    x_range = np.arange(0.0, 0.1, 0.00001)
    noise = np.random.uniform(-1.3, 1.3, 10000)
    for i in range(0, 10000):
        x = "{0:.5f}".format(x_range[i])
        y = "{0:.5f}".format(noise[i])
        file.write(f"{x}\t{y}\n")

    mean = "{0:.5f}".format(np.mean(noise))
    disp = "{0:.5f}".format(np.var(noise))
    print(f"Mean value is {mean}")
    print(f"Variance is {disp}")
    file.close()
    exit(0)


if len(sys.argv) < 2:
    print("Input command ('show' or 'csv')")
    exit(1)
if sys.argv[1] == "show":
    plot_graph()
elif sys.argv[1] == "csv":
    if len(sys.argv) < 3:
        print("Input file for output")
        exit(1)
    output_to_csv(sys.argv[2])
