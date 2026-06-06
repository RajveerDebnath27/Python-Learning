class Boat:
    def __init__(self,propellers,**kwargs):
        self.propellers = propellers

        super().__init__(**kwargs)

    def swim(self):
        print(f"swmming in water with {self.propellers} propellers")
