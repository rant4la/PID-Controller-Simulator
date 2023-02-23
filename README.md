# PID-Controller-Simulator
This is a PID controller simulator which can automatically tune the correct P, I and D coefficients. It works for any system that can be modeled with a spring, drag and mass forces.

Steps for tuning your system:
1. Change the System spring, drag and mass constants to best fit your system that you are modeling.
2. Next change the setpointFunction so that it best simulates what kind of setpoint control your system needs to react to.
3. Finally run the code and you should see a visualization of the setpoint and location graph of the best PID solution:

![image](https://user-images.githubusercontent.com/33716618/220734645-e29b0c93-4e40-46ed-aa80-7621808f613f.png)

4. At the top you can see the best values the optimizer found for P, I and D coefficients and also the cumulative error (absolute error integral):

![image](https://user-images.githubusercontent.com/33716618/220732982-d53b1a37-d630-4709-bba4-1a219f0f57c9.png)



