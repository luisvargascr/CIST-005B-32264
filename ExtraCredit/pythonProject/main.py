class Employee:
    def __init__(self, name):
        self.name = name
        self.remaining_colleagues = []

    def add_colleague(self, colleague):
        self.remaining_colleagues.append(colleague)

    def remove_colleague(self, colleague):
        self.remaining_colleagues.remove(colleague)


class MeetingScheduler:
    def __init__(self, employees):
        self.employees = {employee.name: employee for employee in employees}

    def schedule_meetings(self):
        for week in range(len(self.employees) - 1):
            for employee in self.employees.values():
                if employee.remaining_colleagues:
                    colleague = employee.remaining_colleagues.pop(0)
                    print(f"Week {week + 1}: {employee.name} meets {colleague.name}")
                    colleague.remove_colleague(employee)

    def print_remaining_colleagues(self):
        for employee in self.employees.values():
            print(f"{employee.name} remaining colleagues: {[colleague.name for colleague in employee.remaining_colleagues]}")


# Creating employees
employees = [Employee("Employee {}".format(i)) for i in range(1, 7)]

# Assigning initial list of remaining colleagues for each employee
for i, employee in enumerate(employees):
    employee.remaining_colleagues = employees[:i] + employees[i+1:]

# Creating a scheduler
scheduler = MeetingScheduler(employees)

# Schedule meetings
scheduler.schedule_meetings()

# Print remaining colleagues for each employee after scheduling
scheduler.print_remaining_colleagues()
