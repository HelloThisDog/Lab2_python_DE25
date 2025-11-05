import matplotlib.pyplot as plt
"""so this is old, I could delete the file and move on but you won't see how things get to where they are"""
#following an example for a graph with shapes drawn, on geeksforgeeks
#also following a graph class example by kokchun
class plot_base():
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax

fig, ax = plt.subplots()
plt.grid(True)
plt.title("Drawing Shape Classes")
plt.show()
