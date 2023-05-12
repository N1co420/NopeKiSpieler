import socketio
import requests
import register_login_User

sio = socketio.Client() 

def connect_to_socketio_server(access_token):
   sio.connect("https://nope-server.azurewebsites.net", namespaces="/", auth={"token": access_token})


@sio.event
def disconnect():
    print("disconected")

@sio.event
def callback(data):
    print(data)

@sio.on('list:tournaments')
def socket_on(data):
   print(data)

def main():
    user = {"username": "nico", "password": "654321"}
    result = register_login_User.login(user)

    connect_to_socketio_server(result)

main()
