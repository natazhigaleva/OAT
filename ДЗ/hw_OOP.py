## ------------------------------ Task_1 ----------------------------- ##

class Booking:
    def __init__(self, guest, check_in, check_out, room_type):
        self.guest = guest
        self.check_in = check_in
        self.check_out = check_out
        self.room_type = room_type
        self.booked = False

    def to_book(self):
        if not self.booked:  # Проверить наличие свободных номеров
            self.booked = True
            print(f"Номер для {self.guest} с {self.check_in} по {self.check_out} успешно забронирован")
        else:
            print("К сожалению, свободных номеров нет")

    def cancel_reservation(self):  # Отменить бронь
        if self.booked:
            self.booked = False
            print(f"Бронь для {self.guest} с {self.check_in} по {self.check_out} успешно отменена")
        else:
            print(f"Номер для {self.guest} с {self.check_in} по {self.check_out} не был забронирован")

    def show(self):  # Проверить наличие свободных номеров
        if self.booked == False:
            print("Желаете забронировать номер?")
        else:
            print("Извините, свободных номеров нет")

reserv_1 = Booking("Иван Иванов", "2023-03-08", "2023-03-10", "Стандарт")
reserv_2 = Booking("Петр Петров", "2023-03-11", "2023-03-13", "Люкс")

reserv_1.to_book()
reserv_2.to_book()
reserv_1.cancel_reservation()
reserv_2.show()

## ------------------------------ Task_2 ----------------------------- ##

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def show(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Жанр: {self.genre}")

book_1 = Book("Война и мир", "Лев Толстой", "Эпопея")
book_2 = Book("Мастер и Маргарита", "Михаил Булгаков", "Роман-фантасмагория")

book_1.show()
book_2.show()

## ------------------------------ Task_3 ----------------------------- ##

class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show(self):
        print(f"Владелец: {self.owner}")
        print(f"Баланс: {self.balance}")

accaunt_1 = Bank_account("Иван Иванов", 10000)
accaunt_2 = Bank_account("Петр Петров", 20000)

accaunt_1.show()
accaunt_2.show()

## ------------------------------ Task_4 ----------------------------- ##

class Air_ticket:
    def __init__(self, flight, date, seat, cost):
        self.flight = flight
        self.date = date
        self.seat = seat
        self.cost = cost
        self.booked = False

    def to_book(self):
        if not self.booked:
            self.booked = True
            print(f"Билет на рейс {self.flight} на {self.date} успешно забронирован.")
        else:
            print("Билет уже забронирован.")

    def cancel_reservation(self):
        if self.booked:
            self.booked = False
            print(f"Бронь билета на рейс {self.flight} на {self.date} успешно отменена.")
        else:
            print("Билет не забронирован.")

    def show(self):
        print(f"Рейс: {self.flight}")
        print(f"Дата: {self.date}")
        print(f"Место: {self.seat}")
        print(f"Стоимость: {self.cost}")
        print(f"Забронирован: {self.booked}")

ticket_1 = Air_ticket("SU1234", "2023-03-08", "Москва - Санкт-Петербург", 5000)
ticket_2 = Air_ticket("Аэрофлот2345", "2023-03-15", "Санкт-Петербург - Москва", 6000)

ticket_1.show()
ticket_2.show()

ticket_1.to_book()
ticket_2.to_book()

ticket_1.show()
ticket_2.show()

ticket_1.cancel_reservation()

ticket_2.show()