import numpy as np

def single_stage_cooling(T_initial, T_env, k, time):
    return T_env + (T_initial - T_env) * np.exp(-k * time)


def multi_stage_cooling(time, leak=0.0):
    T = []

    for t in time:
        if t < 30:
            # Stage 1: 300K → 77K
            temp = 77 + (300 - 77) * np.exp(-0.08 * t)

        elif t < 70:
            # Stage 2: 77K → 4K
            temp = 4 + (77 - 4) * np.exp(-0.05 * (t - 30))

        else:
            # Stage 3: 4K → ~0K
            temp = 0.5 + (4 - 0.5) * np.exp(-0.02 * (t - 70))

        # Add heat leak
        temp += leak * t

        T.append(temp)

    return np.array(T)