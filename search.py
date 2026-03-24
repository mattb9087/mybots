import os
from hillclimber import HILLCLIMBER


"""for i in range(5):
    os.system("py generate.py")
    os.system("py simulate.py")"""

hc = HILLCLIMBER()
hc.Evolve()
hc.Show_Best()
