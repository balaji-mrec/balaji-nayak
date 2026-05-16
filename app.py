import sqlite3
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# 🔧 Database create cheyyadam
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# 🏠 Home Page
@app.route('/')
def home():
    return render_template("home.html")

# 📝 Signup Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        email = request.form['email']
        pwd = request.form['password']
        cpwd = request.form['confirm_password']

        if pwd != cpwd:
            return "Passwords do not match!"

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (uname, email, pwd))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    return render_template("register.html")

app.run(debug=True)
