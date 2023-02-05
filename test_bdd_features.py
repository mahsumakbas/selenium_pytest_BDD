from pytest_bdd import when, then, given, scenario, scenarios

# import all step definition files here
from step_defs.test_bdd_calculator import *
from step_defs.test_bdd_triangle import *

# it discovers all feaures(test cases) under "features" folder,
# so no need to define scenarios one by one manually
scenarios('./features/')
