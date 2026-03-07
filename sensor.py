import numpy
import constants as c
import pyrosim.pyrosim as pyrosim


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName

        # storing sensor values
        self.values = numpy.zeros(c.iterations)

    def Get_Value(self, i):
        self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        if i == c.iterations - 1:
            print(self.values)

    def Save_Values(self):
        dst = 'data/' + self.linkName + 'Sensor'
        numpy.save(dst, self.values)
