import json
import numpy as np
import matplotlib.pyplot as plt
from EntropyHub import SampEn

# Load symbolic input
with open("symbolic_input.json", "r") as file:
    data = json.load(file)

# Extract signal
signal = np.array(data.get("symbolic_sequence", []))

# Check for minimum length
if len(signal) < 12:
    raise ValueError("Input sequence too short for entropy calculation. Minimum length: 12")

# Calculate Sample Entropy
entropy, counts, matches = SampEn(signal, m=2, r=0.2)

# Save entropy results
results = {
    "entropy_values": entropy.tolist() if hasattr(entropy, "tolist") else [entropy],
    "summary": {
        "min": float(min(entropy)) if hasattr(entropy, '__iter__') else float(entropy),
        "max": float(max(entropy)) if hasattr(entropy, '__iter__') else float(entropy),
        "mean": float(np.mean(entropy)) if hasattr(entropy, '__iter__') else float(entropy),
        "std": float(np.std(entropy)) if hasattr(entropy, '__iter__') else 0.0
    }
}

with open("entropy_results.json", "w") as out_file:
    json.dump(results, out_file, indent=2)

# Plot entropy values
plt.figure(figsize=(10, 5))
plt.plot(results["entropy_values"], marker='o')
plt.title("Symbolic Entropy Over Time")
plt.xlabel("Index")
plt.ylabel("Sample Entropy")
plt.grid(True)
plt.savefig("entropy_graphs.png")
plt.close()
