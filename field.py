class Field:
    id = 0
    name = 'field_name'

    def __init__(self, identification, name):
        self.id = identification
        self.name = name

    def interact(self):
        print(self.name)

    @staticmethod
    def create_fields():
        fields = [Field(2, 'KASA SPOLECZNA'), Field(7, 'SZANSA'),
                  Field(17, 'KASA SPOLECZNA'), Field(22, 'SZANSA'),
                  Field(33, 'KASA SPOLECZNA'), Field(36, 'SZANSA'),
                  Field(10, 'ODWIEDZINY'), Field(30, 'NIE IDZ DO WIEZIENIA')]

        return fields
