import logging
from random import randint
import sys
from flask import request
from flask_socketio import emit, join_room, leave_room, rooms
from app.websocketenv.helpers.SocketWorkers.RealTImeDataWorker import (
    connect,
    start_work,
    stop_work,
)
from .... import socketio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

clients = []
namespace_var = "/greeksheet"


def sendGreekSheetData():
    data = randint(1, 99999999)
    return data


@socketio.on("join", namespace=namespace_var)
def joined(message):
    global clients
    roomname = message["room"]
    print("ROOm===>>", rooms())
    con_sid = request.sid
    join_room(roomname, con_sid, namespace_var)
    if len(clients) == 0:
        connect()
        start_work("live_count", sendGreekSheetData, roomname, namespace_var, 2)
    clients.append(request.sid)
    clients = list(set(clients))
    print("user joined the room with sid:  ", con_sid)
    print("All rooms====", rooms())
    print("All clients====>>> ", clients)


@socketio.on("leave", namespace=namespace_var)
def leaved(message):
    con_sid = request.sid
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    leave_room(message["room"])
    print("user leaved the room with sid:  ", con_sid)
    print("All clients====>>> ", clients)
    if clients and con_sid in clients:
        clients.remove(con_sid)
    print("All rooms====", rooms())
    if len(clients) == 0:
        stop_work()


@socketio.on("disconnect", namespace=namespace_var)
def disconnected():
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    print("Auto Disconnection: ", request.sid)

    if clients:
        clients.remove(request.sid)
    print("user leaved the room with sid:  ", request.sid)
    if len(clients) == 0:
        stop_work()
    print("All clients====>>> ", clients)
    print("All rooms====", rooms())
