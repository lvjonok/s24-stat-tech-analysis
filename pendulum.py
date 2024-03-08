import numpy as np
import numpy.typing as npt


def control(q: npt.ArrayLike, v: npt.ArrayLike, dv: npt.ArrayLike, time: npt.ArrayLike):
    # for pendulum we have to return an array of 1 element
    return np.array(
        [
            30 * np.sin(time),
        ]
    )
