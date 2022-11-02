import asyncio
import base64

import cv2
import websockets

async def start():
    uri = "ws://3.36.68.46:53418"
    async with websockets.connect(uri) as websocket:
        Data = {'kind': 0, 'roomNumber' : "1234"}
        await websocket.send(str(Data))
        send_t = asyncio.create_task(sendImg(websocket))
        recvT = asyncio.create_task(recvCom(websocket))
        await recvT
        await send_t

async def recvCom(websocket):
    while(1):
        get = await websocket.recv()
        print(get)

async def sendImg(websocket):
    capture = cv2.VideoCapture(0)
    while cv2.waitKey(33) < 0:
            ret, frame = capture.read()
            img = cv2.imencode('.jpg',frame)
            
            await websocket.send(base64.b64encode(img[1]).decode('utf-8'))

asyncio.get_event_loop().run_until_complete(start())