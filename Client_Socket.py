import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')


@sio.event
async def my_message(data):
    print('message received with ', data)
    await sio.emit('my response', {'response': 'my response'})

@sio.event
async def hello(data):
    print('Bot: ', data.get('message'))
    msg1 = input("User: ")
    await sio.emit("hel", {'message': msg1})

@sio.event
async def disconnect():
    print('disconnected from server')

async def main():
    await sio.connect('http://192.168.0.175:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())