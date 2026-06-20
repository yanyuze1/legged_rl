"""
Python module serving as a project/extension template.
"""

# Register Gym environments.
from .tasks import *


import os

LEGGED_RL_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
