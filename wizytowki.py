from faker import Faker
fake = Faker('pl_PL')


class BaseContact:
    def __init__(self, first_name, last_name, phone, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.mail = mail

    def __str__(self):
        return f"Base Card: {self.last_name} {self.first_name}, e-mail:{self.mail}, phone:{self.phone}\n"

    @property
    def label_length(self):
        return len(self.last_name) + len(self.first_name) + 1

    def base_contact(self):
        print('\nCalling {} {} on phone number: {}\n'.format(self.first_name, self.last_name, self.phone))


class BusinessContact(BaseContact):
    def __init__(self, company, job, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job
        self.business_phone = business_phone

    def __str__(self):
        return f"Business Card: {self.last_name} {self.first_name}, e-mail:{self.mail}, phone:{self.phone}\n" \
               f"\t\t\tCompany:{self.company}, Job:{self.job}, Business phone: {self.business_phone}\n"

    def business_contact(self):
        print('\nCalling {} {} on phone number:{}\n'.format(self.first_name, self.last_name, self.business_phone))


def create_base_contact(quantity):
    for i in range(quantity):
        card = BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())
        cards.append(card)


def create_business_contact(quantity):
    for i in range(quantity):
        card = BusinessContact(fake.company(), fake.job(), fake.phone_number(),
                               fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())
        cards.append(card)


card1 = BaseContact('Anna', 'Dymna', '684 201 351', 'a_dymna12@op.pl')
card2 = BusinessContact('Romp', 'Clock repairer', '889 456 632',
                        'Jolanta', 'Kozłowska', '796 267 177', 'JolantaKozlowska@armyspy.com')

cards = [card1, card2]


def get_cards():
    by_last_name = sorted(cards, key=lambda c: c.last_name)
    for card in by_last_name:
        print(card)


def call(last_name):
    for card in cards:
        if card.last_name == last_name:
            if isinstance(card, BusinessContact):
                action = input("Which number do you want to call? private/business")
                if action == 'private':
                    return card.base_contact()
                elif action == 'business':
                    return card.business_contact()
            elif isinstance(card, BaseContact):
                return card.base_contact()
            else:
                return 'Something went wrong'
    else:
        return f'Sorry you don have {last_name} in your cards.'


def menu():
    while True:
        print("1-Show Cards\n2-Add new base card\n3-Add new business card\n4-Call\n5-Exit")
        action = input("What would you like to do?")

        if action == "1":
            get_cards()

        elif action == '2':
            quantity = input('How many cards would you like to add:')
            create_base_contact(int(quantity))

        elif action == '3':
            quantity = input('How many cards would you like to add:')
            create_business_contact(int(quantity))

        elif action == '4':
            last_name = input('Who you want to call (type in last name)?')
            call(last_name)

        elif action == "5":
            return False

        else:
            print('Please choose available option.')


if __name__ == '__main__':
    menu()
