import asyncio
import base64

import cv2
import numpy as np
import websockets
import time


async def start():
    uri = "ws://3.36.68.46:53418"
    async with websockets.connect(uri) as websocket:
        Data = {'kind': 1, 'roomNumber' : "1234"}
        await websocket.send(str(Data))
        data = await websocket.recv()
        if(data == "Connect Room"):
             recvI = asyncio.create_task(recvImg(websocket))
             sendC = asyncio.create_task(sendMessage(websocket))
             await recvI
             await sendC

async def sendMessage(websocket):
    while(1):
        command = "hello Server"
        await websocket.send(str({'who':"master","command":command}))
        await asyncio.sleep(5.0)


async def recvImg(websocket):
    while cv2.waitKey(33) < 0:
        get = await websocket.recv()
        get = base64.b64decode(get)
        encoded_img = np.fromstring(get, dtype = np.uint8)
        img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
        cv2.imshow("Video",img)


asyncio.get_event_loop().run_until_complete(start())