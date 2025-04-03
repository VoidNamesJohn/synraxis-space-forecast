import json
from entropy.entropy_toolkit import calculate_entropy_metrics
from entropy.hawking_decay import hawking_entropy_decay
from entropy.symbolic_decay import evolve_symbolic_system

# Step 1: Load symbolic input
with open("entropy/symbolic_input.json", "r") as f:
    data = json.load(f)
sequence = data.get("sequence", [])

# Step 2: Compute entropy + motif metrics
entropy, curvature, details = calculate_entropy_metrics(sequence)

# Step 3: Apply Hawking-style symbolic decay
decayed = hawking_entropy_decay(sequence, rate=0.03)

# Step 4: Run symbolic motif evolution
evolved = evolve_symbolic_system(decayed)

# Step 5: Save output
output = {
    "original": sequence,
    "entropy": entropy,
    "curvature": curvature,
    "decayed": decayed,
    "evolved": evolved,
    "details": details
}
with open("forecast/synraxis_output.json", "w") as out:
    json.dump(output, out, indent=2)

print("✅ SYNRAXIS engine run complete. Output saved to forecast/synraxis_output.json")
