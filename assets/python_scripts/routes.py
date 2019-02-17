from flask import request
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd

from pyscript import foodQuery

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
@cross_origin(supports_credentials=True)
def hello():
  return jsonify({'success': 'ok'})

@app.route("/oi")
@cross_origin(supports_credentials=True)
def oi():
  return "oi"

@app.route("/queryresult", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def query_result():
  data = request.json
  df = pd.read_csv("epi_r.csv")
  df = df.replace({pd.np.nan: None})
  query = foodQuery(df, data['srt'], data['srl'])
  return jsonify(query)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)

