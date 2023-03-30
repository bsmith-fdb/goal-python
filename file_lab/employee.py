class Employee:
    def __init__(self, name, email_address, title, phone_number=None, identifier=None):
        self.name = name
        self.email_address = email_address
        self.title = title
        self.phone_number = phone_number
        self.identifier = identifier

    def email_signature(self, include_phone=False):
        signature = f"{self.name} - {self.title}\n{self.email_address}"
        if include_phone and self.phone_number:
            signature += f" ({self.phone_number})"
        return signature

    @classmethod
    def get_all(cls, file):
        with open(file, 'r') as file_handle:
            lines = [
                line.strip('\n').split(',') + [index + 1]
                for index, line in enumerate(file_handle.readlines())
            ]
        results = []
        for line in lines:
            results.append(cls(*line))
        return results

    @classmethod
    def get_at_line(cls, num, file):
        return Employee.get_all(file)[num-1]

    def save(self, file_name):
        emps = Employee.get_all(file_name)
        if self.identifier:
            emps[self.identifier-1] = self
        else:
            emps.append(self)
        with open(file_name, 'w') as f:
            lines = [f'{emp.name},{emp.email_address},{emp.title},{emp.phone_number}\n' for emp in emps]
            f.writelines(lines)
