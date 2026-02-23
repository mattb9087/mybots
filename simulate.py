"""import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

amplitude = numpy.pi/4.0
frequency = 10
phaseOffset = 0

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

steps = 1000
i = numpy.linspace(0, 2*numpy.pi, steps)
targetAngles = amplitude * numpy.sin(frequency * i + phaseOffset)
numpy.save("data/targetAngles.npy", targetAngles)
for i in range(0, 1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles[i],
        maxForce=30
    )

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAngles[i],
        maxForce=30
    )

    print(frontLegSensorValues)
    print(backLegSensorValues)
    time.sleep(0.01)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()"""



import numpy
import random
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import time

physicsCLient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

# set up pyrosim
pyrosim.Prepare_To_Simulate(robotId)

# iterations for for-loop
iterations = 1000
# Back Leg
ampBackLeg = numpy.pi/8
freqBackLeg = 20
phaseOffsetBackLeg = 0
targetAnglesBackLeg = numpy.zeros(iterations)
# Front Leg
ampFrontLeg = numpy.pi/4
freqFrontLeg = 20
phaseOffsetFrontLeg = 0
targetAnglesFrontLeg = numpy.zeros(iterations)

# storing sensor values, numpy
backLegSensorValues = numpy.zeros(iterations)
frontLegSensorValues = numpy.zeros(iterations)

# generate vector of sinusoidally varying values
firstVector = numpy.linspace(0, numpy.pi * 2, iterations)
# Back Leg
for ind, each in enumerate(firstVector):
    targetAnglesBackLeg[ind] = ampBackLeg * numpy.sin(freqBackLeg * each + phaseOffsetBackLeg)
# Front Leg
for ind, each in enumerate(firstVector):
    targetAnglesFrontLeg[ind] = ampFrontLeg * numpy.sin(freqFrontLeg * each + phaseOffsetFrontLeg)

# opening the window using for loop 1000 times
p.loadSDF("world.sdf")
for i in range(iterations):
    p.stepSimulation()

    # add sensors
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(
        "FrontLeg")

    # simulating motors
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesBackLeg[i],
        maxForce=100)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_FrontLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesFrontLeg[i],
        maxForce=100)

    time.sleep(1/240)

# saving sensor data, sine values to a file
# numpy.save('data/backlegsensor', backLegSensorValues)
# numpy.save('data/frontlegsensor', frontLegSensorValues)
numpy.save('data/targetanglesbackleg', targetAnglesBackLeg)
numpy.save('data/targetanglesfrontleg', targetAnglesFrontLeg)

# print("back", backLegSensorValues)
# print("front", frontLegSensorValues)
p.disconnect()