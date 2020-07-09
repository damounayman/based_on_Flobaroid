from __future__ import division
from __future__ import print_function
from builtins import range
from builtins import object
from typing import List, Dict, Tuple, Union

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import pyOpt
import iDynTree; iDynTree.init_helpers(); iDynTree.init_numpy_helpers()
from colorama import Fore

from identification.model import Model
from identification.data import Data
from identification.helpers import URDFHelpers
from excitation.trajectoryGenerator import simulateTrajectory, Trajectory, PulsedTrajectory
from excitation.optimizer import plotter, Optimizer

plotter(self.config, data=trajectory_data)
