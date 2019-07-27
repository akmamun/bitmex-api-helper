from flask import Flask
import json
from flask_cors import CORS
from bitmex import bitmex

app = Flask(__name__)
CORS(app)

# result = client.Instrument.Instrument_get(filter=json.dumps({'rootSymbol': 'XBT'})).result()
client = bitmex.bitmex(api_key=<api_key>, api_secret=<api_secret>)

@app.route("/")
def index():
    return "bitmex api"

@app.route("/order/data")
def order():
    order_data = client.Order.Order_getOrders(symbol="XBTUSD", reverse=True).result()   #order data
    return json.dumps(order_data,default=str) #default=str for datetime filter

@app.route("/instrument/data")
def instrument():
    instrument_data = client.Instrument.Instrument_get(symbol="XBTUSD", reverse=True).result()   #Instrument data
    return json.dumps(instrument_data,default=str)

@app.route("/position/data")
def position():
    position_data= client.Position.Position_get(filter=json.dumps({'symbol': 'XBTUSD'})).result() #position data give param error if not use filter
    return json.dumps(position_data,default=str)

if __name__ == '__main__':
    app.run()
