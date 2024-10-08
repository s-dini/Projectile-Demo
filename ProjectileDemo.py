import matplotlib.pyplot as plt
import numpy as np
import math


def plot_graph(velocity_initial, angle, initial_position, ax, title="Graph", xlabel="X-axis", ylabel="Y-axis", line_style="-", color="blue", marker=None, show=False):
    t = np.linspace(0, 10, endpoint=True)
    X = ReturnX(velocity_initial, angle, initial_position[0], t) 
    Y = ReturnY(velocity_initial, angle, initial_position[1], t)

    ax.plot(X, Y, linestyle=line_style, color=color, marker=marker, label=f'Angle: {angle}°')

def CalculateComponents(vi, angle): 
    angle_rad = np.radians(angle)  
    vx = vi * math.cos(angle_rad) 
    vy = vi * math.sin(angle_rad)
    return (vx, vy)

def ReturnX(vi, angle, x, t): 
    angle_rad = np.radians(angle)  
    vx = vi * math.cos(angle_rad)
    return (vx * t + x)

def ReturnY(vi, angle, y, t): 
    angle_rad = np.radians(angle)  
    vy = vi * math.sin(angle_rad)
    return (( -0.5 * 9.8 * t ** 2.0 ) + ( vy * t ) + y )  # Vertical position as a function of time

# Create figure and axes: fig, ax returns both the figure and the axes 
fig, ax = plt.subplots(figsize=(10, 10))

plot_graph(50, 45, (10,0), ax, line_style="-", color="blue")
plot_graph(50, 30, (0,0), ax, line_style="-", color="green")
plot_graph(25, 10, (0,30), ax, line_style="-", color="brown")

plt.autoscale(enable=True, axis="both", tight=None)

ax = plt.gca()

ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)

ax.set_title("Projectile Motion (Parametric)")
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
ax.grid(True)
ax.legend()

plt.show()
