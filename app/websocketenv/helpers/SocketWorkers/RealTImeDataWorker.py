# make sure to use eventlet and call eventlet.monkey_patch()
import eventlet
from .... import socketio
from flask_socketio import emit

eventlet.monkey_patch()

# gloabal worker
workerObject = None


class RealTimeDataWorker(object):
    switch = False
    unit_of_work = 0

    def __init__(self, sio):
        """
        assign socketio object to emit
        """
        self.socketio = sio
        self.switch = True

    def do_work(self, eventname, func, interval=1):
        """
        do work and emit message
        """
        while self.switch:
            print("unit of work: ", self.unit_of_work)
            # must call emit from the socket io
            # must specify the namespace
            self.socketio.emit(
                eventname, {"data": func()}, room="greeksheet", namespace="/greeksheet"
            )
            # important to use eventlet's sleep method
            eventlet.sleep(interval)

    def stop(self):
        """
        stop the loop
        """
        self.switch = False


def connect():
    """
    connect
    """
    global worker
    worker = RealTimeDataWorker(socketio)
    print("Worker COnnected::::::::::::::")
    emit("re_connect", {"msg": "connected"})


def start_work(eventname, func, interval):
    """
    trigger background thread
    """
    emit("update", {"msg": "Starting Worker"})
    # notice that the method is not called - don't put braces after method name
    socketio.start_background_task(worker.do_work, eventname, func, interval)


def stop_work():
    """
    trigger background thread
    """
    try:
        worker.stop()
        emit("update", {"msg": "worker has been stoppped"})
    except Exception as e:
        print("Worker is not defined yet....")
