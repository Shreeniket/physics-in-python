#Created by Shreeniket Upasani
import numpy as np
import matplotlib.pyplot as plt
import math
from vpython import *

pi = np.pi

#Class that creates vectors using numpy arrays and defines certain useful functions for the vectors
class Vector:
    #X,Y,Z co-ordinates:
    x = 0.0
    y = 0.0
    z = 0.0
    vector = np.array([x,y,z])

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = np.array([x,y,z])

    def displayVector(self):
        print(self.vector)

    def get(self):
        return self.vector

    def getMod(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def add(self, vector):
        x = vector.x + self.x
        y = vector.y + self.y
        z = vector.z + self.z
        sum = Vector(x,y,z)
        return sum

    def subtract(self,vector):
        x = self.x - vector.x
        y = self.y - vector.y
        z = self.z - vector.z
        difference = Vector(x,y,z)
        return difference

    def dot(self, vector):
        return self.x*vector.x + self.y*vector.y + self.z*vector.z

    def multiply(self, k):
        self.x *= k
        self.y *= k
        self.z *= k

    def angle(self):
        angle = math.atan(self.y/self.x)
        return angle
    

def euler_method(init_theta, init_omega, l, no_steps, step_size):
    allTheta = [init_theta]
    allT = [0]
    theta = init_theta
    allOmega = [init_omega]
    allAlpha = [0]
    for i in range(no_steps):
        alpha = -(9.8/l)*np.sin(theta)
        d_omega = alpha*step_size  
        omega = allOmega[-1] + d_omega
        theta = allTheta[-1] + omega*step_size
        allTheta.append(theta)
        t = allT[-1]+step_size
        allT.append(t)
        allOmega.append(omega)
        allAlpha.append(alpha)
    return allT, allTheta, allOmega


def simple_pendulum():
    init_theta = pi/6
    init_omega = 0
    l = 2
    time = 20
    step_size = 0.01
    no_steps = int(time/step_size)
    allT, allTheta, allOmega = euler_method(init_theta, init_omega, l, no_steps, step_size )
    visualize_simple_pendulum(l, allTheta, allT)
    return allT, allTheta, allOmega

def visualize_simple_pendulum(l,positions, times):
    scene = canvas(center=vector(0, -1, 0) )
    init_x = l*np.sin(positions[0])
    init_y = -l*np.cos(positions[0])
    ball = sphere(pos=vector(init_x, init_y, 0), radius=0.2, color=color.white)
    rod = cylinder(pos=vector(0, 0, 0), axis=ball.pos, radius=0.01, color=color.red)

    for i in range(len(positions)):
        ball_x = l*np.sin(positions[i])
        ball_y = -l*np.cos(positions[i])
        ball.pos = vector(ball_x, ball_y, 0)
        rod.axis = ball.pos - rod.pos
        rate(1 / (times[i + 1] - times[i]))  

def graph():
    time_values, angle_values, omega_values = simple_pendulum()
    plt.plot(time_values, angle_values)
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (radians)')
    plt.title('Simple Pendulum Simulation')
    plt.grid(True)
    plt.show()

graph()
