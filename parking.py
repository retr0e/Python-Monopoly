from field import Field


class Parking(Field):

    payback = 0

    def __init__(self):
        super().__init__(20, 'PARKING')
