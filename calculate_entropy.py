import json
import numpy as np
import EntropyHub as EH

# Load symbolic JSON input
with open('forecast/forecast_entropy_curvature_data.json', 'r') as f:
    data = json.load(f)

signal = np.array(data.get('symbolic_entropy_sequence', []))

# Ensure the signal is valid
if len(signal) < 12:
    raise ValueError("Input sequence too short for entropy calculation. Minimum length: 12")

# Calculate Sample Entropy
result = EH.SampEn(signal, m=2, r=0.2)

# Prepare output structure
output = {
    "sample_entropy": result[0].tolist(),
    "pattern_counts": result[1].tolist(),
    "template_matches": result[2].tolist()
}

# Write to output JSON
with open('forecast/output_entropy_result.json', 'w') as f:
    json.dump(output, f, indent=2)

print("Entropy calculation complete. Output saved to forecast/output_entropy_result.json")
