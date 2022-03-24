from flask import Flask
from flask_cors import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)

from ChinaTrend import ChinaTrend_api
from WorldTrend import WorldTTrend_api
from flask.json import JSONEncoder as _JSONEncoder

class JSONEncoder(_JSONEncoder):
    def default(self, o):
        import decimal
        if isinstance(o, decimal.Decimal):

            return float(o)

        super(JSONEncoder, self).default(o)
app.json_encoder = JSONEncoder


app.register_blueprint(ChinaTrend_api)
app.register_blueprint(WorldTTrend_api)

if __name__ == "__main__":
    app.run(port=5000)