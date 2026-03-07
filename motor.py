import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

        self.amplitude = c.ampBackLeg
        self.frequency = c.freqBackLeg
        self.offset = c.phaseOffsetBackLeg

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if self.jointName == b'Torso_BackLeg':
            self.frequency = c.freqBackLeg / 2

        self.motorValues = numpy.zeros(c.iterations)
        for ind, each in enumerate(c.firstVector):
            self.motorValues[ind] = self.amplitude * numpy.sin(self.frequency * each + self.offset)

    def Set_Value(self, desiredAngle, robotId):
        # simulating motors
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForceBackLeg)

    def Save_Value(self):
        dst = 'data/' + self.jointName + 'Motor'
        numpy.save(dst, self.motorValues)