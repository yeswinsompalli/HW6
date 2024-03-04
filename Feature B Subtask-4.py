    def print_individual_and_team_capacity(self, sprint_days):
        for member in self.team_members:
            print(f"{member.name} Available Effort-Hours: {member.calculate_available_hours(sprint_days)}")
        print(f"Total Team Available Effort-Hours: {self.calculate_team_capacity(sprint_days)}")
