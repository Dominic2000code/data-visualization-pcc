from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000) -> None:
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def _get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go, and how far to go.

            x_step = self._get_step()

            y_step = self._get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
