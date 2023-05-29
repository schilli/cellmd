import numpy as np

class Particle(object):
    """Particle class"""

    def __init__(self, ndim=2):
        self.ndim = ndim
        self.init()

    def init(self):
        self.coords = np.zeros(self.ndim, dtype=np.int8)
        self.velocities = np.zeros(self.ndim, dtype=np.int8)

    def __str__(self):
        str = ""
        str += f"coords:     {self.coords}\n"
        str += f"velocities: {self.velocities}"
        return str

class Universe(object):
    """Represents the simulation universe and contains the current state, the history, etc."""

    def __init__(self, L=3, N=1, ndim=2, steps=3):
        self.L = L
        self.N = N
        self.ndim = ndim
        self.steps = steps

        self.init()

    def init(self):
        """Create cells and insert particles"""
        self.cells = np.zeros(self.ndim*[self.L], dtype=np.int8)

        for i in range(self.N):
            coords = np.random.randint(0, self.L, size=self.ndim)
            while self.cells[*coords] != 0:
                coords = np.random.randint(0, self.L, size=self.ndim)
            self.cells[*coords] = 1


    def simulate(self):
        for step in range(self.steps):
            pass


def main():
    #universe = Universe()
    print(Particle())

if __name__ == "__main__":
    main()