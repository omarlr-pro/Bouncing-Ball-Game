import mysql.connector
from datetime import datetime
import hashlib

class MySQLAuthentication:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.username = None  # Initialize username attribute

    def register(self, username, password):
        try:
            # Hash the password using SHA-256
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            self.cursor.execute(sql, (username, hashed_password))
            self.conn.commit()
            print("Registration successful!")
        except mysql.connector.Error as err:
            print("Registration failed:", err)

    def login(self, username, password):
        try:
            # Hash the password provided by the user for comparison
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            sql = "SELECT * FROM users WHERE username = %s AND password = %s"
            self.cursor.execute(sql, (username, hashed_password))
            user = self.cursor.fetchone()
            if user:
                print("Login successful!")
                self.username = username  # Store the username
                return True
            else:
                print("Invalid username or password!")
                return False
        except mysql.connector.Error as err:
            print("Login failed:", err)

    def update_last_activity(self, username):
        try:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sql = "UPDATE users SET lastactivity = %s WHERE username = %s"
            self.cursor.execute(sql, (now, username))
            self.conn.commit()
            print("Last activity updated!")
        except mysql.connector.Error as err:
            print("Failed to update last activity:", err)
