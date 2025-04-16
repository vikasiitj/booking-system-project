import uuid

# Dummy in-memory database (use a real one like PostgreSQL in production)
tickets = {
    "Delhi": 50,
    "Mumbai": 40,
    "Chennai": 30,
    "Kolkata": 25
}

bookings = []

def search_tickets():
    return tickets

def book_ticket(city, user):
    if city in tickets and tickets[city] > 0:
        tickets[city] -= 1
        ticket_id = str(uuid.uuid4())[:8]
        bookings.append({
            "ticket_id": ticket_id,
            "city": city,
            "user": user
        })
        return {"ticket_id": ticket_id, "city": city, "user": user}, 200
    else:
        return {"error": "No tickets available for selected city!"}, 400

def get_all_bookings():
    return bookings
