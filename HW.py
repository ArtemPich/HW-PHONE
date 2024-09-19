import psycopg2

def create_db (conn):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS client(
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    email VARCHAR(40),
    phones INTEGER NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phone(
    phone_id SERIAL PRIMARY KEY,
    phone INTEGER NOT NULL
    id_client INTEGER NOT NULL REFERENCES client(client_id)
    );
    """)
    return cur.fetchone()

def add_client(conn):
    cur.execute("""
    INSERT INTO client
    VALUES (client_id, "first_name", "last_name", "email", phones
    ); 
    """)

def add_phone(conn):
    cur.execute("""
    INSERT INTO phone
    VALUES (phone_id, phone, id_client
    );
    """)
    conn.commit()

def change_client(conn):
    cur.execute("""
    INSERT INTO client VALUES(1,"Peter", "Ivanov", "Ivanov@gmail.com", 89041354020
    );
    """)
    conn.commit()

def change_phone(conn):
    cur.execute("""
    INSERT INTO phone VALUES(1, 8901305020
    );
    """)
    conn.commit()

def delete_phone(conn):
    cur.execute("""
    DELETE FROM phone WHERE client_id=%s
    );
    """)
    cur.execute("""
    SELECT FROM phone;
    """)
    return cur.fetchone()

def delete_client(conn):
    cur.execute("""
    DELETE FROM client WHERE client_id=%s;
    """)
    cur.execute("""
    SELECT * FROM client;
    """)
    return cur.fetchone()

def find_client(conn):
    cur.execute("""
    SELECT * FROM client;
    """)
    print('fetchall', cur.fetchall())

conn = psycopg2.connect(database="clients_db", user="postgres", password="postgres")
with conn.cursor() as cur :
    print()

conn.close()
