# Bitmex API Helper for Python Flask
#### Implementation of [Bitmex](https://github.com/BitMEX/api-connectors/tree/master/official-http/python-swaggerpy) API connectors in Flask 
### Create [virtual environment]('https://docs.python.org/3/library/venv.html) and install requirements 
```sh
pip install -r requirements.txt
```
### Need API Key and API Secret from [Bitmex Test](https://testnet.bitmex.com/app/apiKeys)
- Add `api_key` and `api_secret` in [app](./src/app.py)
#### List of Implemented Routes
| Request | Endpoint |  Details |
| --- | --- | --- |
| `GET` | `http://127.0.0.1:5000/data/order`| Get Orders Data|
| `GET` | `http://127.0.0.1:5000/data/instrument`| Get Instrument Data|
| `GET` | `http://127.0.0.1:5000/data/position`| Get Position Data|
| `GET` | `http://127.0.0.1:5000/data/quote`| Get Quote Data|

- To see route list from cli `flask routes`

### Lets run the App
```sh
python app.py 
```
