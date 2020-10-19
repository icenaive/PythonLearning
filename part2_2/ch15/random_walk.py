from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step, y_step = self.get_step()
            
            if not x_step and not y_step:
                continue
            
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
            x_directions = choice([1, -1])
            y_directions = choice([1, -1])
            x_distance = choice(list(range(5)))
            y_distance = choice(list(range(5)))

            x_step = x_directions * x_distance
            y_step = y_directions * y_distance
            
            return [x_step, y_step]