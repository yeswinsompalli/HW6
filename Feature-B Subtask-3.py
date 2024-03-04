class TeamCapacityCalculator:
    def __init__(self):
        self.team_members = []

    def add_member(self, name, days_off, hours_committed_to_ceremonies, available_hours_range):
        member = TeamMember(name, days_off, hours_committed_to_ceremonies, available_hours_range)
        self.team_members.append(member)
