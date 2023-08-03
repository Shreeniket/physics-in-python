#Created by Shreeniket Upasani
import numpy as np
import matplotlib.pyplot as plt
import math
from vpython import *
import time


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
    

#This function will solve the differential that relates the position and time for the required simulation
def euler_method(init_pos, init_t, no_steps, step_size, f, init_v): #init_pos will be a vector
    allPos = [init_pos]
    allT = [init_t]
    rate = init_v
    allRate = [rate]
    #This for loop calculates the rate at any given time(given by the differential) then solves it by using Euler's method
    for i in range(no_steps):
        rate = init_v.add(derivative(f, allT[-1], init_v)) #rate will be a vector(Not constant)
        dt = allT[-1] + step_size  #Calculates the change in time
        dpos = rate
        dpos.multiply(step_size)
        pos = allPos[-1].add(dpos) #Calculates current position by adding last position to change in positon

        allT.append(dt)
        allPos.append(pos)
        allRate.append(rate)

    return allPos, allT, allRate

def derivative(f, t, init_v):
    if f == 'projectile':
        d_rate = Vector(0, -9.8*t, 0)
    return d_rate

def rate_of_projectile(dt, init_v):
    d_rate = Vector(init_v.x, -9.8*dt, 0)  # Incorporate gravity in the y-direction
    return d_rate

def plot_vector_vs_time(allVec, allT, title):
    # Extract x, y, and z components from allVec
    x = [vec.x for vec in allVec]
    y = [vec.y for vec in allVec]
    z = [vec.z for vec in allVec]

    # Create separate graphs for x, y, and z components
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(allT, x)
    plt.xlabel('Time')
    plt.ylabel('x '+title)

    plt.subplot(3, 1, 2)
    plt.plot(allT, y)
    plt.xlabel('Time')
    plt.ylabel('y '+title)

    plt.subplot(3, 1, 3)
    plt.plot(allT, z)
    plt.xlabel('Time')
    plt.ylabel('z '+title)

    plt.tight_layout()
    plt.show()


def projectile():
    x = 10
    y = 10
    z = 0
    u0 = Vector(x, y, z)
    p0 = Vector(0, 0, 0)
    Tf = (2*u0.y)/9.8
    no_of_steps = int(Tf/0.01)
    allPos, allT, allRate = euler_method(p0, 0, no_of_steps, 0.01, 'projectile', u0)
    #plot_vector_vs_time(allPos, allT, 'Position')
    positions = []
    max_range = (2*x*y)/9.8
    visualize_projectile_motion(allPos, allT, max_range)

def visualize_projectile_motion(allPos, allT, max_range):
    scene = canvas(width=800, height=600)
    projectile = sphere(pos=vector(0, 0, 0), radius = 0.3, color = color.red)
    x_axis = cylinder(pos = vector(-50,0,0), radius = 0.02, axis = vector(1, 0, 0), length = 75)
    y_axis = cylinder(pos = vector(0,-50,0), radius = 0.02, axis = vector(0, 1, 0), length = 75)
    z_axis = cylinder(pos = vector(0,0,-50), radius = 0.02, axis = vector(0, 0, 1), length = 75)
    time.sleep(5)
    for t, pos in zip(allT, allPos):
        rate(1 / (t+0.01 - t))  
        projectile.pos = vector(pos.x, pos.y, pos.z)


projectile()
