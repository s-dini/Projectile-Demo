import matplotlib.pyplot as plt
import numpy as np
import math

def plot_graph(velocity_initial, angle, ax, title="Graph", xlabel="X-axis", ylabel="Y-axis", line_style="-", color="blue", marker=None, show=False):
    t = np.linspace(0, 5, endpoint=True)  # Time array
    X = ReturnX(velocity_initial, angle, t) 
    Y = ReturnY(velocity_initial, angle, t)
    
    ax.plot(X, Y, linestyle=line_style, color=color, marker=marker, label=f'Angle: {angle}°')

def CalculateComponents(vi, angle): 
    angle_rad = np.radians(angle)  # Convert angle to radians
    vx = vi * math.cos(angle_rad) 
    vy = vi * math.sin(angle_rad)
    return (vx, vy)

def ReturnX(vi, angle, t): 
    angle_rad = np.radians(angle)  # Convert angle to radians
    vx = vi * math.cos(angle_rad)
    return vx * t  # Horizontal position as a function of time

def ReturnY(vi, angle, t): 
    angle_rad = np.radians(angle)  # Convert angle to radians
    vy = vi * math.sin(angle_rad)
    return ( -0.5 * 9.8 * t ** 2.0 ) + ( vy * t )  # Vertical position as a function of time

# Create figure and axes: fig, ax returns both the figure and the axes 
fig, ax = plt.subplots(figsize=(10, 10))

# Plot multiple lines
plot_graph(50, 45, ax, line_style="-", color="blue")
plot_graph(50, 30, ax, line_style="-", color="green")

# Set titles and labels
ax.set_title("Projectile Motion (Parametric)")
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
ax.grid(True)
ax.legend()

plt.show()
