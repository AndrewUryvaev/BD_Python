import psycopg2

def create_table(cur):
    cur.execute("""CREATE TABLE client(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL
                last_name VARCHAR(50) NOT NULL,
                email VARCHAR(50) UNIQUE);
               """)

    cur.execute("""CREATE TABLE client_phone(
                id_phone SERIAL PRIMARY KEY,
                id_client INTEGER NOT NULL REFERENCES client(id),
                phone VARCHAR(20) UNIQUE);
                """)

    conn.commit()

def add_client(cur, name, last_name, email):
    cur.execute("""INSERT INTO client(name, last_name, email)
                VALUES(%s, %s, %s);
                """, (name, last_name, email))

def add_phone(cur, id_client, phone):
    cur.execute("""INSERT INTO client_phone(id_client, phone)
                VALUES(%s, %s);
                """, (id_client, phone))

def change_client(id, nam=None, surn=None, em=None, phon=None):
    if num is not None:
        cur.execute("""UPDATE client SET name=%s
                    WHERE id=%s;
                    """, (nam, id))
    if surn is not None:
        cur.execute("""UPDATE client SET last_name=$s
                    WHERE id=%s;
                    """, (surn, id))
    if em is not None:
        cur.execute("""UPDATE client SET email=%s
                    WHERE id=%s;
                    """, (em, id))
    if phon is not None:
        cur.execute("""UPDATE client_phone SET phone=%s
                    WHERE id_client=%s;
                    """, (phon, id))

    print(f'Данные телефона клиента с id {id} изменены.')


def del_phone(id, phon):
    cur.execute("""DELETE FROM client_phone
                WHERE id_client=%s AND phone=%s;
                 """, (id, phon))

def del_client(id_name):
    cur.execute("""DELETE FROM client_phone
                WHERE id_client=%s;
                """, (id_name, ))
    cur.execute("""DELETE FROM client
                WHERE id=%s;
                """, (id_name, ))

def find_client(search):
    cur.execute("""SELECT * FROM client AS c
                LEFT JOIN client_phone AS cp ON c.id = cp.id_client
                WHERE c.name LIKE %s;
                """, (search, ))
    if cur.fetchone() is not None:
        print(cur.fetchone()[0], cur.fetchone()[1], cur.fetchone()[2], cur.fetchone()[3], cur.fetchone()[6])
        return
    cur.execute("""SELECT * FROM client AS c
                LEFT JOIN client_phone AS cp ON c.id = cp.id_client
                WHERE c.last_name LIKE %s;
                """, (search, ))
    if cur.fetchone() is not None:
        print(cur.fetchone()[0], cur.fetchone()[1], cur.fetchone()[2], cur.fetchone()[3], cur.fetchone()[6])
    cur.execute("""SELECT * FROM client AS c
                LEFT JOIN client_phone AS cp ON c.id = cp.id_client
                WHERE c.email LIKE %s;
                """, (search, ))
    if cur.fetchone() is not None:
        print(cur.fetchone()[0], cur.fetchone()[1], cur.fetchone()[2], cur.fetchone()[3], cur.fetchone()[6])
    cur.execute("""SELECT * FROM client AS c
                LEFT JOIN client_phone AS cp ON c.id = cp.id_client
                WHERE cp.phone LIKE %s;
                """, (search, ))
    if cur.fetchone() is not None:
        print(cur.fetchone()[0], cur.fetchone()[1], cur.fetchone()[2], cur.fetchone()[3], cur.fetchone()[6])



if __name__ == '__main__':
    with psycopg2.connect(database="", user="", password="") as conn:
        with conn.cursor() as cur:
            create_table()
            add_client(1, 'Andrew', 'Uryvaev', 'andrej.2000@mail.ru')
            add_phone(2, '2', '9251002645')
            change_client(3, 'Filipov', 'Egor', 'filipov.E2017@mail.ru', '9521789052')
            del_phone(3, '9521789052')
            del_client(4)
            find_client('Egor')

conn.close()




















