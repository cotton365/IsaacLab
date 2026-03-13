# test_flat.py
from isaaclab.app import AppLauncher
import argparse
parser = argparse.ArgumentParser()
AppLauncher.add_app_launcher_args(parser)
args, _ = parser.parse_known_args()
app_launcher = AppLauncher(args)
simulation_app = app_launcher.app

# Use a known-working simple env
import gymnasium as gym
env = gym.make("Isaac-Anymal-C-v0", render_mode=None)  # Official Anymal-C flat terrain
print("Resetting official Anymal-C...")
obs, _ = env.reset()
print("Success! Obs shape:", obs.shape)
env.step(env.action_space.sample())
env.close()
simulation_app.close()
print("Official env works.")