from world import WORLD
from robot import ROBOT
import pybullet as p
import constants as c
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
    def __init__(self):
        self.physicsCLient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        p.setGravity(c.gravity_x, c.gravity_y, c.gravity_value)

    def Run(self):
        for i in range(c.iterations):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)

            print(i)
            time.sleep(c.time)

    def __del__(self):
        p.disconnect()
