import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()

# Создание таблицы пользователей, если она не существует
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL)''')

# Регистрация нового пользователя
def register_user(name, email, password):
    try:
        cursor.execute('''INSERT INTO users (name, email, password)
                          VALUES (?, ?, ?)''', (name, email, password))
        conn.commit()
        print("Регистрация прошла успешно")
    except sqlite3.IntegrityError:
        print("Пользователь с таким email уже существует")

# Авторизация пользователя
def login_user(email, password):
    cursor.execute('''SELECT * FROM users WHERE email=? AND password=?''',
                   (email, password))
    user = cursor.fetchone()
    if user:
        print("Авторизация прошла успешно")
    else:
        print("Неверный email или пароль")

# Пример использования функций
register_user("Иван", "ivan@example.com", "qwerty")
login_user("ivan@example.com", "qwerty")

# Закрытие соединения с базой данных
conn.close()