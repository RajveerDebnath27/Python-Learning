class Car:
    def __init__(self,wheels,**kwargs):
        self.wheels = wheels
        super().__init__(**kwargs)

    def drive(self):
        print(f"Driving in land with {self.wheels} wheels")