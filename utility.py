from active_fields import ActiveFields


class Utility(ActiveFields):
    bonus = 0

    def __init__(self, identification, name, buyout):
        super().__init__(identification, name, buyout, 0)
        self.bonus = 4

    @staticmethod
    def create_utilities():
        Utility(12, 'ELEKTROWNIA', 150)
        Utility(28, 'WODOCIAGI', 150)
