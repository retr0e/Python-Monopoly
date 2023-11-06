class Player:
    nick = 'default_name'
    money = 2000
    owned_properties = []
    current_position = 0

    def __init__(self, nick_name):
        self.nick = nick_name
        