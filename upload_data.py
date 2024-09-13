# this code will read the data from notbook dataset and will upload to mongodb

from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://harsh_arora:harsh_arora_01@cluster0.sfrra.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connect to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="harsh_project"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\\Users\\Harsh Arora\\Downloads\\sensorproject\\notebooks\\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())
"""
Example : 

name	age	city
0	Alice	25	New York
1	Bob	30	London

df.T:

         0         1
name   Alice      Bob
age      25        30
city  New York   London

df.T.to_json():

'{"0":{"name":"Alice","age":25,"city":"New York"},"1":{"name":"Bob","age":30,"city":"London"}}'

Load JSON into a dictionary:

{
  "0": {"name": "Alice", "age": 25, "city": "New York"},
  "1": {"name": "Bob", "age": 30, "city": "London"}
}

Extract values and convert to a list:


[
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "London"}
]

"""

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

print(f"Inserted {len(json_record)} records into {DATABASE_NAME}.{COLLECTION_NAME}")
