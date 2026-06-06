from employee import Employee

class Developer(Employee):
    def code(self):
        print(f"{self.name} is writing Python code")

    def __del__(self):
        print(f"Goodbye {self.name}! Access revoked.")