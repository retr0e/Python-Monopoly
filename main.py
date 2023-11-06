# class Bank:
class Player:
    nick = 'default_name'
    money = 0
    owned_properties = []


class Field:
    id = 0
    name = 'field_name'


class Tax(Field):
    money_hit = 0


class Start(Field):
    bonus = 200


class Parking(Field):
    payback = 0


class ActiveFields(Field):
    purchase = 0
    rent = []
    Owner = None
    Mortgage = 0
    Mortgage_buyout = 0


class Property(ActiveFields):
    houses = 0
    available_hotel = False
    hotel_price = 0
    house_price = 0


class Utility(ActiveFields):
    bonus = 0



