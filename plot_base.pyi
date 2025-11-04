import matplotlib.pyplot as plt

fig, ax = plt.subplots()


ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

plt.grid(True)
plt.title("Drawing Shape Classes")
plt.show()