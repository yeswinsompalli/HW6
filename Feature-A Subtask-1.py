def get_sprint_points_from_user():
    user_input = input("Enter sprint points separated by space: ")  # Example: 30 40 50
    return [int(point) for point in user_input.split()]
