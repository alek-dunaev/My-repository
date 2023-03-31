class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'

    def get_guest(self):
        return f'{self.name} {self.surname} {self.city}'


a = Client("Иван", "Петров", "Пермь", 50)
b = Client('Владимир','Зайцев','Кострома',50)
c = Client('Олеся','Янина','Новосибирск',50)

guest_list = [a, b, c]

for guest in guest_list:
    print(guest.get_guest())
