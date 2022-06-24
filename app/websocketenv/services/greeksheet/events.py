from time import sleep
from flask import request
from flask_socketio import emit, join_room, leave_room,rooms
import logging
import sys
from .... import socketio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

@socketio.on('join', namespace='/greeksheet')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    join_room(message['room'])
    print("user joined the room with sid:  ",request.sid)
    count = 1
    # while True:
    #     print("Count====>",count)
    #     emit('live_count', {"count": count})
    #     count+=1
    #     print("All rooms====",rooms());
    #     print("greeksheet sids===",rooms('greeksheet'));
    #     socketio.sleep(1)

@socketio.on('leave', namespace='/greeksheet')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    leave_room(message['room'])
    print("user leaved the room with sid:  ",request.sid)



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

