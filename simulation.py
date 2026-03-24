from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
    def __init__(self, directOrGUI):
        if directOrGUI == 'DIRECT':
            self.physicsCLient = p.connect(p.DIRECT)

        else:
            self.physicsCLient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        p.setGravity(c.gravity_x, c.gravity_y, c.gravity_value)

    def Run(self):
        for i in range(c.iterations):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            """print(i)"""
            time.sleep(c.time)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
