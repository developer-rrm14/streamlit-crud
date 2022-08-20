import services.database as db;

INSERT = "INSERT INTO tb_client(name, age, occupation) VALUES (%s,%s,%s)"


def incluir(client):
    db.cursor.execute(INSERT, (client.name, client.age, client.occupation))
    db.conn.commit()
