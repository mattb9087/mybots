import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B py simulate.py " + directOrGUI )
        f = open("fitness.txt")
        self.fitness = float(f.read())
        f.close()

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomCol = random.randint(0, 1)

        self.weights[randomRow, randomCol] = random.random() * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        length, width, height = 1, 1, 1
        x, y, z = -2, 2, 0.5
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        length1, width1, height1 = 1, 1, 1
        x1, y1, z1 = 1.5, 0, 1.5
        pyrosim.Send_Cube(name="Torso", pos=[x1, y1, z1], size=[length1, width1, height1])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])

        length, width, height = 1, 1, 1
        x, y, z = -0.5, 0, -0.5
        pyrosim.Send_Cube(name="BackLeg", pos=[x, y, z], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])

        length2, width2, height2 = 1, 1, 1
        x2, y2, z2 = 0.5, 0, -0.5  # the coordinates are relative to the joint that joins both links. In this case the joint (absolute coordinates) is at 2, 0, 1 so the link's position will be 0.5, 0, 0.5 because the center of the link is moved 0.5, 0, 0.5 from the joint
        pyrosim.Send_Cube(name="FrontLeg", pos=[x2, y2, z2], size=[length2, width2, height2])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        """pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-1.5)
        pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-1.5)
        pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=-1.5)
        pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=-1.5)"""

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=(currentColumn + 3),
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID


