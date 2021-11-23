
import socketio
from fastapi import FastAPI

sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
app = FastAPI()
socketio_app = socketio.ASGIApp(sio, app)


@sio.event
def connect(sid, environ,auth):
    print("connect ", sid)


@sio.on('message')
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('response', 'hi ' + data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@app.get("/v2")
def read_main():
    return {"message": "Hello World"}


# NOTE: Pass credentials during connect 
# io.connect("http://127.0.0.1:3000/", {
#     auth: {
#       token: "AuthToken", #creds here 
#     },
#   }),

# Access them though def connect(sid, environ,auth): #auth params