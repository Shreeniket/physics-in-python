#Created by Shreeniket Upasani
import numpy as np
import matplotlib.pyplot as plt
import math
from vpython import *

pi = math.pi
G = 6.67430e-11
   
def euler_method(init_pos, init_t, no_steps, step_size, init_v, m1, m2): #init_pos will be a vector
    allPos = [init_pos]
    allT = [init_t]
    v_planet = init_v
    allRate = [v_planet]
    planet_pos = init_pos
    for i in range(no_steps):
        star_pos = np.array([0, 0, 0])
        r_diff = star_pos - planet_pos
        r = np.linalg.norm(r_diff)
        F = (G * m1 * m2 / r**3)*r_diff
        a = F/m2
        dv = a * step_size
        v_planet = v_planet + dv
        dpos = v_planet * step_size
        planet_pos = planet_pos + dpos
        t = allT[-1] + step_size
        allT.append(t)
        allPos.append(planet_pos)
    return allPos, allT, allRate

def planetary_motion(m1_p, m2_p, init_pos2_p, t, init_v_p):
    m1 = m1_p
    m2 = m2_p
    init_pos2 = init_pos2_p
    time = 1460*24*3600
    step_size = 900
    no_steps = int(time/3600)   
    init_v = init_v_p
    allPos, allT, allV = euler_method(init_pos2, 0, no_steps, step_size, init_v, m1, m2)
    visualize_planetary_motion(allT, allPos)
    
def visualize_planetary_motion(time_array, allPos):
    scene = canvas(title="Planetary Motion Visualization", width=800, height=600, range = 2.5e11)

    star = sphere(pos=vector(0, 0, 0), radius=1e10, color = color.yellow)
    ring_radius = allPos[0][0]
    ring_thickness = 5e8
    ring_object = ring(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=ring_radius, thickness=ring_thickness)

    planet_visual = sphere(pos=vector(allPos[0][0], allPos[0][1], allPos[0][2],), radius=5e9, color=color.blue)

    for t, pos in zip(time_array, allPos):
        rate(800)  
        planet_visual.pos = vector(pos[0], pos[1], pos[2])


m1 = 2e30
m2 = 6e24
init_pos2 = np.array([1.5e11, 0.0, 0.0])
init_v = np.array([0.0, 0.0, 3e4])
planetary_motion(m1, m2, init_pos2, 10, init_v)
