import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(frame):
    ax.clear()

    # Parameters for Gaussian distributions
    mean_x, mean_y = 0, 0

    # Variance changes over time
    variance_x = 3 + 3 * np.cos(1 * frame)
    variance_y = 3 + 3 * np.cos(1 * frame)

    # Generate data points for the 2D Gaussian distribution
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)

    # Create a 2D grid
    X, Y = np.meshgrid(x, y)

    # Calculate the Gaussian distribution for each point on the grid
    Z = (
        np.exp(-(X - mean_x)**2 / (2 * variance_x))
        * np.exp(-(Y - mean_y)**2 / (2 * variance_y))
    )

    # Display the heatmap
    ax.imshow(Z, cmap="rainbow", interpolation="nearest", origin="lower", aspect="auto")
    ax.set_title('2D Gaussian - Frame {}'.format(frame))

fig, ax = plt.subplots()

# Create the animation
animation = FuncAnimation(fig, update, frames=100, interval=100, repeat=False)

plt.show()
