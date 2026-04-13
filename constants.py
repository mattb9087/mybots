import numpy

iterations = 1000

# gravity constants
gravity_x = 0
gravity_y = 0
gravity_value = -9.8

# back leg constants
ampBackLeg =numpy.pi/8
freqBackLeg = 20
phaseOffsetBackLeg = 0
maxForceBackLeg = 100

# front leg constants
ampFrontLeg = numpy.pi/4
freqFrontLeg = 20
phaseOffsetFrontLeg = 0
maxForceFrontLeg = 100

# generate vector of sinusoidally varying values
firstVector = numpy.linspace(0, numpy.pi * 2, iterations)

# time sleep
time = 1/240

numberOfGenerations = 10

populationSize = 10