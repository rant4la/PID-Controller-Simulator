from pid import PidController
from system import System
import matplotlib.pyplot as plt


import math

system = System(2, 30, 0.1, 10)
setpoint = 0

smallestCumulativeError = 9999999
bestPID = []
bestSetpointVector = []
bestLocationVector = []

def setpointFunction(t):
    if (t < 12):
        return 100
    if (t < 25):
        return 50
    return 0


for p in range(0, 100):
    for i in range(0, 10):
        for d in range(0, 10):
        
            system.reset()
            controller = PidController(p/10, i/10, d/10)

            setpointVector = []
            locationVector = []

            cumulativeError = 0

            for t in range(1, 50):

                setpoint = setpointFunction(t)

                setpointVector.append(setpoint)
                locationVector.append(system.location)

                controlForce = controller.evaluate(setpoint, system.location)
                
                cumulativeError += abs(controller.error)

                system.simulate(controlForce)


            if (cumulativeError < smallestCumulativeError):
                smallestCumulativeError = cumulativeError
                bestSetpointVector = setpointVector
                bestLocationVector = locationVector
                bestPID = [str(controller.p), str(controller.i), str(controller.d)]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(bestSetpointVector, label='Setpoint')
ax.plot(bestLocationVector, label='Location')
 
# Adding title
titleText = 'Best PID parameters were: (' + ', '.join(bestPID) + ') (Cumulative error: ' + str(round(smallestCumulativeError)) + ')\n'
titleText += 'Spring constant: ' + str(system.springConstant) + ', '
titleText += 'Spring location: ' + str(system.springLocation) + ', '
titleText += 'Drag constant: ' + str(system.dragConstant) + ', '
titleText += 'Mass: ' + str(system.mass) + ''
ax.set_title(titleText, fontsize=10)

# Adding axis title
ax.set_xlabel('Time [s]', fontsize=10)
ax.set_ylabel('Location [m]', fontsize=10)
 


ax.legend()

plt.show()