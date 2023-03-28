class Employee:
    def __init__(self, name, email_address, title, phone_number=None):
        self.name = name
        self.title = title
        self.email_address = email_address
        self.phone_number = phone_number

    def email_signature(self, include_phone=True):
        sig = f"{self.name} - {self.title}\n{self.email_address}"
        if include_phone and self.phone_number:
            sig += f" ({self.phone_number})"
        return sig
