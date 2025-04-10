import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def f(x, a):
    return np.abs(x)**(2/3) + np.sqrt(3.3 - x**2) * np.sin(a * np.pi * x)

# Batas x agar √(3.3 - x²) tidak imajiner
x_min = -np.sqrt(3.3)
x_max = np.sqrt(3.3)
x = np.linspace(x_min, x_max, 2000)

fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

# Plot awal (a = 0)
a_init = 0
line, = ax.plot(x, f(x, a_init), 'r-', linewidth=2)

# Atur batas sumbu x dan y tetap [-10, 10]
ax.set_xlim(-7, 7)
ax.set_ylim(-5, 5)

ax.set_title(r"Grafik Hati: $f(x) = |x|^{2/3} + \sqrt{3.3 - x^2} \cdot \sin(a \pi x)$")
ax.grid(True)

# Slider untuk a
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(ax_slider, 'a', -10, 10, valinit=a_init)

def update(val):
    a = slider.val
    line.set_ydata(f(x, a))
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()