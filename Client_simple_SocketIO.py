import socketio


sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def hello(data):
    print('Bot: ', data.get('message'))
    msg1 = input("User: ")
    sio.emit("hel", {'message': msg1})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.0.175:5000')
sio.wait()