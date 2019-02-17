from flask import request
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import json
import pandas as pd
import re

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
  query = foodQuery(df, data['oi'])
  return jsonify(query)

#query method
def foodQuery(df, name):
	query_results = []
	regex = re.compile('[^a-z0-9]')
	name = regex.sub('', name)
	df.columns = [regex.sub('', c) for c in df.columns]
	if name not in df.columns:
		return "oops! no recipes found with the selected ingredient"
	else:
		df_len = len(df.index)
		for i in range(0, df_len):
			if df.at[i, name] == 1:
				q_name = df.at[i, 'title']
				rating = df.at[i, 'rating']
				cal = df.at[i, 'calories']
				protein = df.at[i, 'protein']
				fat = df.at[i, 'fat']
				sodium = df.at[i, 'sodium']
				query_results.append([q_name, rating, cal, protein, fat, sodium])
	query_results = sorted(query_results, key=lambda x: x[1], reverse=True)
	q_results = []
	for i in range(0, 10):
		if(query_results == None or len(query_results) <= i):
			break
		q_results.append(query_results[i])
	q_results = json.dumps(q_results)
	return q_results

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)

