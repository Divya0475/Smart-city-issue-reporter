from flask import Flask, render_template, request
import sqlite3
import uuid

app = Flask(__name__)

# -----------------------------
# DATABASE SETUP
# -----------------------------
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS issues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference_id TEXT,
            city TEXT,
            area TEXT,
            street TEXT,
            issue TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# EMAIL FUNCTION (SIMULATED)
# -----------------------------
def send_confirmation_email(receiver_email, reference_id, issue, city, area, street):
    """
    Email trigger simulation for demo purposes.
    """
    print("\n========== EMAIL TRIGGER ==========")
    print(f"To        : {receiver_email}")
    print(f"Reference : {reference_id}")
    print(f"Issue     : {issue}")
    print(f"Location  : {city}, {area}, {street}")
    print("Status    : Confirmation email triggered successfully")
    print("==================================\n")

# -----------------------------
# ROUTES
# -----------------------------
@app.route("/", methods=["GET", "HEAD"])
def index():
    return render_template("index.html", reference_id=None)

def index():
    # Initial page load → show form
    return render_template("index.html", reference_id=None)

@app.route("/submit", methods=["POST"])
def submit():
    # Debug: show full form data
    print("FORM DATA RECEIVED:", request.form)

    city = request.form.get("city")
    area = request.form.get("area")
    street = request.form.get("street")
    issue = request.form.get("issue")
    email = request.form.get("email")

    print("EMAIL RECEIVED:", email)

    reference_id = "SC-" + str(uuid.uuid4())[:8].upper()

    # Save to database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO issues (reference_id, city, area, street, issue, email)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (reference_id, city, area, street, issue, email))
    conn.commit()
    conn.close()

    # Trigger email (simulated)
    send_confirmation_email(email, reference_id, issue, city, area, street)

    # Render SAME page, but now success view will show
    return render_template("index.html", reference_id=reference_id)

if __name__ == "__main__":
    app.run(debug=True)
