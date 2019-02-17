import pandas as pd
import json

def foodQuery(df, name):
	query_results = []
	if name not in df.columns:
		return "oops! no recipes found with the selected ingredient"
	else:
		df_len = len(df.index)
		for i in range(0, df_len):
			if df.at[i, name].astype(int) == 1:
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
	print(type(q_results))
	return q_results

df = pd.read_csv("epi_r.csv")
print(foodQuery(df, "octopus"))
