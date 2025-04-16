from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from booking_logic import search_tickets, book_ticket, get_all_bookings

app = Flask(_name_)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    tickets = search_tickets()
    return render_template("search.html", tickets=tickets)

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        user = request.form.get('user')
        city = request.form.get('city')
        if not user or not city:
            flash("Both fields are required!", "danger")
            return redirect(url_for('book'))

        result, status = book_ticket(city, user)
        if status == 200:
            flash("✅ Booking successful!", "success")
        else:
            flash(f"❌ {result['error']}", "danger")
        return redirect(url_for('book'))
    return render_template("book.html")

@app.route('/bookings', methods=['GET'])
def bookings():
    all_bookings = get_all_bookings()
    return render_template("bookings.html", bookings=all_bookings)

@app.route('/')
def home():
    return "Booking service is running!"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
