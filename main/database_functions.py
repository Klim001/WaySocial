PATH = 'perso.db'


def create_db(path):
    import sqlite3
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS persons(
        id INTEGER,
        username CHAR NOT NULL,
        password CHAR NOT NULL,
        balance FLOAT NOT NULL, 
        entry BOOL NOT NULL   
    )''')
    return


def wright_entry(path, name, password):
    import sqlite3
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute("""SELECT * FROM persons WHERE username = ?""", (name,))
    list_ = cursor.fetchall()
    for i in list_:
        if password == i[2]:
            return [i[0], i[1], i[2], i[3]]
    return 0


def add_to_db(path, data):
    import sqlite3
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute("""SELECT username FROM persons""")
    list_ = cursor.fetchall()
    list_ = [str(x[0]) for x in list_]
    if data['username'] not in list_:
        cursor.execute("""INSERT INTO persons (id, username, password, balance, entry) VALUES (?, ?, ?, ?, ?)""",
                       (data['id'], data['username'], data['password'], 0, True))
        connect.commit()
        connect.close()
        return [1, 'Успешная регистрация']
    else:
        return [0, 'Такой никнейм уже занят']


if __name__ == '__main__':
    create_db(PATH)
    add_to_db(PATH, {'id': 1, 'username': 'go', 'password': 'ppp'})
    print(wright_entry(PATH, 'go', 'ppp'))
