#!/usr/bin/python3

import fire
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class plotter:
    title: str
    output: str

    def __init__(self, title: str, output: str = None):
        self.title = title
        self.output = output

    def plot(self, input_file):
        sns.set_theme()
        runtimes = pd.read_csv(input_file)
        print(runtimes.columns)
        print(runtimes)
        sns.relplot(data=runtimes, x=" Density", y=" CSR w/o MKL", kind="line", hue="Vertices")
        plt.show()


if __name__ == "__main__":
    fire.Fire(plotter)
