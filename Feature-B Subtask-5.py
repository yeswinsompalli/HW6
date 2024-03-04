team_capacity_calculator = TeamCapacityCalculator()
num_members = int(input("Enter the number of team members: "))
for _ in range(num_members):
    name = input("Enter team member's name: ")
    days_off = int(input("Enter days off for this member: "))
    hours_committed_to_ceremonies = int(input("Enter hours committed to ceremonies: "))
    min_hours = int(input("Enter minimum available hours per day: "))
    max_hours = int(input("Enter maximum available hours per day: "))
    available_hours_range = (min_hours, max_hours)
    team_capacity_calculator.add_member(name, days_off, hours_committed_to_ceremonies, available_hours_range)

sprint_days = int(input("Enter the number of sprint days: "))
team_capacity_calculator.print_individual_and_team_capacity(sprint_days)