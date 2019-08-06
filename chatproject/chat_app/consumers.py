# -*- coding: utf-8 -*-

from channels import Channel
from channels import Group


# to handle if a client socket is connecting to the server. You have to create a list of rooms here:
# message.channel_session[‘rooms’] = []
def websocket_connect(message):
    pass


# to handle if a client socket is disconnecting to the server.
def websocket_disconnect(message):
    pass


# to handle when the server receive messages from client socket.
# This function redirects the message to receive.chat using:
def websocket_receive(message):
    # receives a message and send it to other subscribing clients as following:
    Channel("receive").send(message)
    pass


# to handle when a new user joins a chat room.
# Here, you could notify to everybody in the room that a new user has joined the room.
# You could save the user information, for example “username”: “user-1”,
# in the message and send a message to the room with that information using send_chat function.
def join_chat(message):
    # message = { 'room_id': 2, 'username': 'smjeong' }
    pass


# to handle when a user leaves a chat room.
# Here, you could notify everybody that someone has left by calling send_chat function.
def leave_chat(message):
    pass


# to handle when a user sends a message to a chat room. Here, you must get the Group where you would send the message.
# You could get it by using this code:
# group = Group(“room-“ + str(message[“room_id”))
def send_chat(message):
    group = Group()
    data = {'message': message['comment']}
    group.send(data)
