import json
from entropy.entropy_toolkit import calculate_entropy_metrics
from entropy.hawking_decay import hawking_entropy_decay
from entropy.symbolic_decay import evolve_symbolic_system
from einstein_layers import run_einstein_layers

# Step 1: Load symbolic input
with open("entropy/symbolic_input.json", "r") as f:
    data = json.load(f)
sequence = data.get("sequence", [])

# Step 2: Compute entropy + motif metrics
entropy, curvature, details = calculate_entropy_metrics(sequence)

# Step 3: Apply Hawking-style symbolic decay
decayed = hawking_entropy_decay(sequence, decay_rate=0.03)

# Step 4: Run symbolic motif evolution
evolved = evolve_symbolic_system(decayed)

# Step 5: Run Einstein symbolic layer
einstein_output = run_einstein_layers()

# Step 6: Save combined output
output = {
    "original": sequence,
    "entropy": entropy,
    "curvature": curvature,
    "decayed": decayed,
    "evolved": evolved,
    "details": details,
    "einstein": {
        "curvature": einstein_output["curvature"].tolist(),
        "time_dilation": einstein_output["time_dilation"],
        "length_contracted": einstein_output["length_contracted"],
        "relativistic_energy": einstein_output["relativistic_energy"],
        "gravity_waveform": einstein_output["gravity_waveform"].tolist()
    }
}

with open("forecast/synraxis_output.json", "w") as out:
    json.dump(output, out, indent=2)

print("✅ SYNRAXIS engine run complete. Output saved to forecast/synraxis_output.json")
