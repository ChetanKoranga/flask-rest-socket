from app import socketio, create_app

start_app = create_app()

if __name__ == "__main__":
    socketio.run(app, port=3500)
