from fastapi import FastAPI
import json

app = FastAPI()

with open("json/2022_2023.json", 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
	

@app.get('/')
def get_data():
	return {"data":data}