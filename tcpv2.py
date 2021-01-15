#!/usr/bin/env python

import asyncio
import websockets

print("Remote connection satrting on 192.168.0.43 and port 5000")
async def echo(websocket, path):
    admin = 0
    async for message in websocket:
        if message == "test123":
            message = "password:Access Granted"
            await websocket.send(message)
            print("Request Made. Authorized access.")
            admin = 1
        elif message == "123456" and admin == 1:
            await websocket.send("Light is on")
            await websocket.send(f'Message recieved: {message}')
            admin = 1
        else:
            await websocket.send(f'Message Recieved: {message}')
            print("Request Made")
        
start_server = websockets.serve(echo, "192.168.0.43", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
