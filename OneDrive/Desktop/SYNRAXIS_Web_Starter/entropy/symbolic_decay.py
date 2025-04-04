import numpy as np

def evolve_symbolic_system(sequence, iterations=10, transformation="shift"):
    """
    Evolves a symbolic motif sequence over time using a symbolic transformation rule.

    Parameters:
        sequence (list): Input motif sequence (e.g., entropy values, motif IDs).
        iterations (int): Number of symbolic transformation steps.
        transformation (str): Rule to apply ('shift', 'invert', 'scale').

    Returns:
        list: List of evolved sequences per iteration.
    """
    evolved = [sequence.copy()]

    for _ in range(iterations):
        last = evolved[-1]

        if transformation == "shift":
            next_seq = [(v + 1) % 10 for v in last]
        elif transformation == "invert":
            max_val = max(last)
            next_seq = [max_val - v for v in last]
        elif transformation == "scale":
            next_seq = [v * 1.1 for v in last]
        else:
            raise ValueError(f"Unknown transformation rule: {transformation}")

        evolved.append(next_seq)

    return evolved
