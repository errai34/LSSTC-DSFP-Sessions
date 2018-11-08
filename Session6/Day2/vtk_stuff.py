import numpy as np
import matplotlib.pyplot as plt

from pyevtk.hl import gridToVTK, pointsToVTK
np.random.seed(23)

x = np.random.normal(0, 20, 500)
y = np.random.normal(0, 20, 500)
z = np.random.normal(0, 20, 500)

temp = 2.4/x + 0.04 * y**2 + 5/z
pressure = 1.11*x**2 + 3.1*y + 0.06*z**2 # complete

pointsToVTK("./points", x, y, z, data = {"temp" : temp, "pressure" : pressure})