import numpy
import matplotlib.pyplot

"""
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

print(backLegSensorValues)
print(frontLegSensorValues)

matplotlib.pyplot.plot(backLegSensorValues, linewidth="4")
matplotlib.pyplot.plot(frontLegSensorValues)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
"""
targetAngles = numpy.load("data/targetAngles.npy")
print(targetAngles)

matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
