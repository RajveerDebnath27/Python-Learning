class Robot:
    def __init__(self, battery_capacity,**kwargs):
        self.battery_capacity = battery_capacity
        super().__init__(**kwargs)

    def charge(self):
        print(f"Charging {self.battery_capacity}mah")
