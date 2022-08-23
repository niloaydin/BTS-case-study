import websocket, json

def on_open(ws):
    print("opened")


socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"

ws = websocket.WebSocketApp(socket, on_open=on_open )
ws.run_forever()