import numpy as np
import matplotlib.pyplot as plt
import json

def hawking_symbolic_decay(sequence, decay_rate=0.005):
    """
    Applies symbolic decay inspired by Hawking radiation to a sequence.
    Gradually reduces each value with a decay curve, simulating entropy loss.
    """
    if not isinstance(sequence, np.ndarray):
        sequence = np.array(sequence, dtype=float)

    decay_curve = np.exp(-decay_rate * np.arange(len(sequence)))
    decayed_sequence = sequence * decay_curve
    return decayed_sequence, decay_curve.tolist()

if __name__ == "__main__":
    # Example test symbolic motif data
    original = np.array([4, 5, 7, 10, 8, 6, 3, 2, 1, 0.5])
    decayed, curve = hawking_symbolic_decay(original)

    # Save decay to file for terrain engine
    with open("decayed_output.json", "w") as f:
        json.dump({
            "original_sequence": original.tolist(),
            "decay_curve": curve,
            "decayed_sequence": decayed.tolist()
        }, f, indent=2)

    # Optional plot for inspection
    plt.plot(original, label="Original")
    plt.plot(decayed, label="Decayed (Hawking)")
    plt.title("Symbolic Decay Inspired by Hawking Radiation")
    plt.legend()
    plt.grid(True)
    plt.savefig("hawking_decay_plot.png")
    plt.show()
