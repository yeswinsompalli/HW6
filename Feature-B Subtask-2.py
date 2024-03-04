    def calculate_available_hours(self, sprint_days):
        effective_days = sprint_days - self.days_off
        average_available_hours = sum(self.available_hours_range) / 2
        return (average_available_hours - self.hours_committed_to_ceremonies) * effective_days
