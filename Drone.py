class Drone:
    total_cost = 100
    total_km = 0
    def __init__(self, cost_per_km=0.01):
        self.cost_per_km = cost_per_km

    def calculate_cost(self, kilometers):
        self.total_cost += (self.cost_per_km * kilometers)
