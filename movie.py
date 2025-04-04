class MovieTicketBookingSystem:
    def __init__(self):
        self.movies = {}
        self.bookings = {}

    def add_movie(self, movie_id, movie_name, available_seats):
        self.movies[movie_id] = {
            "name": movie_name,
            "available_seats": available_seats
        }
        print(f"Movie '{movie_name}' added with {available_seats} seats.")

    def book_ticket(self, movie_id, customer_name):
        if movie_id not in self.movies:
            print("Movie ID not found.")
            return

        movie = self.movies[movie_id]
        if movie["available_seats"] > 0:
            movie["available_seats"] -= 1
            if movie_id not in self.bookings:
                self.bookings[movie_id] = []
            self.bookings[movie_id].append(customer_name)
            print(f"Ticket booked for '{movie['name']}' by {customer_name}.")
        else:
            print(f"No seats available for '{movie['name']}'.")

    def show_movies(self):
        if not self.movies:
            print("No movies available.")
            return

        print("Available movies:")
        for movie_id, movie in self.movies.items():
            print(f"ID: {movie_id}, Name: {movie['name']}, Available Seats: {movie['available_seats']}")

    def show_bookings(self):
        if not self.bookings:
            print("No bookings available.")
            return

        print("Bookings:")
        for movie_id, customers in self.bookings.items():
            movie_name = self.movies[movie_id]["name"]
            print(f"Movie: {movie_name}")
            for customer in customers:
                print(f" - {customer}")


# Create an instance of the booking system
booking_system = MovieTicketBookingSystem()

# Add movies
booking_system.add_movie(1, "The Matrix", 5)
booking_system.add_movie(2, "Inception", 3)

# Show available movies
booking_system.show_movies()

# Book tickets
booking_system.book_ticket(1, "Alice")
booking_system.book_ticket(1, "Bob")
booking_system.book_ticket(2, "Charlie")

# Show bookings
booking_system.show_bookings()

# Try to book a ticket for a non-existent movie
booking_system.book_ticket(3, "David")

# Try to book a ticket for a movie with no available seats
booking_system.book_ticket(1, "Eve")
booking_system.book_ticket(1, "Frank")
booking_system.book_ticket(1, "Grace")
booking_system.book_ticket(1, "Hannah")

# Show available movies again
booking_system.show_movies()
