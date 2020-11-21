from faker import Faker
fake = Faker('pl_PL')


class BaseContact:
    def __init__(self, first_name, last_name, phone, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.mail = mail

    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name) + 1

    def contact(self):
        print('Wybieram numer {} i dzwonię do {} {}'.format(self.phone, self.first_name, self.last_name))


class BusinessContact(BaseContact):
    def __init__(self, company, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.job = job


def create_contacts(kind, quantity):
    if kind == 'base':
        for i in range(quantity):
            card = BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())
            cards.append(card)
    elif kind == 'business':
        for i in range(quantity):
            card = BusinessContact(fake.company(), fake.job(),
                                   fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())
            cards.append(card)


cards = []


def menu():
    while True:
        print("1-Show Cards")
        print("2-Add new base card")
        print("3-Add new business card")
        print("4-Exit")

        action = input("What would you like to do?")

        if action == "4":
            return False

        elif action == "1":
            by_last_name = sorted(cards, key=lambda c: c.last_name)
            for card in by_last_name:
                print('-{} {} - {}'.format(card.last_name, card.first_name, card.phone))

        elif action == '2':
            a = 'base'
            b = input('How many cards would you like to add:')
            create_contacts(a, int(b))

        elif action == '3':
            a = 'business'
            b = input('How many cards would you like to add:')
            create_contacts(a, int(b))

        else:
            print('Please choose available option.')


if __name__ == '__main__':
    menu()
