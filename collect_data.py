import time

import mujoco
import mujoco.viewer
import numpy as np
from mujoco_logger import SimLogger
import importlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--model", type=str, default="two_link", help="Eigher `pendulum` or `two_link`"
)
args = parser.parse_args()

control = importlib.import_module(f"{args.model}")

np.random.seed(0)

model = mujoco.MjModel.from_xml_path(f"model/{args.model}/scene.xml")
data = mujoco.MjData(model)

mujoco.mj_resetData(model, data)

with mujoco.viewer.launch_passive(model, data) as viewer, SimLogger(
    model, data, output_filepath=f"data/{args.model}.json"
) as logger:
    start = data.time
    while viewer.is_running() and data.time - start < 20.0:
        step_start = time.time()

        data.ctrl = control.control(data.qpos, data.qvel, data.qacc, data.time)

        mujoco.mj_step(model, data)
        logger.record()

        # Pick up changes to the physics state, apply perturbations, update options from GUI.
        viewer.sync()

        # Rudimentary time keeping, will drift relative to wall clock.
        time_until_next_step = model.opt.timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)
