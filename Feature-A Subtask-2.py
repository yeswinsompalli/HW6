def calculate_average_velocity(sprint_points):
    if not sprint_points:
        return 0
    return sum(sprint_points) / len(sprint_points)
