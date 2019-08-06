from channels import route
from .consumers import websocket_connect, websocket_receive, websocket_disconnect, join_chat, leave_chat, send_chat


routing_websocket = [
    route("websocket.connect", websocket_connect),
    route("websocket.receive", websocket_receive),
    route("websocket.disconnect", websocket_disconnect),
]
routing_chat = [
    route("chat.receive", join_chat, command="^join$"),
    route("chat.receive", leave_chat, command="^leave$"),
    route("chat.receive", send_chat, command="^send$"),
]