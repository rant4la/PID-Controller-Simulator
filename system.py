class System:

    def __init__(self, springConstant, springLocation, dragConstant, mass):
        self.springConstant = springConstant
        self.springLocation = springLocation
        self.dragConstant = dragConstant
        self.mass = mass

        self.reset()

    def simulate(self, controlForce):
        
        springForce = self.springConstant * (-self.location + self.springLocation)
        dragForce = self.dragConstant * -self.speed

        acceleration = (controlForce + springForce + dragForce) / self.mass

        self.lastLocation = self.location
        self.location = self.location + acceleration
        self.speed = self.location - self.lastLocation

        return self.speed

    def reset(self):
        self.lastLocation = 0
        self.location = 0
        self.speed = 0
