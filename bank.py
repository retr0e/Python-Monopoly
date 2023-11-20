class Bank:
    @staticmethod
    def trade_properties(seller, buyer):
        i = 0
        for prop in seller.owned_properties:
            print(i, ' ' + prop.name)
            i += 1

        property_for_sale = int(input('Ktore z tych pol chcesz sprzedac?'))
        while property_for_sale < 0 or property_for_sale > len(seller.owned_properties):
            property_for_sale = int(input('Ktore z tych pol chcesz sprzedac?'))

        property_for_sale_price = int(input('Podaj cene nieruchomości'))

        print('Czy akceptujesz kupno: ', seller.owned_properties[property_for_sale], ' za: '
              , str(property_for_sale_price))

        print('1 - Kupuje')
        print('2 - Odrzucam oferte')
        buyer_decision = int(input('Decyzja kupca'))

        while buyer_decision < 1 or buyer_decision > 2:
            buyer_decision = int(input('Decyzja kupca'))

        match buyer_decision:
            case 1:
                seller.money += property_for_sale_price
                buyer.money -= property_for_sale_price

                seller.owned_properties[property_for_sale].owner = buyer
                buyer.owned_properties.append(seller.owned_properties[property_for_sale])

                seller.owned_properties.pop(property_for_sale)
                print('Oferta przyjęta pieniądze zostały przelane!')
            case 2:
                print('Oferta odrzucona... gra się kontynuje...')
                return None
