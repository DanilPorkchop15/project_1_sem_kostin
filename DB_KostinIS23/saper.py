import sqlite3 as sq
from data_users import info_users

with sq.connect('saper.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )""")
    # cur.execute("INSERT INTO users VALUES (1, 'Алексей', 1, 22, 1000)")
    # cur.execute("INSERT INTO users VALUES (2, 'Виктор', 1, 25, 1500)")
    # cur.execute("INSERT INTO users VALUES (3, 'Надежда', 2, 19, 900)")
    # cur.execute("INSERT INTO users VALUES (4, 'Александр', 1, 29, 3500)")
    # cur.execute("INSERT INTO users VALUES (5, 'Данил', 1, 17, 9999)")
    # cur.execute("INSERT INTO users VALUES (7, 'Лиза', 2, 19, 200)")
    # cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)
    # cur.execute("SELECT * FROM users")
    # players = cur.fetchall()
    # cur.execute("SELECT * FROM users WHERE sex = 2")
    # women = cur.fetchall()
    # cur.execute("SELECT * FROM users WHERE score < 1000")
    # under1000 = cur.fetchall()
    # cur.execute("SELECT * FROM users WHERE score=(SELECT MAX(score) FROM users)")
    # maxScore = cur.fetchall()
    # cur.execute("SELECT * FROM users WHERE old BETWEEN 18 AND 20 ")
    # old = cur.fetchall()
    # cur.execute("UPDATE users SET score = score+100 WHERE name LIKE 'Д%'")
    # cur.execute("UPDATE users SET old = 20 WHERE old = 19")
    # cur.execute("UPDATE users SET score = score+300 WHERE score < 1000")
    # cur.execute("UPDATE users SET score = score+100 WHERE old >= 20")
    # cur.execute("DELETE FROM users WHERE score=1270")

# print(players)
# print(women)
# print(under1000)
# print(maxScore)
# print(old)
