import numpy as np

def hawking_entropy_decay(sequence, decay_rate=0.05):
    """
    Applies symbolic Hawking-style entropy decay to a numeric sequence.

    This simulates symbolic evaporation or entropy loss inspired by Hawking radiation,
    where earlier values retain more 'mass' (information) than later ones.

    Parameters:
        sequence (list or np.array): The input numeric sequence (entropy, curvature, etc.).
        decay_rate (float): The decay coefficient. Higher = faster symbolic dissipation.

    Returns:
        list: Decayed numeric sequence with entropy decay applied.
    """
    decayed = []
    info_mass = 1.0

    for i, val in enumerate(sequence):
        info_loss = np.exp(-decay_rate * i) * info_mass
        decayed_val = val * info_loss
        decayed.append(decayed_val)

        # Emulate black hole evaporation: info mass slowly reduces over time
        info_mass *= (1 - decay_rate / 10)

    return decayed
