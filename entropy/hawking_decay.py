import numpy as np

def apply_hawking_decay(sequence, decay_rate=0.05):
    """
    Applies symbolic Hawking-style decay to a numeric sequence.
    Models information bleed or symbolic entropy evaporation.
    """
    decayed = []
    info_mass = 1.0

    for i, val in enumerate(sequence):
        info_loss = np.exp(-decay_rate * i) * info_mass
        decayed_val = val * info_loss
        decayed.append(decayed_val)

        # Optional: reduce mass after emission like black hole evaporation
        info_mass *= (1 - decay_rate / 10)

    return decayed
