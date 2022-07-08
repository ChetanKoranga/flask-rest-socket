import logging
from socket import SocketIO
import sys
from time import sleep

from flask import request
from flask_socketio import emit, join_room, leave_room, rooms

from .... import socketio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

clients = []

@socketio.on('join', namespace='/greeksheet')
def joined(message):
    flag = True
    print('ROOm===>>',rooms())
    if 'greeksheet' in rooms():
        print("Flag triggered===")
        flag = False
    
    join_room(message['room']) 
    clients.insert(request.sid)
    
    
    print("user joined the room with sid:  ",request.sid)
    print("All rooms====",rooms())
    print("All the clients connected===>")
    emit('live_count', {"count": 100},rooms=message['room'])
    # room = rooms()
    count = 1
    if flag:
        while ('greeksheet' in room):
            # print("Room====>",room)
            room = rooms()
            count+=1
            print("count======",count)
            emit('live_count', {"count": count},room=message['room'])
            socketio.sleep(2)
            emit('live_count', {"count": count},rooms=message['room'])
            count+=1
            print("All rooms====",rooms())
            print("greeksheet sids===",rooms('greeksheet'))
            socketio.sleep(1)



@socketio.on('leave', namespace='/greeksheet')
def leaved(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    leave_room(message['room'])
    print("user leaved the room with sid:  ",request.sid)
    print("All rooms====",rooms())
    

@socketio.on('get_sheet_data', namespace='/greeksheet')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all subsciber in the room."""
    pass


# @socketio.on('left', namespace='/chat')
# def left(message):
#     """Sent by clients when they leave a room.
#     A status message is broadcast to all people in the room."""
#     room = session.get('room')
#     leave_room(room)
#     emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

