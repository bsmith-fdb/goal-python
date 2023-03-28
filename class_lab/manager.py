from employee import Employee


class Manager(Employee):
    def __init__(self, name, email_address, title, phone_number=None):
        super().__init__(name=name, email_address=email_address, title=title, phone_number=phone_number)
        self.meetings = []

    def schedule_meeting(self, invitees, meeting_time):
        self.meetings.append({"time": meeting_time, "invitees": invitees})
        self.meetings.sort(key=lambda _: _["time"])

    def run_next_meeting(self):
        return self.meetings.pop(0)
