import json
import numpy as np
import EntropyHub as EH

# Load symbolic data
with open('symbolic_input.json') as f:
    data = json.load(f)

sequence = data.get("symbolic_sequence", [])
if len(sequence) < 12:
    raise ValueError("Input sequence too short for entropy calculation. Minimum length: 12")

# Convert to numpy array
signal = np.array(sequence)

# Calculate entropy
result = EH.SampEn(signal, m=2, r=0.2)

# Save result
entropy_data = {
    "SampleEntropy": result[0].tolist(),
    "Matches": result[1].tolist(),
    "Templates": result[2].tolist()
}

with open('entropy_results.json', 'w') as f:
    json.dump(entropy_data, f, indent=2)

print("Entropy results saved to entropy_results.json")
