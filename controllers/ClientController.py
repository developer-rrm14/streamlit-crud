import services.database as db;
import utils.query as query;
import models.Client as client;
import asyncio
import aiopg


def insert(client):
    db.cursor.execute(query.INSERT_CLIENT, (client.name, client.age, client.occupation))
    db.conn.commit()


def delete(id):
    db.cursor.execute(query.DELETE_CLIENT_BY_ID, str(id))
    db.conn.commit()


def selectAll():
    db.cursor.execute(query.SELECT_ALL_CLIENTS)
    client_list = []

    for row in db.cursor.fetchall():
        client_list.append(client.Client(row[0], row[1], row[2], row[3]))

    return client_list
