import numpy as np
import json
import os
from entropy.entropy_toolkit import calculate_entropy_metrics
from entropy.hawking_decay import apply_symbolic_decay
from einstein_layers import run_einstein_layers

def generate_chaotic_pattern(length=100, r=3.99, x0=0.4):
    pattern = [x0]
    for _ in range(length - 1):
        x0 = r * x0 * (1 - x0)
        pattern.append(x0)
    return pattern

# Step 1: Generate chaotic input
chaotic_input = generate_chaotic_pattern(length=100)

# Step 2: Symbolic Hawking entropy decay
decayed_data = apply_symbolic_decay(chaotic_input)

# Step 3: Entropy and symbolic curvature
entropy_result, curvature_result, evolution_steps = calculate_entropy_metrics(decayed_data)

# Step 4: Einstein relativity simulation
einstein_result = run_einstein_layers()

# Step 5: Output result dictionary
output_data = {
    "chaotic_input": chaotic_input,
    "decayed": decayed_data,
    "entropy": entropy_result,
    "curvature": curvature_result,
    "evolution": evolution_steps,
    "einstein": {
        "curvature": einstein_result["curvature"].tolist(),
        "time_dilation": einstein_result["time_dilation"],
        "length_contracted": einstein_result["length_contracted"],
        "relativistic_energy": einstein_result["relativistic_energy"],
        "gravity_waveform": einstein_result["gravity_waveform"].tolist()
    }
}

# Step 6: Save to JSON in forecast/
output_path = "forecast/chaos_output.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as out:
    json.dump(output_data, out, indent=2)

print(f"✅ Chaotic forecast run complete. Output saved to {output_path}")

# Step 7: Optional – copy to Netlify UI (docs/)
netlify_output_path = "docs/chaos_output.json"
os.makedirs(os.path.dirname(netlify_output_path), exist_ok=True)

try:
    with open(netlify_output_path, "w") as net_out:
        json.dump(output_data, net_out, indent=2)
    print(f"🌐 Output also synced to Netlify UI: {netlify_output_path}")
except Exception as e:
    print(f"⚠️ Could not sync to Netlify UI: {e}")
