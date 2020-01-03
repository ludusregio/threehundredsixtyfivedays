class Robot:

    def __init__(self, designation, model, color, weight):
        self.designation = designation
        self.model = model
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f'My designation is {self.designation}')
