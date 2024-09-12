import matplotlib.pyplot as plt
import numpy as np
import math

# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

#---------------------------------------------

# calc vx, vy using an angle in degrees
# idea: sample rate (how many data points are collected per second?) 

def plot_graph(velocity_initial, angle, ax,  title="Graph", xlabel="X-axis", ylabel="Y-axis", line_style="-", color="blue", marker=None, show=False):
    t = np.linspace(0, 5, endpoint=True) 
    plt.figure(figsize=(10, 10))

    X = ReturnX(velocity_initial, angle, t) 
    Y = ReturnY(velocity_initial, angle, t)

    ax.plot(X, Y, linestyle=line_style, color=color, marker=marker, label=f'Angle: {angle}°')


def CalculateComponents (vi, angle): 
    angle_rad = np.radians(angle)  # Convert angle to radians

    vx = vi * math.cos(angle_rad) 
    vy = vi * math.sin(angle_rad)

    return (vx, vy)

def ReturnX(vi, angle, t): 
    angle_rad = np.radians(angle)  # Convert angle to radians
    vx = vi * math.cos(angle_rad)
    
    return ( vx * t ) 

def ReturnY(vi, angle, t): 
    angle_rad = np.radians(angle)  # Convert angle to radians
    vy = vi * math.cos(angle_rad)

    return ( ( -9.8 * t ** 2.0 ) + ( vy*t ) )


# y_pos is actually a tuple with an actual list and the last time t before the object hits the ground 
""" 
y_pos = CalculateY(velocity[1], 5, 20) 
x_pos = CalculateX(velocity[0], y_pos[1] + 1, 0.0) 

plot_graph(x_pos, y_pos[0], title="Projectile Motion", xlabel="Horizontal Distance (m)", ylabel="Vertical Distance (m)", line_style="-", color="blue", marker=None)

"""

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 10))

# Plot multiple lines
plot_graph(ax, 50, 45, line_style="-", color="blue")
plot_graph(ax, 50, 30, line_style="-", color="green")

# Set titles and labels
ax.set_title("Projectile Motion")
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
ax.grid(True)
ax.legend()

plt.show()
        
    
    