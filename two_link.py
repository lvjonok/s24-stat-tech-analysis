import numpy as np
import numpy.typing as npt


def control(q: npt.ArrayLike, v: npt.ArrayLike, dv: npt.ArrayLike, time: npt.ArrayLike):
    # for two-link we have to return an array of 2 elements
    return np.array(
        [
            30 * np.sin(time),
            10 * np.sin(time),
        ]
    )
