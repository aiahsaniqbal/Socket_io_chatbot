import eventlet
import socketio
from Server_Processings import storing_data,call_Rasa


sio = socketio.Server(cors_allowed_origins='*')
# sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    msg='Hello From PSEB Chatbot'
    print('Bot: ', msg)
    storing_data(sid, 'user_id', sid)
    storing_data(sid, 'bot', msg)
    sio.emit("message_client", {'message': msg},room=sid)

@sio.event
def my_message(sid, data):
    msg= data.get('message')
    print('User: ', msg)

@sio.event
def message_bot(sid, data):
    sio.emit('bot_typing',{'message':'Bot is Typing...'})
    msg = data.get('message')
    storing_data(sid, 'user', msg)
    print('User: ', msg)

    response = call_Rasa(sid, msg)

    bot_response = ''
    for value in response.json():
        print('Bot : ', value.get('text'))
        storing_data(sid, 'bot', value.get('text'))
        bot_response += value.get('text')

    print('Bot: ', bot_response)
    sio.emit("message_client", {'message': bot_response},room=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('192.168.113.125', 5000)), app)