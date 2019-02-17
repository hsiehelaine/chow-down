import json
import pandas as pd
import re

def foodQuery(df, selection, name):
	query_results = []
	regex = re.compile('[^a-zA-Z0-9]')
	separate_query = []
	if name is not '':
		name = regex.sub('', name)
		name = name.lower()
	df.columns = [regex.sub('', c) for c in df.columns]
	if name is not '' and name not in df.columns:
		return "oops! no recipes found with the selected ingredient"
	else:
		df_len = len(df.index)
		for i in range(0, df_len):
			if name is '':
				q_name = df.at[i, 'title']
				rating = df.at[i, 'rating']
				cal = df.at[i, 'calories']
				protein = df.at[i, 'protein']
				fat = df.at[i, 'fat']
				sodium = df.at[i, 'sodium']
				query_results.append([q_name, rating, cal, protein, fat, sodium])
			elif df.at[i, name] == 1:
				q_name = df.at[i, 'title']
				rating = df.at[i, 'rating']
				cal = df.at[i, 'calories']
				protein = df.at[i, 'protein']
				fat = df.at[i, 'fat']
				sodium = df.at[i, 'sodium']
				query_results.append([q_name, rating, cal, protein, fat, sodium])
	sort_query = 1
	rev = True
	if selection == "calories":
		sort_query = 2
		rev = False
		query_results = sorted(query_results, key=lambda x: float('inf') if x[sort_query] is None else x[sort_query], reverse=rev)
	elif selection == "protein":
		sort_query = 3
		query_results = sorted(query_results, key=lambda x: float('-inf') if x[sort_query] is None else x[sort_query], reverse=rev)
	elif selection == "fat":
		sort_query = 4
		rev = False
		query_results = sorted(query_results, key=lambda x: float('inf') if x[sort_query] is None else x[sort_query], reverse=rev)
	elif selection == "sodium":
		sort_query = 5
		rev = False
		query_results = sorted(query_results, key=lambda x: float('inf') if x[sort_query] is None else x[sort_query], reverse=rev)
	else:
		query_results = sorted(query_results, key=lambda x: float('-inf') if x[sort_query] is None else x[sort_query], reverse=rev)
	q_results = {}
	for i in range(0, 10):
		if(query_results == None or len(query_results) <= i):
			break
		value = json.dumps(query_results[i][1:])
		q_results[query_results[i][0]] = value
	q_results = json.dumps(q_results)
	return q_results