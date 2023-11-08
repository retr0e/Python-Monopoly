from active_fields import ActiveFields


class Railway(ActiveFields):

    def __init__(self, identification, name, buyout, rent):
        super().__init__(identification, name, buyout, rent)

    def interact(self, player, player_list):
        super().interact()

    @staticmethod
    def create_railways():
        railways = [Railway(5, 'DWORZEC ZACHODNI', 200, [25, 50, 100, 200]),
                    Railway(15, 'DWORZEC GDANSKI', 200, [25, 50, 100, 200]),
                    Railway(25, 'DWORZEC WSCHODNI', 200, [25, 50, 100, 200]),
                    Railway(35, 'DWORZEC CENTRALNY', 200, [25, 50, 100, 200])]

        return railways
