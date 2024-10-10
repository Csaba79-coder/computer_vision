import matplotlib.pyplot as plt
import numpy as np

class SineCurveManager:
    def __init__(self):
        self.x = np.linspace(0, 2 * np.pi, 100)
        self.y = np.sin(self.x)

    def plot_sine_curve(self):
        plt.plot(self.x, self.y)

        plt.title('Sinus görbe')
        plt.xlabel('X tengely')
        plt.ylabel('Y tengely')

        plt.show()

if __name__ == '__main__':
    manager = SineCurveManager()
    manager.plot_sine_curve()