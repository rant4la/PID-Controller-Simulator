class PidController:

    def __init__(self, p, i, d):
        self.p = p
        self.i = i
        self.d = d

        self.error = 0
        self.lastError = 0
        self.integral = 0
        self.derivative = 0

    def evaluate(self, target, actual):
        self.lastError = self.error
        self.error = target - actual

        self.integral = self.integral + self.error
        self.derivative = self.lastError - self.error

        pControl = self.p * self.error
        iControl = self.i * self.integral
        dControl = self.d * self.derivative

        return pControl + iControl + dControl
    







