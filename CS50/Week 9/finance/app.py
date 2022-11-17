
import os
import sys

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash


from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    stocks = db.execute("SELECT symbol, price, sum(shares) AS shares, (sum(shares) * price) AS total FROM transactions GROUP BY symbol HAVING user_id = ?", user_id)
    stock_value = 0
    for line in stocks:
        stock_value += line["total"]


    return render_template("index.html", cash=cash, stocks=stocks, stock_value=stock_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    user_id = session["user_id"]

    if request.method == "POST":
        symbol = request.form.get("symbol")
        try:
            shares = float(request.form.get("shares"))
        except (AttributeError, ValueError):
            return apology("must provide number of shares", 400)

        if not shares.is_integer() or int(shares) < 1:
            return apology("must provide number of shares", 400)
        if not symbol:
            return apology("must provide stock symbol", 400)

        try:
            price = lookup(symbol)["price"]
        except TypeError:
            return apology("invalid stock symbol", 400)


        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        cash -= shares * price
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)

        db.execute(
            "INSERT INTO transactions (user_id, symbol, price, shares, date) VALUES (?, ?, ?, ?, (SELECT datetime('now')))",
            user_id,
            symbol,
            price,
            shares
        )

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute("SELECT symbol, price, shares, date FROM transactions WHERE user_id = ? ORDER BY date ASC", user_id)

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        stock = lookup(request.form.get("symbol"))
        if not stock:
            return apology("invalid stock symbol", 400)
        return render_template(
            "quoted.html",
            name=stock["name"],
            price=usd(stock["price"]),
            symbol=stock["symbol"],
        )

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        elif password != confirmation:
            return apology("password does not match", 400)

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
        except ValueError:
            return apology("username already registered", 400)

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    user_id = session["user_id"]

    if request.method == "POST":
        symbol = request.form.get("symbol")
        try:
            shares = float(request.form.get("shares"))
        except (AttributeError, ValueError):
            return apology("must provide number of shares", 400)

        if not shares.is_integer() or int(shares) < 1:
            return apology("must provide number of shares", 400)
        if not symbol:
            return apology("must provide stock symbol", 400)

        price = lookup(symbol)["price"]
        if not price:
            return apology("invalid stock symbol", 400)

        owned_shares = db.execute("SELECT SUM(shares) FROM transactions WHERE (symbol LIKE ? AND user_id = ?)", symbol, user_id)
        owned_shares = owned_shares[0]["SUM(shares)"]

        if shares > owned_shares:
            return apology("You don't own that many shares", 400)

        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        cash += shares * price
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)

        db.execute(
            "INSERT INTO transactions (user_id, symbol, price, shares, date) VALUES (?, ?, ?, ?, (SELECT datetime('now')))",
            user_id,
            symbol,
            price,
            shares * -1
        )

        return redirect("/")

    else:

        stocks = db.execute("SELECT DISTINCT symbol, sum(shares) AS shares FROM transactions GROUP BY symbol HAVING user_id = ?", user_id)

        return render_template("sell.html", stocks=stocks)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Add funds."""
    user_id = session["user_id"]
    if request.method == "POST":
        add = request.form.get("add")
        if not add or int(add) <= 0:
            return apology("enter amount to add", 400)
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + int(add), user_id)
        return render_template("added.html")


    else:
        return render_template("add.html")