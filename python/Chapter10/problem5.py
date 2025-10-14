class Train:
    def __init__(self, train_name, total_seats, fare_per_seat):
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare_per_seat = fare_per_seat

    def book_ticket(self, num_seats):
        if num_seats <= 0:
            return "Invalid number of seats."
        elif num_seats > self.available_seats:
            return f"Only {self.available_seats} seats are available."
        else:
            self.available_seats -= num_seats
            total_fare = num_seats * self.fare_per_seat
            return f"{num_seats} seat(s) booked successfully! Total fare: ₹{total_fare}"

    def get_status(self):
        return f"🚆 Train '{self.train_name}' has {self.available_seats} out of {self.total_seats} seats available."

    def get_fare_info(self):
        return f"Fare per seat for '{self.train_name}' is ₹{self.fare_per_seat}"


train = Train("Rajdhani Express", total_seats=100, fare_per_seat=1500)

print(train.get_fare_info())
print(train.get_status())
print(train.book_ticket(3))
print(train.get_status())
print(train.book_ticket(200))
