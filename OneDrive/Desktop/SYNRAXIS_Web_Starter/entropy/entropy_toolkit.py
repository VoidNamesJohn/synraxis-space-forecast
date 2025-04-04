import json
import numpy as np
import EntropyHub as EH
import matplotlib.pyplot as plt
from pathlib import Path

def load_symbolic_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return np.array(data.get("symbolic_sequence", []))

def calculate_entropy_metrics(signal):
    if len(signal) < 12:
        raise ValueError("Input sequence too short for entropy calculation. Minimum length: 12")

    sampen = EH.SampEn(signal, m=2, r=0.2)
    apen = EH.ApEn(signal, m=2, r=0.2)
    pe = EH.PermEn(signal, m=3)

    return {
        "SampleEntropy": sampen[0][0],
        "ApproximateEntropy": apen[0][0],
        "PermutationEntropy": pe[0][0]
    }

def save_results(results, output_path):
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

def plot_entropy_graphs(results, output_path):
    labels = list(results.keys())
    values = list(results.values())

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color='cyan')
    plt.title("Entropy Metrics")
    plt.xlabel("Metric")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main():
    input_file = 'symbolic_input.json'
    result_file = 'forecast/entropy_results.json'
    plot_file = 'forecast/entropy_graphs.png'

    signal = load_symbolic_data(input_file)
    results = calculate_entropy_metrics(signal)
    save_results(results, result_file)
    plot_entropy_graphs(results, plot_file)
    print("Entropy results and graph saved.")

if __name__ == "__main__":
    main()