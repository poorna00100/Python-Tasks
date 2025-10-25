# plotting_probabilities.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

def plot_normal_distribution(mean=0, std_dev=1):
    """Plots a Normal Distribution Curve"""
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    y = norm.pdf(x, mean, std_dev)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='blue', label=f'N({mean}, {std_dev}²)')
    plt.title("Normal Distribution")
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_binomial_distribution(n=10, p=0.5):
    """Plots a Binomial Distribution"""
    x = np.arange(0, n + 1)
    y = binom.pmf(x, n, p)

    plt.figure(figsize=(8, 5))
    plt.bar(x, y, color='orange', alpha=0.7, label=f'Binomial(n={n}, p={p})')
    plt.title("Binomial Distribution")
    plt.xlabel("Number of Successes")
    plt.ylabel("Probability")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()


def main():
    print("Select a distribution to plot:")
    print("1. Normal Distribution")
    print("2. Binomial Distribution")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        mean = float(input("Enter mean (e.g., 0): "))
        std_dev = float(input("Enter standard deviation (e.g., 1): "))
        plot_normal_distribution(mean, std_dev)

    elif choice == '2':
        n = int(input("Enter number of trials (n): "))
        p = float(input("Enter probability of success (p): "))
        plot_binomial_distribution(n, p)

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
