import pyrosim.pyrosim as pyrosim


pyrosim.Start_SDF("boxes.sdf")

"""
length, width, height = 1, 1, 1
x, y, z = 0, 0, 0.5
x2, y2, z2 = 1, 0, 1.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length,width,height])
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



pyrosim.End()