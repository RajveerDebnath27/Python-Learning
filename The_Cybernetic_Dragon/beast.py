class Beast:
    def __init__(self,fang_length,**kwargs):
        self.fang_length = fang_length
        super().__init__(**kwargs)

    def roar(self):
        print(f"Roaring with {self.fang_length}cm fangs")