import matplotlib.pyplot as plt
import numpy as np


class Bifurcation:
    def __init__(self, logistic_map_iterations, ratios_density, skip_first_k=10, x0=.5) -> None:
        self.logistic_map_iterations = logistic_map_iterations
        self.skip_first_k = skip_first_k
        self.x0 = x0
        self.ratios_number = ratios_density
        self.iteration_results = []
        self.data = {}
        assert self.skip_first_k < self.logistic_map_iterations

    def logistic_map(self, x: float, growth_rate: float) -> float:
        return growth_rate*x*(1-x)
    
    def recursive_iterator(self, growth_rate: float, results: list) -> list:
        if len(results) == 0:
            results.append(self.x0)
        if len(results) == self.logistic_map_iterations:
            return results
        else:
            results.append(self.logistic_map(results[-1], growth_rate=growth_rate))
            return self.recursive_iterator(growth_rate=growth_rate, results=results)

    def run(self):
        for r in np.linspace(0,4, self.ratios_number):
            results = []
            result = self.recursive_iterator(growth_rate=r, results=results)
            self.data[r] = result[self.skip_first_k:]
    
    def plot(self, width: float = 5, reverse=False, **kwargs):
        plt.style.use('dark_background')  # Set the dark background style
        phi = 1.4
        plt.figure(figsize=(width, width*phi))
        for key, values in self.data.items():
            x_values = [key] * len(values)  # Replicate key for the number of values
            plt.scatter(values, [(-1 if reverse else 1)*i  for i in x_values], c='white', **kwargs)

        plt.xlabel('growth ratio')
        plt.ylabel('population size')
        plt.title('rx(1-x)')
        plt.show()