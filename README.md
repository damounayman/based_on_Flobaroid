# based_on_Flobaroid
This repository is based on Flobaroid to identify the dynamic parameters of abb irb 2600 and abb irb 6640

##Content
Six Python scripts are available :
- `trajectory.py` This script computes an optimal excitation trajectory.
- `visualizer.py` /!\\ TODO
- `excite.py` /!\\ TODO
- `identify.py` /!\\ TODO
- `optimal_trajectory_test.py` /!\\ TODO
- `plot trajectory.py` /!\\ TODO

See the corresponding paragraph for description

##`trajectory.py`
This script computes an optimal excitation trajectory from the following usual parameters :

1.  *\--filename* : the name of the file into which trajectory parameters are to be saved, in [**npz**](https://numpy.org/doc/stable/reference/generated/numpy.savez.html) format;

1. *\--config* : the configuration options for trajectory optimization (algorithm, number of pass, etc.) in [**yaml**](https://yaml.org/) format;

1. *\--model* : the file describing the robot considered, in [**urdf**](http://wiki.ros.org/urdf) format;

1. *\--world* : the file describing the world in which the robot is set, in [**urdf**](http://wiki.ros.org/urdf) format.

Additional parameters exist, see the Python code.
