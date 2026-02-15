import pyrosim.pyrosim as pyrosim


"""
length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5
x2, y2, z2 = 1, 0, 1.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length,width,height])
"""
"""
for k in range(5):
    x = 0
    x += k
    for j in range(5):
        y = 0
        y += j
        length, width, height = 1, 1, 1
        for i in range(10):
            z = 0.5

            z += i
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
            length *= 0.9
            width *= 0.9
            height *= 0.9
"""

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    length, width, height = 1, 1, 1
    x, y, z = -2, 2, 0.5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    """length, width, height = 1, 1, 1
    x, y, z = 0, 0, 0.5
    pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length,width,height])

    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0, 0, 1])

    length1, width1, height1 = 1, 1, 1
    x1, y1, z1 = 0, 0, 0.5
    pyrosim.Send_Cube(name="Link1", pos=[x1, y1, z1], size=[length1, width1, height1])

    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0, 0, 1])

    length2, width2, height2 = 1, 1, 1
    x2, y2, z2 = 0, 0, 0.5
    pyrosim.Send_Cube(name="Link2", pos=[x2, y2, z2], size=[length2, width2, height2])

    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[0, 0.5, 0.5])

    length3, width3, height3 = 1, 1, 1
    x3, y3, z3 = 0, 0.5, 0
    pyrosim.Send_Cube(name="Link3", pos=[x3, y3, z3], size=[length3, width3, height3])

    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[0, 1, 0])

    length4, width4, height4 = 1, 1, 1
    x4, y4, z4 = 0, 0.5, 0
    pyrosim.Send_Cube(name="Link4", pos=[x4, y4, z4], size=[length4, width4, height4])

    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0, 0, -1])

    length5, width5, height5 = 1, 1, 1
    x5, y5, z5 = 0, 0.5, 0
    pyrosim.Send_Cube(name="Link5", pos=[x5, y5, z5], size=[length5, width5, height5])

    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0, 0, -1])

    length6, width6, height6 = 1, 1, 1
    x6, y6, z6 = 0, 0.5, 0
    pyrosim.Send_Cube(name="Link6", pos=[x6, y6, z6], size=[length6, width6, height6])

    """
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

Create_World()
Create_Robot()